# Web - API Design - RESTful API

## What It Is

- REST: **Re**presentational **S**tate **T**ransfer

## Features

- stateless
 - client request must contain all information necessary to respond to a request
 - server does not store any information about client
- client-server are independently
- Cacheable
- Uniform interface
- transform data using JSON

## When To Use

- Public API
- Mobile backend
- Microservices with broad compatibility

## Http Method Semantics

- `GET` for Read
- `POST` for create
- `PATCH` for update
- `DELETE` for remove

## Representation of Status Code

- `200` for success

## Name Convention

url resource name should be a noun, not a verb

- which means use `/products` not `/getProducts`
- `/products` for collections
- `/products?name=foo` for filtering

Pagination

```
/products?limit=20&offset=5
```

## Principles

1. Nouns for resources

- ✅ `GET /users`
- ✅ `GET /users/123`

2. Semantically use HTTP methods
3. Hierachical structure for nested resources

- ✅ `GET /users/123/orders`
- ✅ `GET /users/123/orders/456`
- ⚠️ `GET /users/123/orders/456/items`(usually stop at 2 levels)
- ❌ `GET /getUserOrders?userId=123`

4. Return proper HTTP status code

> [HTTP status code here](http-response-message.md#status-line)

5. Use json
6. Support Filtering, Sorting, Pagination, Searching

- Filtering: `/products?category=electronics&price_lt=1000`
- Sorting: `/products?sort=price_asc`
- Pagination: `/products?limit=20&offset=40`
- Searching: `/products?search=smartphone`

7. Versioning
8. Error Handling

- Return meaningful error messages
- Limit exposure of internal details, for example error stack trace

9. HATEOAterS
10. Authentication & Authorization

- Authentication: Have one's identity verified
  - For example JWT, OAuth
- Authorization: verify user permission to access resource

11. Rate Limiting

- return rate-limit headers

```sh
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 200
X-RateLimit-Reset: 1618886400
```

12. Documentation


