# Nuxt API Design Guide for User Data Operations

## File Structure

```
project-root/
├── server/
│   ├── api/
│   │   ├── auth/
│   │   │   ├── login.post.ts
│   │   │   ├── logout.post.ts
│   │   │   └── refresh.post.ts
│   │   ├── users/
│   │   │   ├── index.get.ts           # GET /api/users
│   │   │   ├── index.post.ts          # POST /api/users
│   │   │   ├── [id].get.ts            # GET /api/users/:id
│   │   │   ├── [id].patch.ts          # PATCH /api/users/:id
│   │   │   ├── [id].delete.ts         # DELETE /api/users/:id
│   │   │   └── [id]/
│   │   │       ├── profile.get.ts     # GET /api/users/:id/profile
│   │   │       └── settings.patch.ts  # PATCH /api/users/:id/settings
│   │   └── me/
│   │       ├── index.get.ts           # GET /api/me (current user)
│   │       ├── profile.patch.ts       # PATCH /api/me/profile
│   │       └── avatar.put.ts          # PUT /api/me/avatar
│   ├── middleware/
│   │   ├── auth.ts
│   │   ├── rbac.ts
│   │   └── validation.ts
│   ├── utils/
│   │   ├── db.ts
│   │   ├── jwt.ts
│   │   ├── validators.ts
│   │   └── responses.ts
│   ├── models/
│   │   ├── User.ts
│   │   └── types.ts
│   └── services/
│       ├── userService.ts
│       └── authService.ts
```

## Naming Conventions

### 1. **File Names**
- Use lowercase with hyphens for multi-word names
- Include HTTP method as suffix: `resource.method.ts`
- Use `[param]` syntax for dynamic routes
- Examples: `users.get.ts`, `[id].patch.ts`, `user-profile.get.ts`

### 2. **API Endpoints**
- **RESTful naming**: Use plural nouns for resources
- **Consistent patterns**:
  - `GET /api/users` - List all users
  - `POST /api/users` - Create user
  - `GET /api/users/:id` - Get specific user
  - `PATCH /api/users/:id` - Update user
  - `DELETE /api/users/:id` - Delete user
  - `GET /api/me` - Get current authenticated user

### 3. **Function Names**
- Use camelCase
- Verb-first for actions: `getUser`, `createUser`, `updateUserProfile`
- Boolean functions: `isAuthenticated`, `hasPermission`, `canAccessResource`

### 4. **Variable Names**
- camelCase for variables: `userId`, `userData`, `isActive`
- PascalCase for types/interfaces: `User`, `UserProfile`, `ApiResponse`
- SCREAMING_SNAKE_CASE for constants: `MAX_LOGIN_ATTEMPTS`, `TOKEN_EXPIRY`

## Code Implementation Examples

### 1. Basic GET Endpoint with Authentication

```typescript
// server/api/users/[id].get.ts
import { defineEventHandler, getRouterParam, createError } from 'h3'
import { getUserById } from '~/server/services/userService'
import { requireAuth } from '~/server/middleware/auth'

export default defineEventHandler(async (event) => {
  // Authenticate request
  const authUser = await requireAuth(event)
  
  // Get route parameter
  const userId = getRouterParam(event, 'id')
  
  if (!userId) {
    throw createError({
      statusCode: 400,
      message: 'User ID is required'
    })
  }
  
  // Check permissions
  if (authUser.id !== userId && !authUser.roles.includes('admin')) {
    throw createError({
      statusCode: 403,
      message: 'Forbidden: You can only access your own data'
    })
  }
  
  // Fetch user data
  const user = await getUserById(userId)
  
  if (!user) {
    throw createError({
      statusCode: 404,
      message: 'User not found'
    })
  }
  
  // Return sanitized user data (remove sensitive fields)
  return {
    id: user.id,
    email: user.email,
    name: user.name,
    createdAt: user.createdAt
  }
})
```

### 2. POST Endpoint with Validation

