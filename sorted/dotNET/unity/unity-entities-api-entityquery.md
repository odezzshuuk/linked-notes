# Unity Entities API - EntityQuery

* [How to get EntityQuery instance](#how-to-get-entityquery-instance)
* [Query Method](#query-method)
* [EntityQuery Filters](#entityquery-filters)
* [Execute Query](#execute-query)
* [Shared Component Filter](#shared-component-filter)
* [Value Change Filter](#value-change-filter)
* [Enableable Filter](#enableable-filter)

## How To Get EntityQuery Instance

1. Build by `EntityQueryBuilder` tool to create `EntityQuery` instance

```cs
EntityQuery query = new EntityQueryBuilder(Allocator.Temp)
    .WithAllRW<ObjectRotation>()
    .WithAll<>(ObjectRotationSpeed)
    .Build(this);
```

2. [`EntityQuery SystemState.GetEntityQuery()`](unity-entities-api-systemstate.md#methods)

- `GetEntityQuery(ComponentType)`
  - Take a [`ComponentType`](unity-entities-api-componenttype.md) as parameter
- `GetEntityQuery(NativeArray<ComponentType>)`
- `GetEntityQuery(params EntityQueryDesc[]) `
- `GetEntityQuery(in EntityQueryBuilder)`

3. Build from [SystemAPI.QueryBuilder](unity-entities-api-systemapi.md#systemapi.querybuilder)

```cs
SystemAPI.QueryBuilder().WithAll<Score>().Build();
```

## Query Method

`Withxxx` methods to specify which [archetypes](unity-entities-archetype.md) to select

- `WithAll<T>()`: All Filtered out [archetypes](unity-entities-archetype.md) must contain type `T` component, and must **ENABLED**
- `WithAny<T>()`: **At Least One** of the filtered [archetypes]() must contain type `T` component
- `WithNone<T>()`: Filtered out [archetypes](unity-entities-archetype.md) must not contain or **DISABLED** type `T` component
- `WithAbsent<T>()`: Filtered out [archetypes](unity-entities-archetype.md) must not contain type `T` component
- `WithPresent<T>()`: Filtered out [archetypes](unity-entities-archetype.md) must contain type `T` component, NO MATTER if it is enabled or disabled

## EntityQuery Filters

- [Shared Component Filter](#shared-component-filter)
- [Value Change Filter](#value-change-filter)

## Execute Query

- `ToEntityArray`: Returns an array of [Entity](unity-entities-api-entity.md) instances
- `ToComponentDataArray<T>`: Returns an array of **component data** of type `T`
- `CreateArchetypeChunkArray`:
  - Returns all the chunks that contain the selected entities. Because a query operates on archetypes, shared component values, and change filters, which are all identical for all the entities in a chunk, the set of entities stored in the returned set of chunks is the same as the set of entities ToEntityArray returns.

## Shared Component Filter

> [Shared Component](unity-entities-component.md#shared-component)

- Use `SetSharedComponentFilter`

```cs
struct SharedGrouping : ISharedComponentData
{
    public int Group;
}

[RequireMatchingQueriesForUpdate]
partial class ImpulseSystem : SystemBase
{
    EntityQuery query;

    protected override void OnCreate()
    {
        query = new EntityQueryBuilder(Allocator.Temp)
            .WithAllRW<ObjectPosition>()
            .WithAll<Displacement, SharedGrouping>()
            .Build(this);
    }

    protected override void OnUpdate()
    {
        // By default (without a filter), count all entities that have the required components.
        query.ResetFilter();
        int unfilteredCount = query.CalculateEntityCount();
        // With a filter, only entities in chunks that have SharedGrouping=1 will be counted.
        query.SetSharedComponentFilter(new SharedGrouping { Group = 1 });
        int filteredCount = query.CalculateEntityCount();
        // Many query methods include a variant that ignores any active filters. These variants are generally
        // more efficient, and should be used when conservative upper-bound results are acceptable.
        int ignoreFilterCount = query.CalculateEntityCountWithoutFiltering();
    }
}
```

- only entities in chunks that have `SharedGrouping=1` will be counted

## Value Change Filter

```cs
public class ExampleSystem : SystemBase
{
    EntityQuery query;

    protected override void OnCreate()
    {
        query = new EntityQueryBuilder(Allocator.Temp)
            .WithAllRW<LocalToWorld>()
            .WithAll<ObjectPosition>()
            .Build(this);
        // Set the filter to only include entities where the Displacement value has changed
        query.SetChangedVersionFilter<ObjectPosition>();
    }
}
```

- This query will include entities where the `ObjectPosition` component has changed since the last time the query was updated
- The change filter also only checks write access to the component, that's why write/read access of component matters

## Enableable Filter

