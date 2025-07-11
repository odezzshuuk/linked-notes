# Unity Entites - EntityManager

## What's For

- Useful for managing [structural changes](unity-entities-structural-changes.md)

## Features

- Some APIs can cause [structural changes](unity-entities-structural-changes.md)
- When structural changes performed, 
  - `EntityManager` wait for all jobs to complete
  - This will create a [sync point(wait operation)](csharp-task#wait-a-task)
  - Which can cause performance issues
- Can't work with [jobs](unity-jobs.md)
- Only methods `CreateEntity()`, `Instantiate()`, `CreateArchetype()` allowed in [`SystemAPI.Query()`](unity-entities-api-systemapi)
- Do not pass temporary entity to `EntityManager` methods,

## How To Reach It

[`SystemBase.EntityManager`](unity-entities-system.md#systembase)

```cs
public partial class MySystem : SystemBase
{
    protected override void OnCreate()
    {
        EntityManager.AddComponentData(entity, componentData)
    }
}
```

[`SystemState.EntityManager`](unity-entities-api-systemstate.md)

```cs
public partial struct MySystem : ISystem
{
    public void OnCreate(ref SystemState state)
    {
        state.EntityManager.AddComponentData(entity, componentData);
    }
}
```

`world.EntityManager`

- About [how to get world reference](unity-entities-world#how-to-reach-it)

```cs
public partial struct MySystem : ISystem
{
    public void OnCreate(ref SystemState state)
    {
        EntityManager entityManager = World.DefaultGameObjectInjectionWorld.EntityManager;
        entityManager.AddComponentData(entity, componentData);
    }
}
```

## Method

`CreateEntity()`

`Instantiate()`

`DestroyEntity()`

`AddComponent()`

`RemoveComponent()`

`GetComponentData()`

