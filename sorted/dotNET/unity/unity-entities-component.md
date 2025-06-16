# Unity Entites - Component

## What's it

- Where data is stored

Features

- Can contain method, but not recommended, pure data is best practice

## Component Types

- [unmanaged component](#unmanaged-component)
- [managed component](#managed-component)
- [shared component](#shared-component)

## Unmanaged component

Declaration

```cs
public struct MyComponent : IComponentData
{
    public int myValue;
}
```

Features

- Can only contain [unmanaged data](csharp-types.md#unmanaged-types)

## Managed component

Declaration

```cs
public class MyComponent : IComponentData
{
    public int myValue;
}
```

Features

- Can't use [jobs]() and [burst compiler](unity-burst.md)
- Must include a constructor with no paramaters for serailization purposes

Manage Reference with `ICloneable` and `IDisposable`

```cs
public class ManagedComponentWithExternalResource : IComponentData, IDisposable, ICloneable
{
    public ParticleSystem particleSystem;

    public void Dispose()
    {
        UnityEngine.Object.Destroy(particleSystem);
    }

    public object Clone()
    {
        return new ManagedComponentWithExternalResource { particleSystem = UnityEngine.Object.Instantiate(ParticleSystem) };
    }
}
```

- with `ICloneable`, when 2 entities have this component, each entity will have its own instance of the `ParticleSystem`
- without `IDisposable`, if the component is destroyed, the `ParticleSystem` will keep
- So use `IDisposable` to destroy `ParticleSystem` when the component is destroyed

## Shared component

What it is

- Unity stores all entities in the same [archetype]() that have the same shared component values together

Features

- Can be [unmanaged component](#unmanaged-component) or [managed component](#managed-component)
- An array stores each different values of shared component
- This array is seperated from [chunks](unity-entities-archetype.md#archetypes-chunk)
- Chunks store handles(index/pointer) to locate the shared component values

when an entity shared component value changed

- If this value already exists, move the entity to a chunk that stores the handle of the existing value
- Otherwise, adds the new value to the shared component values array, and move the entity to a chunk that stores the handles of the new value

Create Shared Component

- Inherit from `ISharedComponentData`

```cs
public struct ExampleUnmanagedSharedComponent : ISharedComponentData
{
    public int Value;
}
```



