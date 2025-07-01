# Unity Entities API - SystemAPI Query

## What is SystemAPI.Query<T>

- A **generic** component [query](unity-entities-query-entities.md#whats-query) method that takes component type or **wrapped component type** as a type parameter

## Supported Type Parameters

- [`IAspect`](unity-entities-aspect.md)
- `IComponentData`
- `ISharedComponentData`
- `DynamicBuffer<T>`
- [`RefRO<T>`]
- [`RefRW<T>`]
- `EnabledRefRO<T> where T : IEnableableComponent, IComponentData`
- `EnabledRefRW<T> where T : IEnableableComponent, IComponentData`

`RefRW<T>/RefRO<T>`

- `RefRW<T>.ValueRW`, `RefRW<T>.ValueRO`, `RefRO<T>.ValueRO` all return a `T` type reference

## Accessing Entities

- use `WithEntityAccess()` to access the entity

```cs
foreach (var (transform, speed, entity) in SystemAPI.Query<RefRW<LocalToWorld>, RefRO<RotationSpeed>>().WithEntityAccess()) {
}
```

## Limitations

- [`DynamicBuffer<T>`]() type parameters in `SystemAPI.Query<T>` are read-write access by default
- Not Reusable. Can't be stored in a variable then use it in multiple `foreach` statement,  for example reuse like that `Queryer queryer = SystemAPI.Query<RefRW<LocalTransform>, RefRO<RotationSpeed>>();` is not work

## About Entities Query


