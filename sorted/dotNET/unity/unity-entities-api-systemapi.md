# Unity Entities API - SystemAPI

* [What's This](#what's-this)
* [Practical Usage](#practical-usage)
* [SystemAPI.Query](#systemapi.query)
* [SystemAPI.QueryBuilder](#systemapi.querybuilder)

## What's This

- A class that provides caching and utility methods for accessing data in an entity's world

## Practical Usage

1. Iterate through data
2. Query building: 
3. Access data
4. Access [singletons]

## Access Data

Access [Component](unity-entities-component.md)

- `GetComponentLookup`
- `GetComponent`
- `SetComponent`
- `HasComponent`
- `IsComponentEnabled`
- `SetComponentEnabled`

Access [Buffers]()

- `GetBufferLookup`
- `GetBuffer`
- `HasBuffer`
- `IsBufferEnabled`
- `SetBufferEnabled`

EntityInfo

- `GetEntityStorageInfoLookup`
- `Exists`

[Aspects](unity-entities-aspect.md)

- `GetAspect`

[Handles]()	

- `GetEntityTypeHandle`
- `GetComponentTypeHandle`
- `GetBufferTypeHandle`
- `GetSharedComponentTypeHandle`

## Managed API To Handle Managed Components 

> Here is [Managed Components](unity-entities-component.md#managed-component)

- SystemAPI Managed API was in `SystemAPI.ManagedAPI` namespace

```cs
foreach (var transformRef in SystemAPI.Query<SystemAPI.ManagedAPI.UnityEngineComponent<Transform>>()) {
    transformRef.Value.Translate(0,1,0);
}
```

## SystemAPI.Query

[SystemAPI.Query](unity-entities-api-systemapi-query.md)

## SystemAPI.QueryBuilder


