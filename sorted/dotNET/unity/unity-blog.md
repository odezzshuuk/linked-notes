# Unity - Blog

## For Materials Having Different Look In Different Scene Or Project

- [Project Color Space Setting](unity-project-settings.md#player)
- [Lighting Setting](unity-lighting.md)

## Why Materials display pink

- [unity shader](unity-shader-object.md#error-shader)

## Why Unity Re-compile Is Extremely Slow

- By Default, all assemblies in your project created with [assembly definitions](unity-assembly-definition.md) automatically reference all precompiled assemblies
- Unity must recompile all your assembiles when you update any single line of the precompiled assemblies

## Why KeyNotFoundException When Send Rpc

This is happened when 

- Subscribe Rpc method in `OnEnable` and unsubscribe in `OnDisable`, 
- And the Rpc method is called before the NetworkObject is spawned.

```cs
public class Example : NetworkBehaviour
{
    public event Action someEvent;
    public override void OnEnable()
    {
        someEvent += PingRpc;
    }
    public override void OnDisable()
    {
        someEvent -= PingRpc;
    }
    [ClientRpc]
    private void PingRpc()
    {
        // Do something
    }
}
```

Analysis:

Solution:

```cs
public class Example : NetworkBehaviour
{
    public event Action someEvent;
    public override void OnEnable()
    {
        someEvent += PingRpc;
    }
    public override void OnDisable()
    {
        someEvent -= PingRpc;
    }
    public void Ping() {
        if (IsSpawned)
        {
            PingRpc();
        }
        else
        {
            Debug.LogWarning("NetworkObject is not spawned yet.");
        }

    }
    [ClientRpc]
    private void PingRpc()
    {
        // Do something
    }
}
```

2. or subcribe the Rpc method in `OnNetworkSpawn`




