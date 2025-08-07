# Unity Entities Programming - Organizing System Data

* [Why](#why)
* [How To Organize?](#how-to-organize?)
* [Which Component To Store?](#which-component-to-store?)
* [How To Get `SystemHandle`?](#how-to-get-`systemhandle`?)

## Why 

- It's bad practice to declare public fields in a system type, which lead to following consequences:
  - Creating dependencies between systems, which not respect data-oriented design
  - Can't guarantee thread or lifetime safety

## SystemHandle

Struct `SystemHandle` is a

- system-associated type
- entity-like, but not an actual entity
- [singleton](unity-entities-component#singleton-component)-like with differences
  - Singletons aren't tied to the system's lifetime
  - Singletons can only exist per system type, not per system instance

## How To Organize?

- When need to store data in a system type, create a exclusive component type for the system on purpose
- Add then add the that component to [`SystemHandle`](#systemhandle)
- Then set data in that component
- Rather than storing as fields in system type

## How To Get `SystemHandle`?

1. `SystemHandle world.GetExistingSystem<T>()` where `T` is the system type

- Comparing to [`T world.GetExistingSystemManaged<T>()`](unity-entities-communication-with-monobehaviour#access-system-from-monobehaviour) which return the instance of type T system

2. `SystemHandle SystemBase.SystemHandle` property
3. `SystemHandle SystemState.SystemHandle` property which work with [`ISystem`](unity-entities-system#isystem)

## How To Store Data In `SystemHandle`?

2 Steps:

1. Add Component to `SystemHandle`:
2. Set data in that component

```cs
public struct ExampleComponent : IComponentData {
    public int Value;
}
public partial struct ExampleSystem : ISystem {

    public void OnCreate(ref SystemState state) {
        // Add component to SystemHandle
        state.EntityManager.AddComponent<ExampleComponent>(state.SystemHandle, new ExampleComponent());
        // Set data in that component
        state.SetComponent(state.SystemHandle, new ExampleComponent { Value = 42 });
    }
}
```

## How To Get Data From `SystemHandle`?



