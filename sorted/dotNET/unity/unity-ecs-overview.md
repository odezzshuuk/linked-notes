# Unity - ECS Overview

## Overview

For ECS Structure Example:

- [Archetype](unity-entities-archetype) X
  - [Entity](unity-entities-entity) A: Speed, Direction, Position, Renderer
  - Entity B: Speed, Direction, Position, Renderer
- Archetype Y
  - Entity C: Speed, Direction, Position

Explanation

- `Speed`, `Direction`, `Position`, and `Renderer` are [Components](unity-entities-component) of the entities.
- [System](unity-entities-system) for organizing(init, update) the logic of those components.

## World

[World](unity-entities-world) and [system](unity-entities-system) are created at the very beginning of the game

- after assembliies loaded
- before the first frame of first scene is loaded
