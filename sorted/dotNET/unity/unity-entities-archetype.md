# Unity Entites - Archetype

## What's It

- An identifier for container which contains entities with the same components
- For example: 
  - Archetype X
    - Entity A: Speed, Direction, Position, Renderer
    - Entity B: Speed, Direction, Position, Renderer
  - Archetype Y
    - Entity C: Speed, Direction, Position

## Features

- When add or remove a component from an entity, it will change the archetype of the entity
- Moving entities between archetypes frequently is resource-intensive
- So modifying entities' components should be done carefully

## Archetypes Chunk

What's Chunk

- Entities in the same archetype will be split into pieces with the same size, called [chunks](#chunk)

Features

- Chunks contains 
  - An **Array** of component [**types**](csharp-reflection-class-type.md)
  - An **Array** of entity IDs
- Chunks in Archetype is a contiguous block of memory
- Each chunk has the same size, 16Kb
- Chunk are always tightly packed, which means
  - when an entity add, it will be added to the last chunk
  - **when an entity remove, the last entity in the chunk will be moved to the removed entity's position**
 
## Creating an Archetype

Use `EntityManager.CreateArchetype` to create an archetype with specific components:

```cs
var archetype = entityManager.CreateArchetype(
    typeof(Translation),
    typeof(Rotation),
    typeof(MyComponent)
);
