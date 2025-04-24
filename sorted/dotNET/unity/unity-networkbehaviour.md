# Unity Multiplayer - NetworkBehaviour

* [What's This](#what's-this)
* [Spawning And Despawning](#spawning-and-despawning)
* [Synchronization](#synchronization)
* [Dynamically Spawn](#dynamically-spawn)

## What's This

- An abstract class derives from [MonoBehaviour](unity-monobehaviour.md)
- Where user add netcode logic
- Receive or send netcode-aware properties
- NetworkBehaviour component need a [NetworkObject]() component to do network-related tasks, such as Rpc

```cs
public class Example : NetworkBehaviour {
  public void OnNetworkSpawn() { }
}
```

## Spawning And Despawning

Unity Method Invoke Order

1. In-scene object

- `Awake() -> OnNetworkSpawn() > Start()`

2. [Dynamically spawned](#dynamically-spawn)

- `Awake() -> Start() -> OnNetworkSpawn()`

## Synchronization

[Synchronization](unity-networkbehaviour-synchronization.md)

## Dynamically Spawn

Dynamically spawned include

- Instantiate prefab
- From disabled to enable

**Operation order of NetworkObject dynamically spawn**

- Server Side

1. NetworkObject instantiate
2. NetworkObject spawn, `OnNetworkSpawn()` invoked
3. `CreateObjectMessage` is generated
  - `NetworkObject` state is serialized
  - `NetworkVairbale` state is serialized
  - `NetworkBehaviour.OnSynchronize` is invoked for each `NetworkBehaviour` component
4. Send `CreateObjectMessage` to all clients that are observers of the `NetworkObject`

- Client Side

1. Receive `CreateObjectMessage`
  - `NetworkObject` is instantiated
  - `NetworkVariable` state is deserailized and applied
  - `Networkbehaviour.OnSynchronize` is invoked for each `NetworkBehaviour` component
2. `NetworkObject` is spawned

**Operation order of full client synchronization**

- Server Side

1. `SceneEventMessage` of type `SceneEventType.Synchronize` is received
  - All spawned NetworkObjects that are visible to the client, already instantiated, and spawned are serialized.
    - NetworkObject state is serialized.
    - NetworkVariable state is serialized.
    - NetworkBehaviour.OnSynchronize is invoked for each NetworkBehaviour component.
      - If this method isn't overridden then nothing is written to the serialization buffer.
2. `SceneEventMessage` is sent to the client

- Client Side

1. Receive `SceneEventMessage` of type `SceneEventType.Synchronize` is received
2. Scene information is deserialized and scenes are loaded(if not already)
  - In-scene placed NetworkObjects are instantiated when the a scene is loaded
3. All `NetworkObject` synchronization information is deserialized
  - Dynamically spawned NetworkObjects are instantiated and state is synchronized.
  - For each NetworkObject instance:
    - `NetworkVariable` state is deserialized and applied.
    - `NetworkBehaviour.OnSynchronize` is invoked.
      - If this method isn't overridden then nothing is read from the serialization buffer.
    - The `NetworkObject` is spawned.
      - For each associated `NetworkBehaviour` component, `NetworkBehaviour.OnNetworkSpawn` is invoked.


