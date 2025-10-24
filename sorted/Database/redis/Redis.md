# Redis

- It is a Key-Value database.
- Data types:
  - String
  - Hash
  - List
  - Set and Sorted Set

## Installation

[Windows download link](https://github.com/poradowski/redis/releases)

Check redis version

```bash
redis-server --version
```

## Startup

Start client

```bash
redis-cli
```

Start server

```bash
redis-server
```

## Client operations

- exit: exit redis client
- shutdown: shut down redis server

Key operations

- set key value: set the value of key to value
- del key: delete key
- exists key: check if key exists
- keys *: get all keys
- keys key: check if key exists
- expire key seconds: set expiration time for key

Value retrieval

- get key: get value of **String** type
- hgetall key: get value of **Hash** type
- lrange key start end: get value of **List** type
- smembers key: get value of **Set** type

## Redis Indexing

- Forward index: 0 indicates the first element, 1 the second, and so on
- Reverse index: -1 indicates the last element, -2 the second last, etc.

## Redis key naming best practices

> Naming convention

- Store object properties: `object:id:subobjects`

```
user:1:roles
user:john:roles
```

Use namespace: `namespace:object:id:subobjects`

- Suitable for **multiple application development**

```
tenant:user:1:roles
```

- List

## Suitable scenarios for redis

- Frequently accessed data
- Infrequently modified data
- Data with low consistency requirements

## Redis usage guidelines

- Although redis can store set-type values, generally do not store sets, because redis will store all kinds of subsets of the set

## Redis principle

[Redis principle](redis-principle.md)

