# Unity Entities API - SystemState

## What's For

- Context for DOT programming
- System create by implementing `ISystem`, need access current `SystemState` by ref parameters of methods `OnCreate(ref SystemState)`, `OnUpdate(ref SystemState)`, and `OnDestroy(ref SystemState)`

## Properties

- [EntityManager](unity-entities-api-entitymanager.md): access to entity manager
- [World](unity-entities.md#world)
  - References the current ECS world the current system belongs to.
  - One system can access to one world at a time.
- Enabled
- [Dependency](unity-entities-system.md#system-dependency): 
  - A [`JobHandle`](unity-jobs-jobhandle.md) Tracking the dependencies before [system]() perform logic.
  - Used to ensure that the system runs after the jobs it depends on have completed.
- Time
- LastSystemVersion
- SystemHandle

## Methods

`CreateEntityQuery`

`RequireForUpdate<T>()`

- Require component type `T` exist for system to update
