# Unity Multiplayer - Best Practices

## Spawn a Network Prefab

> Only server can spawn NetworkObjects

Register the prefab in the [`NetworkManager`](unity-multiplayer-concepts.md#networkmanager) component

1. Create scriptable object: `Create/Netcode/NetworkPrefabsList`
2. Create a prefab with `NetworkObject` component
3. Assign the prefab to `NetworkPrefabsList` object
4. Assign the `NetworkPrefabsList` object to `NetworkManager.NetworkPrefabsLists` field

Code to spawn a prefab

```cs
public class ExampleUI : NetworkBehaviour {

    [SerializeField] private GameObject examplePrefab;
    [SerializeField] private Button spawnButton;

    public void OnEnable() {
        spawnButton.onClick.AddListener(DynamicllySpawnPrefab);
    }

    [Rpc(SentTo.Server)]  // ① 
    public void DynamicllySpawnPrefab() {
        var instance = Instantiate(examplePrefab);
        var instanceNetworkObject = instance.GetComponent<NetworkObject>();
        instanceNetworkObject.Spawn(); // ②
    }
}
```

1. When spawnButton clicked on a client, attribute `[Rpc(SentTo.Server)]` is used to send the message to server

- without `[Rpc]` attribute, click spawnButton will throw `NotServerException: Only server can spawn NetworkObjects`

2. `Spawn(bool destroyWithSceneObject = false)` method takes 1 optional parameter


