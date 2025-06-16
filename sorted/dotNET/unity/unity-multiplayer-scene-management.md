# Unity Multiplayer - Scene Management

## Event On SceneManager

Events name

- **To receive all scene event type, use `OnSceneEvent` event**
- `OnLoad`: Invoked only when a Load event is being processed
- `OnUnload`: Invoked only when an Unload event is being processed
- `OnSynchronize`: Invoked only when a Synchronize event is being processed
- `OnLoadEventCompleted`: Invoked only when a LoadEventCompleted event is being processed
- `OnUnloadEventCompleted`: Invoked only when an UnloadEventCompleted event is being processed
- `OnLoadComplete`: Invoked only when a LoadComplete event is being processed
- `OnUnloadComplete`: Invoked only when an UnloadComplete event is being processed
- `OnSynchronizeComplete`: Invoked only when a SynchronizeComplete event is being processed

How to subscribe

- Which can be directly subscribe the access event name on `SceneManger`

```cs
public voie OnNetworkSpawned() {
    NetworkManager.Singleton.SceneManager.OnLoad += SceneLoadCallback;
}
// ...
public void SceneLoadCallback(SceneEvent sceneEvent) {
    // ...
}
```

## Scene Event Type

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

How to subscribe

1. subscribe to `OnSceneEvent` event of `SceneManager` to receive all scene event types
2. use `SceneEventType` enum to check the type of the event

```cs
public void OnNetworkSpawned() {
    NetworkManager.Singleton.SceneManager.OnSceneEvent += SceneEventCallback;
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

## Talk Scene Events By Group

- [Loading](#loading)
- [Unloading](#unloading)
- [Synchronization](#synchronization)

## Loading

## Unloading

## Synchronization

`SceneEventType.Synchronize`

`SceneEventType.SynchronizeComplete`

- All netcode objects spawned on client
- Message send to server include all the NetworkObjects that client spawned

`SceneEventType.ReSynchronize`



