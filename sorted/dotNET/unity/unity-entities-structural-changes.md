# Unity Entities - Structural Changes

## What's It

- Operations that cause unity reorganizing [chunks](unity-entities-archetype.md#archetypes-chunk)

## Why Structural Changes Matter

- Although ECS can increase performance, When structural changes performed, it can cause intensive resource usage

## Features

## Which considered structural changes

- Creating or destroy [entities](#entity)
- Adding or remove [components](#component)
- Setting a [shared component](unity-entities-component.md#shared-component) value

## Managed Structural Changes

- Both [`EntityManager`](unity-entities-api-entitymanager.md) and [`EntityCommandBuffer`](unity-entities-api-entitycommandbuffer) can perform structural changes
- Structural changes caused by `EntityManager` execute in a sync way
- To queue structural changes, use `EntityCommandBuffer`

When `EntityManager` And When `EntityCommandBuffer`

- Use `EntityManager` Ok with perform structural changes in a sync(block) way in main thread
- When optimize with [jobs](), use `EntityCommandBuffer` to queue structural changes
- For `EntityManager` Only methods `CreateEntity()`, `CreateArchetype()`, `Instantiate()` allowed in [`SystemAPI.Query()`](unity-entities-api-systemapi)
  - which means you can't add component use `EntityManager` in `SystemAPI.Query()`
- To Add a component in `SystemAPI.Query()`, use `EntityCommandBuffer.AddComponent()`


