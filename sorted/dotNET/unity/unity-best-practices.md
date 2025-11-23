# Unity - Best Practices

## .meta file

- is auto-generated file, but included in version control

## Debug

[Debug](unity-debug.md)

## Show Up Hide Tools In Scene

[show up hide tools](unity-editor-scene.md#show-up-hide-tools-in-scene)

## Show Up Hide Window

## Searching By Filter

- `t:`: Type Filter, `t:Enemy` Search asset with [type name]() contain `Enemy`

## NetworkManager issue 

Description:

- Whenever load back to the scene where orginal `NetworkManager` is, it will create another `NetworkManager` instance, causing conflict

Solution:

1. Manage duplicates by code

- For example

```cs
public class Application: MonoBehaviour {
    private void Awake() {
        var networkManagers = FindObjectsOfType<NetworkManager>();
        if (networkManagers.Length > 1) {
            Destroy(gameObject); // Destroy duplicate NetworkManager
        } else {
            DontDestroyOnLoad(gameObject); // Keep the original NetworkManager
        }
    }
}

```

2. Create a bootstrap scene with `NetworkManager` , which only loads once and never back to this scene during the game


