# Unity Entities - SystemGroup

- Can contains systems and other system groups

## Default SystemGroup

- `InitializationSystemGroup`, `SimulationSystemGroup`, `PresentationSystemGroup`

## Create a SystemGroup

- To create SystemGroup, create a class inheriting from `ComponentSystemGroup`

```cs
public class CustomSystemGroup : ComponentSystemGroup
{
    protected override void OnCreate()
    {
        base.OnCreate();
        // Add systems to this group
        AddSystemToUpdateList(World.GetOrCreateSystem<SomeSystem>());
    }
}
```

## Manage SystemGroup

- Use `UpdateInGroup` attribute to add a system to a specific SystemGroup
- Use `UpdateBefore` and `UpdateAfter` attributes to control the execution order of systems

```cs
[UpdateInGroup(typeof(CustomSystemGroup))]
[UpdateBefore(typeof(AnotherSystem))]
public class ExampleSystem : SystemBase { }

public class AnotherSystem : SystemBase { }
```

- `ExampleSystem` will run before `AnotherSystem` in the `CustomSystemGroup`.


