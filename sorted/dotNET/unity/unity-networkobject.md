# Unity Multiplayer - NetworkObject

- A GameObject with a [NetworkObject component](unity-multiplayer-concepts.md#networkobject-component) and at least one [NetworkBehaviour](unity-networkbehaviour.md)

## Fields And Properties

Scene-Related

- Property `DestroyWithScene`: When Scene is unloaded, the object will be destroyed
- Field `SceneMigrationSynchronization`: Synchronized when migrated to a different scene via `MoveGameObjectToScene(GameObject go, Scene scene)`

