# Unity Entities Programming - Query Entities 

## What's Query

- Query is a way to select entities based on their [components](unity-entities-component.md)

## 2 Ways to Query Entities

1. [`SystemAPI.Query()`](#systemapi-query)
2. `EntityQuery` instance

## Filters

Entities can be query by filter. A filter can be the combination of those points:

- Basic query that Both `SystemAPI.Query<T>()` and `EntityQuery` can do
  - [Component](unity-entities-component.md) type
  - Component data accessibility(read/write)
  - Enable/disable state
- Additional query that only `EntityQuery` can do
  - Query [Shared Component](unity-entities-component.md#shared-component)
  - Whether the component value changed

## SystemAPI Query

[SystemAPI.Query<T>()](unity-entities-api-systemapi-query.md)

## Query with EntityQuery 

[EntityQuery](unity-entities-api-entityquery.md)

