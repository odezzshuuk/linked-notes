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

When Player Object is spawned

- when scene management is disabled, spawned when a joining client's is [approved]()
- when scene management is enabled, spawned when a joining client's finished initial [synchronization](unity-multiplayer-scene-management.md#synchronization)

## Spawning

What's Spawning

- When create a GameObject with `Instantiate()`, it will only create on local machine
- Spawning a [`NetworkObject`](#networkobject) means
  - Instantiate the `NetworkObject` on local machine
  - Synchronized between all clients by the server

Features

- Only server can spawn NetworkObjects

## Scene Management

[Scene Management](unity-multiplayer-scene-management.md)

## Synchronization

## Serialization

[Serialization](unity-multiplayer-serialization.md)

## NetworkVariable

[NetworkVariable](unity-networkvariable.md)

## OwnerShip

Misunderstandings

- `NetworkManager.LocalClientId` is not `NetworkBehaviour.OwnerClientId`

## Connection Approval

## Rpc

Rpc as event listener

```cs
public override void OnNetworkSpawn() { }
```

