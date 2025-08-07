# Unity Entities - Baking

* [What's this](#what's-this)
* [What's for](#what's-for)
* [Authoring](#authoring)
* [When Baking Happens](#when-baking-happens)
* [Baker](#baker)
* [Baking World](#baking-world)
* [Baking System](#baking-system)
* [IBaker](#ibaker)
* [GetEntity Methods](#getentity-methods)
* [Filter Baking Output](#filter-baking-output)
* [BakeDerivedTypesAttribute](#bakederivedtypesattribute)

## What's this

- Converting data from [authoring](#authoring) data into ECS data 
- Process that converts GameObjects data into [entities](unity-entities-entity.md)

## What's for

- Unity use baker to read data from the input [authoring](unity-entities-authoring.md) scene
- Write to ecs component

## Authoring

> For convenient editing, GameObject data is made up of both runtime and authoring, which lead to bad runtime performance 

- To distinguish [Components](unity-component.md) like `MonoBehaviour` and [ECS component](unity-entities-component.md), former components are called **authoring components**
- Similar to **Authoring Scene** and **Authoring GameObject**. They are literally the Scene and GameObject when talking about unity
- Authoring data is any data that you create during the editing, such as scripts, assets

## When Baking Happens

- Whenever the authoring data in an authoring scene changes, baking process triggered
- Only in the editor

## Baker

- Step 1: Create Baker
  - Inherit from `Baker<TAuthoring>` where `TAuthoring` is the authoring component, normally a `MonoBehaviour` component
  - Override `Bake(TAuthoring authoring)` method to write data to the entity
- Step 2: Implement `Bake` method
  - Get the entity using [`GetEntity()`](#GetEntity Methods)
  - Use `AddComponent(entity, componentData)` to add component data to the entity

```cs
public class ExampleAuthoring : MonoBehaviour {
    public int exampleValue;
}

public struct ExampleComponent : IComponentData {
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

## Baking World


## Baking System

What's This

- A system declaration with `[WorldSystemFilter(WorldSystemFilterFlags.BakingSystem)]` attribute

Features

- Only execute at baking process
- Because it is a [system](), it can laverage Jobs and Burst compilation
- Baking System process component in batches
- Baking System don't automatically track [dependencies](unity-entities-system#system-dependency), which means Dependencies must be explicitly set
- Any entities [create](unity-entities-entity.md#create-entities-in-code) in baking system won't end up in a baked entity scene

Create A Baking System


```cs
public struct AnotherTag : IComponentData { }

[WorldSystemFilter(WorldSystemFilterFlags.BakingSystem)]
partial struct AddTagToRotationBakingSystem : ISystem
{
    public void OnUpdate(ref SystemState state)
    {
        var queryMissingTag = SystemAPI.QueryBuilder()
            .WithAll<RotationSpeed>()
            .WithNone<AnotherTag>()
            .Build();

        state.EntityManager.AddComponent<AnotherTag>(queryMissingTag);

        // Omitting the second part of this function would lead to inconsistent
        // results during live baking. Added tags would remain on the entity even
        // after removing the RotationSpeed component.

        var queryCleanupTag = SystemAPI.QueryBuilder()
            .WithAll<AnotherTag>()
            .WithNone<RotationSpeed>()
            .Build();

        state.EntityManager.RemoveComponent<AnotherTag>(queryCleanupTag);
    }
}
```

## IBaker

## GetEntity Methods

What those methods do

- get [entity](unity-entities-entity.md) from authoring gameobject/component

## Filter Baking Output

`[BakingType]`: Any component that is marked with this is filtered out from the baking output

- Which means when `AddComponent(entity, new ExampleComponetData())` in [baker](#baker), this component will not be added to the baked entity

## BakeDerivedTypesAttribute

- when baking `DerivedAuthoring`, the `BaseAuthoring` will also be baked

```cs
class BaseAuthoring : MonoBehaviour { public int BaseValue; }
class DerivedAuthoring : BaseAuthoring { public float DerivedValue; }

[BakeDerivedTypes]
class BaseBaker : Baker<BaseAuthoring> { public override void Bake(BaseAuthoring authoring) { }

class DerivedBaker : Baker<DerivedAuthoring> { public override void Bake(DerivedAuthoring authoring) { }
```
