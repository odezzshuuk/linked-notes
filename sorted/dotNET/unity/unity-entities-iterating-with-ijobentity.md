# Unity Entities Programming - Iterating With IJobEntity 

## What's For

- With `IJobEntity`, you can use it in multiple systems
- `IJobEntity` iterating mechanism is similar to [`IJobFor`](unity-jobs-parallel-jobs#how-to)
  - but replace `Execute(int index)` with method like `Execute(ref TComponent component, in TReadOnlyComponent readOnlyComponent)`
  - So don't need write for loop to iterate
- It create an `IJobChunk` job

## How to

- Implement `IJobEntity` interface
- Implement `Execute()` method

> partial keyword is required

```cs
public partial struct ExampleJob : IJobEntity
{
    [ReadOnly] public float deltaTime;
    [ReadOnly] public float speed;
    [ReadOnly] public float distance;

    public void Execute(ref LocalTransform transform, in RotationSpeed rotationSpeed)
    {
        transform = transform.RotateY(rotationSpeed.RadiansPerSecond * deltaTime);
    }
}
```

- When `ExampleJob` is scheduled, it will perform the rotation on all entities that have `LocalTransform` and `RotationSpeed` components.
- keyword `ref` marked `LocalTransform` data as read-write, keyword `in` marked `RotationSpeed` data as read-only.

Rewrite `SystemAPI.Query<>()` with `IJobEntity`

- `SystemAPI.Query<>()` code

```cs
public partial struct MyRotationSpeedSystem : ISystem
{
    public void OnUpdate(ref SystemState state)
    {
        float deltaTime = SystemAPI.Time.DeltaTime;

        foreach (var (transform, speed) in SystemAPI.Query<RefRW<LocalTransform>, RefRO<RotationSpeed>>())
            transform.ValueRW = transform.ValueRO.RotateY(speed.ValueRO.RadiansPerSecond * deltaTime);
    }
}
```

- `IJobEntity` code

```cs
public partial struct ExampleJob : IJobEntity
{
    [ReadOnly] public float deltaTime;
    public void Execute(ref LocalTransform transform, in RotationSpeed rotationSpeed)
    {
        transform = transform.RotateY(rotationSpeed.RadiansPerSecond * SystemAPI.Time.DeltaTime);
    }
    
}
public partial class ExampleSystem : SystemBase
{
    protected override void OnUpdate()
    {
        var job = new ExampleJob
        {
            deltaTime = SystemAPI.Time.DeltaTime
        };
        job.ScheduleParallel();
    }
}
```


## `Execute` Parameters

- IComponentData: Mark `ref` for read-write access, `in` for read-only access
- ICleanupComponentData	
- ISharedComponent	
- Managed components
- Entity	
- `DynamicBuffer<T>`
- IAspect
- int: what's in represent is based int type parameter attribute
  - `[ChunkIndexInQuery]`
  - `[EntityIndexInChunk]`
  - `[EntityIndexInQuery]`


## Narrow the query

there are 2 ways to query

- Pass a [query](unity-entities-api-entityquery.md) object when schedule the job
- Use attribute set on the job struct

Pass query object

```cs
public partial struct QueryJob : IJobEntity
{
    public void Execute(ref ExampleComponent exampleComponent)
    {
        exampleComponent.Value += 1;
    }
}
public partial class ExampleSystem : SystemBase
{
    protected override void OnCreate()
    {
        // Create a query that selects entities with ExampleComponent
        var query = GetEntityQuery(ComponentType.ReadWrite<ExampleComponent>());

    }
    protected override void OnUpdate()
    {
        var job = new QueryJob();
        job.ScheduleParallel(query);
    }
} 
```

Attributes

- set on the job struct
  - `[WithAll]`
  - `[WithAny]`
  - `[WithNone]`
  - `[WithChangeFilter]`
  - `[WithOptions]`
- set on int parameter in `Execute` method
  - `[EntityIndexInQuery]`



