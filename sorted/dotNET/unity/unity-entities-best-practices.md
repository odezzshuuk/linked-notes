# Unity Entities - Best Practices

## Create Entities In Editor

1. Create GameObject in [subscene](unity-entities-subscene.md)
2. Write [Baker](unity-entities-baking.md)

```cs
public class ExampleAuthoring : MonoBehaviour {
    public int exampleValue;
}
public class ExampleBaker : Baker<ExampleAuthoring> {
    public override void Bake(ExampleAuthoring authoring) {
        // Create an entity
        var entity = GetEntity(TransformUsageFlags.Dynamic);
        
        // Add component data to the entity
        AddComponent(entity, new ExampleComponent { exampleValue = authoring.exampleValue });
    }
}
```

3. Add component to the GameObject
4. System to update the entity

```cs
public partial class ExampleSystem : SystemBase {
    protected override void OnUpdate() {
        Entities.ForEach((ref ExampleComponent exampleComponent) => {
            // Update the component
            exampleComponent.exampleValue++;
        }).Schedule();
    }
}
```

## Create Entity Spawner

- Entities can only create in main thread

1. Create empty GameObject as spawner in [subscene](unity-entities-subscene.md)
2. Write [Baker](unity-entities-baking.md) to create entity when the scene is loaded

```cs
public class SpawnerAuthoring : MonoBehaviour {
    public GameObject prefab;
}

public struct SpawnerData : IComponentData {
    public Entity prefab;
}

public Class SpawnerBaker : Baker<SpawnerAuthoring> {
    public override void Bake(SpawnerAuthoring authoring) {
        // Create an entity for the spawner
        var entity = GetEntity(TransformUsageFlags.Dynamic);
        
        // Assign authring prefab to the component data
        // Add component data to the entity
        AddComponent(entity, new SpawnerData 
        { 
            prefab = GetEntity(authoring.prefab) 
        });
    }
}
```

3. same as [Create entities in editor](#create-entities-in-editor)
4. write system

```cs
public partial struct SpawnerSystem : ISystem {
    public void OnCreate(ref SystemState state) {
        foreach (RefRW<SpawnerData> spawner in SystemAPI.Query<RefRW<SpawnerData>>()) {
            // Create an entity from the prefab
            Entity entity = state.EntityManager.Instantiate(spawner.ValueRO.prefab);
            
            // Optionally, set the position or other properties of the entity
            state.EntityManager.SetComponentData(entity, LocalTransform.FromPosition(new float3(0, 0, 0)));
        }
    }
}
```


## Create Entities In MonoBehaviour Code

> [Authoring](unity-entities-authoring.md)


## Add Component In Editor

## Add Component In Code

