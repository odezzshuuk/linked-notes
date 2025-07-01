# Unity Entities - Entity

## What's This

- icon 󰋙 represents an entity in editor

## Features

- Consists of various type of [Components](#component)

## Get Entities From GameObject

Baking from [authoring](#authoring) GameObject

- Detail about [baking](unity-entities-baking.md)

## Create Entities In Code

With [EntityManager](unity-entities-api-entitymanager.md)

- which potentially cause [structural changes](unity-entities-structural-changes.md)
- Which cause wait operation, may block main thread 
- `EntityManager` manages all the entites in the [world](#world)

With [EntityCommandBuffer](unity-entities-api-entitycommandbuffer.md)


