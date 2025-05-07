# Unity - Multiplayer Concepts

* [NetworkBehaviour](#networkbehaviour)
* [NetworkObject Component](#networkobject-component)
* [NetworkObject](#networkobject)
* [NetworkManager](#networkmanager)
* [Player Object](#player-object)
* [Spawning](#spawning)
* [Scene Management](#scene-management)
* [Synchronization](#synchronization)
* [Serialization](#serialization)
* [NetworkVariable](#networkvariable)
* [OwnerShip](#ownership)
* [Connection Approval](#connection-approval)
* [Rpc](#rpc)

## NetworkBehaviour

[NetworkBehaviour](unity-networkbehaviour.md)

## NetworkObject Component

properties

- AlwaysReplicateAsRoot
- SynchronizeTransform
- ActiveSceneSynchronization
- SceneMigrationSynchronization
- SpawnWithObservers
- DontDestroyWithOwner
- ...

Component order

- NetworkObject component must before any other [NetworkBehaviour](unity-networkbehaviour.md)

## NetworkObject

[NetworkObject](unity-networkobject.md)

## NetworkManager

what's this

- Central netcode hub

properties

- [PlayerPrefab](#player-prefab)
- [NetworkPrefabs](#network-prefabs)

## Player Object

- Asign A [NetworkObject](#networkobject) a specific client as Player Object
- Player Object can be create by instantiated the reference the NetworkObject assigned to `PlayerPrefab` property of [NetworkManager](#networkmanager)

## Spawning

What's Spawning

- When create a GameObject with `Instantiate()`, it will only create on local machine
- Spawning a [`NetworkObject`](#networkobject) means
  - Instantiate the `NetworkObject` on local machine
  - Synchronized between all clients by the server

Features

- Only server can spawn NetworkObjects

## Scene Management

How to subscribe

```cs
public voie Example() {
    NetworkManager.Singleton.SceneManager.OnLoad += SceneLoadCallback;
    NetworkManager.Singleton.SceneManager.OnSceneEvent += SceneEventCallback;
}

private void ScenenLoadCallback() {
  // ...
}

private void SceneEventCallback(SceneEvent sceneEvent) {
    switch (sceneEvent.Type) {
        case SceneEventType.Load:
            break;
        case SceneEventType.Unload:
            break;
        case SceneEventType.Synchronize:
            break;
        default:
            break;
    }
}
```

Scene [Event](csharp-events.md) Properties

- **To receive all scene event type, use `OnSceneEvent` event**
- `OnLoad`: Invoked only when a Load event is being processed
- `OnUnload`: Invoked only when an Unload event is being processed
- `OnSynchronize`: Invoked only when a Synchronize event is being processed
- `OnLoadEventCompleted`: Invoked only when a LoadEventCompleted event is being processed
- `OnUnloadEventCompleted`: Invoked only when an UnloadEventCompleted event is being processed
- `OnLoadComplete`: Invoked only when a LoadComplete event is being processed
- `OnUnloadComplete`: Invoked only when an UnloadComplete event is being processed
- `OnSynchronizeComplete`: Invoked only when a SynchronizeComplete event is being processed

Scene Events Enum `SceneEventType`

- Loading:
  - `SceneEventType.LoadComplete`: signifies that a scene has been loaded locally. Clients send this event to the server.
  - `SceneEventType.LoadEventCompleted`: signifies that the server and all clients have finished loading the scene and signifies that the Scene Event has completed.
- Unloading:
  - `SceneEventType.UnloadComplete`: 
  - `SceneEventType.UnloadEventCompleted`
- Synchronization
  - `SceneEventType.SynchronizeComplete`
  - `SceneEventType.ReSynchronize`

## Synchronization

## Serialization

[Serialization](unity-multiplayer-serialization.md)

## NetworkVariable

[NetworkVariable](unity-networkvariable.md)

## OwnerShip

- In client-server topology, server owns all NetworkObjects

## Connection Approval

## Rpc




