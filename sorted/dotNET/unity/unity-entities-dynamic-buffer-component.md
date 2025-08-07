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

Comparing to [Native Container](unity-jobs-nativecontainer.md)

