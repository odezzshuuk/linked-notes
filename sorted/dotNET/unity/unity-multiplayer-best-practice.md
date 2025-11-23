# Unity Multiplayer - Best Practices

* [Spawn a Network Prefab](#spawn-a-network-prefab)
* [Syncharizing Field](#syncharizing-field)
* [Change Client GameObject Field That Not NetworkVariable Type(Use NetworkObjectReference)](#change-client-gameobject-field-that-not-networkvariable(use-networkobjectreference))

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

## Syncharizing Field

Using [`NetworkVariable<T>`](unity-networkvariable.md) to synchronize field between server and client

- Default permissions: read by everyone, write by server only

```cs
publc class Example : NetworkBehaviour {
    // Declare a NetworkVariable with default arguments
    public NetworkVariable<int> count = new NetworkVariable<int>(
        0,
        NetworkVariableReadPermission.Everyone,
        NetworkVariableWritePermission.Server

    );
    // Declare a NetworkVariable with permission arguments
    public NetworkVariable<int> count = new NetworkVariable<int>(

    public override void OnNetworkSpawn() {
        // listen on the value changed event
        count.OnValueChanged += ValueChangedCallback;
    }

    public override void OnNetworkDespawn() {
        // unsubscribe from the value changed event
        count.OnValueChanged -= ValueChangedCallback;
    }

    private void ValueChangedCallback(int oldValue, int newValue) {
        Debug.Log($"Count changed from {oldValue} to {newValue}");
    }
}
```


## Changing Client GameObject Field That Not NetworkVariable Type(Use NetworkObjectReference)

Check [unsupported serialization types](unity-multiplayer-serialization.md#unsupported-serialization-types)

```cs
public class Example : NetworkBehaviour {
    public int count;
}

public class Program : NetworkBehaviour {

    [Rpc(SentTo.Everyone)]
    public void ChangeClientObjectCountRpc(NetworkObjectReference nobjRef) {
        GameObject obj = nobjRef;  // implicit conversion
        Example example = obj.GetComponent<Example>();
        example.count = 10;
    }

}
```


