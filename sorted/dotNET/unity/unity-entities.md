# Unity - Entities

## Best Practices

> ECS: Entity Component System

[Best Practices](unity-entities-best-practices.md)

## Entity

What's it

- icon 󰋙 represents an entity in editor

Features

- Consists of various type of [Components](#component)

How to create entities

- `EntityManager` manages all the entites in the [world](#world)

```cs
// ...
```

How entities come from

- [Baking](#baking) subscene GameObject
- create baker, use MonoBehaviour component data to create 

## Component

[Component](unity-entities-component.md)

## System

- perform logic on component data

System types

- SystemBase
- ISystem
- EntityCommandBufferSystem: allows group [structural changes]()
- ComponentSystemGroup

method to override

- `OnUpdate()`, `OnCreate()`, `OnDestroy()`

```cs
public partical class MovementSystem : SystemBase {
    protected override void OnUpdate()
    {
        Entities.ForEach((ref Translation translation, in Velocity velocity) =>
        {
            translation.Value += velocity.Value * Time.DeltaTime;
        }).Schedule();
    }
}

```

System Groups

- More about [SystemGroup](#systemgroup)

how to query

- ...

## Authoring

> For convenient editing, GameObject data is made up of both runtime and authoring, which lead to bad runtime performance 

What's this

- To distinguish [Components](unity-component.md) like `MonoBehaviour` and [ECS component](unity-entities-component.md), former components are called **authoring components**
- Similar to authoring Scene and authoring GameObject
- Authoring data is any data that you create during the editing, such as scripts, assets

## Baking

[Baking](unity-entities-baking.md)

## Spawner

## World

- Collection of entities and systems

## SystemGroup

[SystemGroup](unity-entities-systemgroup.md)

## Archetypes

[Archetype](unity-entities-archetype.md)

## Structural Changes

What's It

- Operations that cause unity reorganizing [chunks](unity-entities-archetype.md#archetypes-chunk)

Why Structural Changes Matter

- Although ECS can increase performance, When structural changes performed, it can cause intensive resource usage

Features

Which considered structural changes

- Creating or destroy [entities](#entity)
- Adding or remove [components](#component)
- Setting a [shared component](unity-entities-component.md#shared-component) value

Managed Structural Changes


