# RBAC

- **RBAC**: Role-Based Access Control
- A widely used **database model** for **permission design**
- Logical separation between users and permissions, with two many-to-many relationships:
  - A user can assume multiple roles
  - Different roles can have different permissions

## Database Design

Three main tables: **User**, **Role**, and **Permission**

- **user**: User table
  - `id`: User ID
  - `name`: Username
  - `password`: Password
- **role**: Role table
  - `id`: Role ID
  - `role_id`: Role ID
  - `user_id`: User ID
- **permission**: Permission table
  - `id`: Permission ID
  - `name`: Permission name
  - `value`: Permission value (usually a URL-like resource identifier)
  - `sort`: Custom sorting for permissions

Two association tables: **User-Role** and **Role-Permission**

- **user_role**: User-Role association table
  - `id`: Association ID
  - `user_id`: User ID
  - `role_id`: Role ID

> `user_id` and `role_id` have a many-to-many relationship

- **role_permission**: Role-Permission association table
  - `id`: Association ID
  - `role_id`: Role ID
  - `permission_id`: Permission ID

> `role_id` and `permission_id` have a many-to-many relationship

## Logic

### Adding a User

- Add the user while also updating the user-role association table
- No need to modify permission-related tables

```sql
INSERT INTO user (name, password) VALUES ('admin', '123456');
```

```sql
INSERT INTO user_role (user_id, role_id) VALUES (user_id, role_id);
```
