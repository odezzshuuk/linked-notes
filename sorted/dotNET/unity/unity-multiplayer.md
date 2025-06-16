# Unity - Multiplayer

## Concepts

[Concepts](unity-multiplayer-concepts.md)

## Best Practice

[Best Practice](unity-multiplayer-best-practice.md)

## Things Happening Order When Client Connecting Succeed

Send Connection Request

Connected

Handle Scene Synchronize Event Send By Server

- first is [scene synchronization](unity-multiplayer-scene-management.md#synchronization)
  - includes all scenes the server has loaded
- [networkobject synchronization](unity-networkbehaviour-synchronization.md) after all scenes are loaded

## Things Happening Order On Server

Handle Connection Request

Approval Check

Handle Scene Synchronize Complete Event


