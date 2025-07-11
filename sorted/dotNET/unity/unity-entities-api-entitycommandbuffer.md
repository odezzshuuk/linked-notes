# Unity Entities API - EntityCommandBuffer

## What's This

- A queue of thread-safe commands which you can [add to]() and [playback]()

## Features

- Methods in `EntityCommandBuffer` record commands are mirror to [`EntityManager`](unity-entities-api-entitymanager.md) methods
- Commands stored in `EntityCommandBuffer` eventually will be executed via [`EntityManager`](unity-entities-api-entitymanager.md)
- Can be used to decrease the number of [sync points](csharp-task#wait-a-task) in your code

## How To Use

```cs
public override void OnUpdate() {
    EntityCommandBuffer ecb = new EntityCommandBuffer(Allocator.TempJob);

    // The ECB is captured by the ForEach job.
    // Until completed, the job owns the ECB's job safety handle.
    Entities
        .ForEach((Entity e, in FooComp foo) =>
        {
            if (foo.Value > 0)
            {
                // Record a command that will later add BarComp to the entity.
                ecb.AddComponent<BarComp>(e);
            }
        }).Schedule();

    Dependency.Complete();

    // Now that the job is completed, you can enact the changes.
    // Note that Playback can only be called on the main thread.
    ecb.Playback(EntityManager);

    // You are responsible for disposing of any ECB you create.
    ecb.Dispose();
}
```

## Playback

What's this

- Play back all recorded operations on an [entity manager](unity-entities-api-entitymanager.md)

Features 

- Can only be called on the main thread

`Playback(EntityManager entityManager)`
