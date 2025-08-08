# Unity Entites - Component

* [What's it](#what's-it)
* [Features](#features)
* [What Should Do In Component](#what-should-do-in-component)
* [Component Types](#component-types)
* [Unmanaged component](#unmanaged-component)
* [Managed component](#managed-component)
* [Shared component](#shared-component)
* [Singleton Component](#singleton-component)
* [Dynamic Buffer Component](#dynamic-buffer-component)
* [Enable/Disable Of Component](#enable/disable-of-component)

## What's it

- Where data is stored

## Features

- Can contain method, but not recommended, pure data is best practice

## What Should Do In Component

## Component Types

- [unmanaged component](#unmanaged-component)
- [managed component](#managed-component)
- [shared component](#shared-component)
- [Singleton component](#singleton-component)
- [Dynamic Buffer component](#dynamic-buffer-component)

## Unmanaged component

Declaration

- keyword `struct`

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

- keyword `class`

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

## Singleton Component

What It Is

- A component that only one [entity](unity-entities-entity) in **a [world](unity-entities-world)** can have

Features

- If a singleton component is added to another entity, then it's no longer a singleton component

How To Determine A Singleton Component

- When use singleton APIs on a component with more than one instance, it will throw an **exception**

How To Access Singleton Component

- Use singleton APIs
  - `EntityManager.CreateSingleton()`
  - `SystemAPI.GetSingletonEntity()`
  - `SystemAPI.GetSingleton()`
  - `SystemAPI.SetSingleton()`

## Dynamic Buffer Component

[Dynamic Buffer Component](unity-entities-dynamic-buffer-component.md)

## Restrictions Of Native Container In Component

- When components have [Native Container](unity-jobs-nativecontainer.md), 
- Scheduling jobs with [IJobEntity](unity-entities-iterating-with-ijobentity) And [IJobChunk](unity-entities-query-with-ijobchunk) against those component is not allowed
- But you can schedule the job against container it self on main thread

## Enable/Disable Of Component


