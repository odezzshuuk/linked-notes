# Unity Entities - System

## What's For

- Perform logic on component data
- Mainly for providing an efficient alternative to the traditional `MonoBehaviour.Update()`

## Features

- Do not declare public methods in a system for external code to call

```cs
public partial class MovementSystem : SystemBase {
    // this is bad practice
    protected void Create()
    {
        // Do not declare public methods here
    }
}
```

## System types

- [ISystem]()
- [SystemBase]()
- EntityCommandBufferSystem: allows group [structural changes]()
- ComponentSystemGroup

## ISystem

- Used to create [unmanaged]() system
- Must implement method
  - `OnCreate(ref SystemState)`
  - `OnDestroy(ref SystemState)`
  - `OnUpdate(ref SystemState)`

> Details about [SystemState](unity-entities-api-systemstate.md)

## SystemBase

- Used to create [managed]() system

```cs
public partical class MovementSystem : SystemBase {
    protected override void OnUpdate(ref SystemState state)
    {
        Entities.ForEach((ref Translation translation, in Velocity velocity) =>
        {
            translation.Value += velocity.Value * Time.DeltaTime;
        }).Schedule();
    }
}
```

## Comparison

| Feature                                         | ISystem compatibility | SystemBase compatibility |
| :---------------------------------------------- | :-------------------: | :----------------------: |
| Burst compile OnCreate, OnUpdate, and OnDestroy |          Yes          |            No            |
| Unmanaged memory allocated                      |          Yes          |            No            |
| GC allocated                                    |          No           |           Yes            |
| Can store managed data directly in system type  |          No           |           Yes            |
| [SystemAPI.Query]()                             |          Yes          |           Yes            |
| [Entities.ForEach]()                            |          No           |           Yes            |
| Job.WithCode                                    |          No           |           Yes            |
| IJobEntity                                      |          Yes          |           Yes            |
| IJobChunk                                       |          Yes          |           Yes            |
| Supports inheritance                            |          No           |           Yes            |

When ISystem

- Faster
- Value-based
- Unsupport [managed types](csharp-types.md#referece-types-managed-types)
- support [burst]() compile

When SystemBase

- No [Burst]() compile needed
- Want to use `Entities.ForEach()`
- Interacting with Monobehaviour

## System Groups

- More about [SystemGroup](unity-entities-systemgroup.md)

## System Dependency

[System Dependency](unity-entities-system-dependency.md)

## WorldSystemFilterAttribute

- Define where internal unity systems should be create

`WorldSystemFilterFlags`

- All
- BakingSystem
- ClientSimulation
- ServerSimulation
- Streaming
- ...