```typescript
// server/api/users/index.post.ts
import { defineEventHandler, readBody, createError } from 'h3'
import { z } from 'zod'
import { createUser } from '~/server/services/userService'
import { hashPassword } from '~/server/utils/crypto'

// Define validation schema
const createUserSchema = z.object({
  email: z.string().email('Invalid email format'),
  password: z.string().min(8, 'Password must be at least 8 characters'),
  name: z.string().min(2, 'Name must be at least 2 characters'),
  role: z.enum(['user', 'admin']).default('user')
})

export default defineEventHandler(async (event) => {
  // Read request body
  const body = await readBody(event)
  
  // Validate input
  const validation = createUserSchema.safeParse(body)
  
  if (!validation.success) {
    throw createError({
      statusCode: 400,
      message: 'Validation failed',
      data: validation.error.errors
    })
  }
  
  const { email, password, name, role } = validation.data
  
  // Hash password
  const hashedPassword = await hashPassword(password)
  
  // Create user
  try {
    const user = await createUser({
      email,
      password: hashedPassword,
      name,
      role
    })
    
    // Return created user (without password)
    return {
      statusCode: 201,
      data: {
        id: user.id,
        email: user.email,
        name: user.name,
        role: user.role
      }
    }
  } catch (error) {
    if (error.code === 'DUPLICATE_EMAIL') {
      throw createError({
        statusCode: 409,
        message: 'Email already exists'
      })
    }
    throw error
  }
})
```

### 3. PATCH Endpoint for Updates

```typescript
// server/api/users/[id].patch.ts
import { defineEventHandler, getRouterParam, readBody, createError } from 'h3'
import { z } from 'zod'
import { updateUser } from '~/server/services/userService'
import { requireAuth } from '~/server/middleware/auth'

const updateUserSchema = z.object({
  name: z.string().min(2).optional(),
  email: z.string().email().optional(),
  bio: z.string().max(500).optional()
}).refine(data => Object.keys(data).length > 0, {
  message: 'At least one field must be provided'
})

export default defineEventHandler(async (event) => {
  const authUser = await requireAuth(event)
  const userId = getRouterParam(event, 'id')
  const body = await readBody(event)
  
  // Authorization check
  if (authUser.id !== userId && !authUser.roles.includes('admin')) {
    throw createError({
      statusCode: 403,
      message: 'Forbidden'
    })
  }
  
  // Validate
  const validation = updateUserSchema.safeParse(body)
  if (!validation.success) {
    throw createError({
      statusCode: 400,
      data: validation.error.errors
    })
  }
  
  // Update user
  const updatedUser = await updateUser(userId, validation.data)
  
  return {
    statusCode: 200,
    data: updatedUser
  }
})
```

### 4. Authentication Middleware

```typescript
// server/middleware/auth.ts
import { defineEventHandler, createError, getCookie } from 'h3'
import { verifyToken } from '~/server/utils/jwt'

export const requireAuth = async (event) => {
  // Get token from cookie or header
  const token = getCookie(event, 'auth_token') || 
                getHeader(event, 'authorization')?.replace('Bearer ', '')
  
  if (!token) {
    throw createError({
      statusCode: 401,
      message: 'Authentication required'
    })
  }
  
  try {
    const decoded = await verifyToken(token)
    
    // Attach user to event context
    event.context.user = decoded
    
    return decoded
  } catch (error) {
    throw createError({
      statusCode: 401,
      message: 'Invalid or expired token'
    })
  }
}

export const requireRole = (roles: string[]) => {
  return async (event) => {
    const user = await requireAuth(event)
    
    if (!roles.includes(user.role)) {
      throw createError({
        statusCode: 403,
        message: 'Insufficient permissions'
      })
    }
    
    return user
  }
}
```

### 5. User Service Layer

```typescript
// server/services/userService.ts
import { prisma } from '~/server/utils/db'
import type { User, CreateUserInput, UpdateUserInput } from '~/server/models/types'

export const getUserById = async (id: string): Promise<User | null> => {
  return await prisma.user.findUnique({
    where: { id },
    select: {
      id: true,
      email: true,
      name: true,
      role: true,
      createdAt: true,
      updatedAt: true
      // Exclude password
    }
  })
}

export const getUserByEmail = async (email: string): Promise<User | null> => {
  return await prisma.user.findUnique({
    where: { email }
  })
}

export const createUser = async (data: CreateUserInput): Promise<User> => {
  return await prisma.user.create({
    data,
    select: {
      id: true,
      email: true,
      name: true,
      role: true,
      createdAt: true
    }
  })
}

export const updateUser = async (
  id: string, 
  data: UpdateUserInput
): Promise<User> => {
  return await prisma.user.update({
    where: { id },
    data,
    select: {
      id: true,
      email: true,
      name: true,
      bio: true,
      updatedAt: true
    }
  })
}

export const deleteUser = async (id: string): Promise<void> => {
  await prisma.user.delete({
    where: { id }
  })
}
```

