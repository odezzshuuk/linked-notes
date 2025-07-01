# Unity Entities - Iterating Entities and Components

* [Where Iterating Happens](#where-iterating-happens)
* [How to Iterating with SystemAPI.Query](#how-to-iterating-with-systemapi.query)
* [Iterating with Entities.ForEach](#iterating-with-entities.foreach)
* [With IJobEntity](#with-ijobentity)

## Where Iterating Happens

- Iterating is a common task when create a [system](unity-entities-system.md).

## Why Iterating

- Unlike MonoBehaviour that component data is stored in the object
- In ECS, component data is stored together, which need iterating to update

## How to Iterating with SystemAPI.Query

- Iterate in main thread
- Using `foreach statement` to iterate `SystemAPI.Query<>()` results.

```cs
public partial struct MyRotationSpeedSystem : ISystem
{

    [BurstCompile]
    public void OnUpdate(ref SystemState state)
    {
        float deltaTime = SystemAPI.Time.DeltaTime;

        foreach (var (transform, speed) in SystemAPI.Query<RefRW<LocalTransform>, RefRO<RotationSpeed>>())
            transform.ValueRW = transform.ValueRO.RotateY(speed.ValueRO.RadiansPerSecond * deltaTime);
    }
}
```

- `SystemAPI.Query<RefRW<LocalTransform>, RefRO<RotationSpeed>>()` is used to query entities with `LocalTransform` and `RotationSpeed` components.

## Iterating with Entities.ForEach

- `Entities.ForEach()` static method to iterate

```cs
public partial class ExampleSystem : SystemBase
{
    protected override void OnUpdate(ref SystemState state)
    {
        float deltaTime = SystemAPI.Time.DeltaTime;

        Entities.ForEach((ref LocalTransform transform, in RotationSpeed speed) =>
        {
            transform = transform.RotateY(speed.RadiansPerSecond * deltaTime);
        }).Schedule();
    }
}
```

## With IJobEntity

[IJobEntity](unity-entities-iterating-with-ijobentity.md)

