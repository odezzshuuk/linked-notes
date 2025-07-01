# Unity Entities - Aspect

## What's Aspect

- An object-like wrapper that used to group together a subset of an entity's components into a single C# struct
- Although it looks like a normal struct, but `IAspect` interface is necessary

## Declare An Aspect

- Implement `IAspect`
- keyword `readonly` is necessary

```cs
using Unity.Entities;

public readonly partial struct MyAspect : IAspect {
    public readonly RefRW<LocalTransform> _transform;
}
```

## Aspect Can Include

- A single `Entity` field to store entity's ID
- `RefRW<T>` and `RefRO<T>` fields to access components
- `EnabledRefRW` and `EnabledRefRO` to access enabled state of componnets that implement `IEnableableComponent`
- `DynamicBuffer<T>` to access buffer elements that implement `IBufferElementData`
- Any [`ISharedComponent`](unity-entities-component#shared-component) field to access the shared component value as read-only
- Any `IAspect` field to access another aspect

## Source Generation

- During compilation, Unity generates methods additional methods for aspects

## Take A Look

- A component `CannonBall`
- An aspect `CannonBallAspect`

```cs
struct Score : IComponentData { public float Value; }
struct CannonBall : IComponentData { public float3 Speed; }

// Aspects must be declared as a readonly partial struct
readonly partial struct CannonBallAspect : IAspect
{
    // An Entity field in an Aspect gives access to the Entity itself.
    // This is required for registering commands in an EntityCommandBuffer for example.
    public readonly Entity Self;

    // Aspects can contain other aspects.

    // A RefRW field provides read write access to a component. If the aspect is taken as an "in"
    // parameter, the field behaves as if it was a RefRO and throws exceptions on write attempts.
    readonly RefRW<LocalTransform> _transform;
    readonly RefRW<CannonBall> _cannonBall;

    readonly RefRO<Score> _score

    // Properties like this aren't mandatory. The Transform field can be public instead.
    // But they improve readability by avoiding chains of "aspect.aspect.aspect.component.value.value".
    public float Score => _score.ValueRO.Value;
    public float3 Position
    {
        get => _transform.ValueRO.Position;
        set => _transform.ValueRW.Position = value;
    }

    public float3 Speed
    {
        get => _cannonBall.ValueRO.Speed;
        set => _cannonBall.ValueRW.Speed = value;
    }
}
```


