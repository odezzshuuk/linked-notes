# Unity Entities - Dynamic Buffer Component

## Dynamic Buffer Intruduction

What it is

- While IComponentData is for fixed-size data, Dynamic Buffer Component can manage a resizeable array of unmanaged data

Features

- [Structural Changes](unity-entities-structural-changes.md) are might move the **referenced** array
- Which means that any handle to dynamic bufer becomes invalid after a structural changes

```cs
public void DynamicBufferExample(Entity e) {
    DynamicBuffer<int> buffer = EntityManager.GetBuffer<int>(e);
    // structural changes happened here.
    EntityManager.CreateEntity();

    // throw an exception
    // var x = buffer[0]; 

    // Assigning again to the buffer after structural changes
    buffer = EntityManager.GetBuffer<int>(e);
}
```

Comparing to [Native Container In Component](unity-entities-component.md#restrictions-of-native-container-in-component)

- Dynamic buffers don't have the restriction on using job scheduling
- So use dynamic buffers as much as possible

## Create Dynamic Buffer Component

- Inherit from `IBufferElementData`
- Use `InternalBufferCapacity` attribute to specify the initial capacity of the buffer

```cs
[InternalBufferCapacity(10)]
public struct ExampleBufferComponent : IBufferElementData
{
    public int Value;
}
```

## Get Dynamic Buffer Component

- `DynamicBuffer<T>` represents a dynamic buffer component even though it has no "Component" in its name
- Use dynamic buffer corresponding api, such as `EntityManager.GetBuffer<T>()` or `SystemAPI.GetBuffer<T>()`

```cs
DynamicBuffer<ExampleBufferComnponent> exampleDynamicBuffer = EntityManager.GetBuffer<ExampleBufferComponent>(entity);
```

## Add Dynamic Buffer Component

- `IBaker.AddBuffer<T>()`

```cs
public class ExampleBaker : Baker<ExampleAuthoring>
{
    public override void Bake(ExampleAuthoring authoring)
    {
        var entity = GetEntity(TransformUsageFlags.Dynamic);
        AddBuffer<ExampleBufferComponent>(entity);
        
        // Add elements to the buffer
        DynamicBuffer<ExampleBufferComponent> buffer = GetBuffer<ExampleBufferComponent>(entity);
        for (int i = 0; i < 5; i++)
        {
            buffer.Add(new ExampleBufferComponent { Value = i });
        }
    }
} 
```

