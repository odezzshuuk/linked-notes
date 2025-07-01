# Unity Entities - Best Practices

## Create Entities In Editor

1. Create GameObjects in [subscene](unity-entities-subscene.md)
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

## Add Component In Editor

## Add Component In Code