### 6. Type Definitions

```typescript
// server/models/types.ts
export interface User {
  id: string
  email: string
  name: string
  role: 'user' | 'admin'
  bio?: string
  createdAt: Date
  updatedAt: Date
}

export interface CreateUserInput {
  email: string
  password: string
  name: string
  role?: 'user' | 'admin'
}

export interface UpdateUserInput {
  email?: string
  name?: string
  bio?: string
}

export interface AuthUser {
  id: string
  email: string
  role: string
  iat: number
  exp: number
}

export interface ApiResponse<T> {
  statusCode: number
  data?: T
  message?: string
  errors?: any[]
}
```

## Best Practices

### 1. **Security**
- Always validate and sanitize user input
- Use parameterized queries to prevent SQL injection
- Implement rate limiting for sensitive endpoints
- Never expose sensitive data (passwords, tokens)
- Use HTTPS in production
- Implement CSRF protection

### 2. **Error Handling**
```typescript
// server/utils/responses.ts
export const handleError = (error: any) => {
  console.error('API Error:', error)
  
  if (error.statusCode) {
    return error
  }
  
  return createError({
    statusCode: 500,
    message: 'Internal server error'
  })
}
```

### 3. **Response Format**
Maintain consistent response structures:
```typescript
// Success
{
  statusCode: 200,
  data: { /* user data */ }
}

// Error
{
  statusCode: 400,
  message: "Validation failed",
  errors: [/* error details */]
}
```

### 4. **Pagination**
```typescript
// server/api/users/index.get.ts
export default defineEventHandler(async (event) => {
  const query = getQuery(event)
  const page = parseInt(query.page as string) || 1
  const limit = parseInt(query.limit as string) || 10
  const skip = (page - 1) * limit
  
  const [users, total] = await Promise.all([
    prisma.user.findMany({ skip, take: limit }),
    prisma.user.count()
  ])
  
  return {
    data: users,
    pagination: {
      page,
      limit,
      total,
      totalPages: Math.ceil(total / limit)
    }
  }
})
```

### 5. **Logging**
```typescript
// Log all API requests
export default defineEventHandler(async (event) => {
  const start = Date.now()
  const method = event.method
  const url = event.path
  
  try {
    const response = await yourHandler(event)
    const duration = Date.now() - start
    console.log(`${method} ${url} - 200 - ${duration}ms`)
    return response
  } catch (error) {
    const duration = Date.now() - start
    console.error(`${method} ${url} - ${error.statusCode} - ${duration}ms`)
    throw error
  }
})
```

## Environment Variables

```env
# .env
DATABASE_URL="postgresql://user:password@localhost:5432/mydb"
JWT_SECRET="your-secret-key"
JWT_EXPIRY="7d"
NODE_ENV="development"
```

## Testing Example

```typescript
// tests/api/users.test.ts
import { describe, it, expect } from 'vitest'
import { setup, $fetch } from '@nuxt/test-utils'

describe('Users API', async () => {
  await setup()
  
  it('should get user by id', async () => {
    const response = await $fetch('/api/users/123', {
      headers: {
        authorization: 'Bearer valid-token'
      }
    })
    
    expect(response).toHaveProperty('id')
    expect(response).toHaveProperty('email')
  })
})
```

## Summary

This structure provides:
- ✅ Clear separation of concerns
- ✅ Type safety with TypeScript
- ✅ Consistent naming conventions
- ✅ Reusable middleware and utilities
- ✅ Proper authentication and authorization
- ✅ Input validation
- ✅ Error handling
- ✅ Scalable architecture

Adapt these patterns to your specific project needs and data models.
