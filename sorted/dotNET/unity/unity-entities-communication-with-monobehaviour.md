# Unity Entities Programming - Comnunication With MonoBahaviour

## Access System From MonoBehaviour

```cs
public class ExampleMono : MonoBehaviour
{
    public void Start() {
        var system = World.DefaultGameObjectInjectionWorld.GetExistingSystemManaged<ExampleSystem>();
    }
}
```

Why `GetExistingSystemManaged` and not `GetExistingSystem`?

- `GetExistingSystemManaged` accessing system **methods**, returns the instance of the system type
- `GetExistingSystem` returns a `SystemHandle`, which is for accessing system data [store by SystemHandle](unity-entities-organizing-system-data.md#how-to-get-systemhandle).

|             | GetExistingSystemManaged | GetExistingSystem  |
| ----------- | :----------------------: | :----------------: |
| return type | `T` type system instance |   `SystemHandle`   |
| Purpose     |  access system methods   | access system data |
