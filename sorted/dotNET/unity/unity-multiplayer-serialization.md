# Unity Multiplayer - Serialization

* [What's serialization ](#what's-serialization)
* [When serialization occurs](#when-serialization-occurs)
* [Who can be serialized](#who-can-be-serialized)

## What's serialization

## When serialization occurs

- Rpc
- NetworkVariable
- NetworkSerializer

## Who can be serialized

- Unmanaged types
- Any type(include managed types) "that" implements `INetworkSerializable` interface
- Unity fixed string types: `FixedString32Bytes`, `FixedString64Bytes`, `FixedString128Bytes`, `FixedString512Bytes`

## Unsupported Serialization Types

- **Type** `GameObject`, `NetworkObject`, `NetworkBehaviour` will **NOT serialized**


