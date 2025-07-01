# Unity Entites - EntityManager

## What's For

- Useful for managing [structural changes](unity-entities-structural-changes.md)

## Features

- Some api can cause [structural changes](unity-entities-structural-changes.md)
- When structural changes performed, 
  - `EntityManager` wait for all jobs to complete
  - This will create a [sync point(wait operation)](csharp-task#wait-a-task)
  - Which can cause performance issues
- Can't work with [jobs](unity-jobs.md)
- Only methods `CreateEntity()`, `Instantiate()`, `CreateArchetype()` allowed in [`SystemAPI.Query()`](unity-entities-api-systemapi)

## Method

`CreateEntity()`

`Instantiate()`

`DestroyEntity()`

`AddComponent()`

`RemoveComponent()`

`GetComponentData()`

