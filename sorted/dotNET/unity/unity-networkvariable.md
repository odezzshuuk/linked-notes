# Unity Multiple - NetworkVariable

## What Is That

## How To Use

```cs
public class Example : NetworkBehaviour {
    // Declare a NetworkVariable
    public NetworkVariable<int> myInt = new NetworkVariable<int>();

    public override void OnNetworkSpawn() {

    }

} 
```

## Supported Types

- Mostly same as [multiplayer serialization type](unity-multiplayer-serialization.md#who-can-be-serialized) for supported types
- Except that `string` is not support


## INetworkSerializable

## INetworkSerializeByMemcpy
