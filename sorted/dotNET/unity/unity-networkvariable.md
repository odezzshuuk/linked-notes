# Unity Multiple - NetworkVariable

## What Is That

## How To Use

Listen on network variable changes

```cs
public class Example : NetworkBehaviour {
    // Declare a NetworkVariable
    public NetworkVariable<int> myInt = new NetworkVariable<int>();

    public override void OnNetworkSpawn() {
        myInt.OnValueChanged += MyIntChangedCallback;
    }

    public override void OnNetworkDespawn() {
        myInt.OnValueChanged -= MyIntChangedCallback;
    }

    public void MyIntChangedCallback(int oldValue, int newValue) {
        Debug.Log($"MyInt changed from {oldValue} to {newValue}");
    }

} 
```

With permission arguments to `NetworkVariable` constructor

```cs
public NetworkVariable<int> myInt = new NetworkVariable<int>(
  0,
  NetworkVariableReadPermission.Everyone,  // read permission
  NetworkVariableWritePermission.Owner     // write permission
);
```

## Supported Types

- Mostly same as [multiplayer serialization type](unity-multiplayer-serialization.md#who-can-be-serialized) for supported types
- Except that `string` is not support


## INetworkSerializable

## INetworkSerializeByMemcpy
