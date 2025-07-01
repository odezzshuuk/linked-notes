# Unity Entities API - SystemBase.Entities.ForEach

## How to use

- By passing a lambda expression as parameter like that `Entities.ForEach(<lambda expression>)`

## Standard Delegate 

- Standard lambda expression looks like: `(Entity entity, int entitiyInQueryIndex, ref ObjectPosition translation, in Movement move) => { /* code */ }`
- Up to 8 parameters for lambda expression

## Entities.ForEach Delegate Detail

Lambda expression parameters must be group in following order 

- Parameters passed-by-value(no parameter modifiers)
- Writable parameters(parameter `ref` modifiers)
- Read-only parameters(parameter `in` modifier)

Why `ref` and `in` modifiers?

- Argument pass to no modifiers parameter of lambda expression is a copy 
- So if a parameter is only need to read, this will take up extra memory

## Component Paramaters

```cs
Entities.ForEach((ref Destination outputData, in Source inputData) => {
    outputData.Value = inputData.Value;
}).ScheduleParallel();
```

- To update component data, use `ref` modifier
- To declare a read-only component, use `in` modifier

## Named Parameters

- For unity assigning values itself
  - `Entity entity`
  - `int entityInQueryIndex`
  - `int nativeThreadIndex`
  - `EntityCommands commands`

`Entity entity`

- Current entity. 
- Parameter's name can be anything, as long as the type is `Entity`.

`int entityInQueryIndex`

- The index of the entity in the list of all entities that the query selected. 
- Use the entity index value when you have a [native array]() that you need to fill with a unique value for each entity. 
- Use the `entityInQueryIndex` as the index in that array. 
- Use `entityInQueryIndex` as the sortKey to add commands to a concurrent entity command buffer.

`int nativeThreadIndex`

- A unique index of the **THREAD** executing the current iteration of the lambda expression. 
- When you use Run to execute the lambda expression, nativeThreadIndex is always zero. Don't use nativeThreadIndex as the sortKey of a concurrent entity command buffer; use entityInQueryIndexinstead.

`EntityCommands commands`

- Can be any name, as long as the type is `EntityCommands`.
- Use this parameter only in conjunction with either `WithDeferredPlaybackSystem<T>` or `WithImmediatePlayback`. The `EntityCommands` type has several methods that mirror their counterparts in the `EntityCommandBuffer` type. 
- If you use an `EntityCommands` instance inside `Entities.ForEach`, 
- The compiler creates extra code where appropriate to handle the creation, scheduling, playback, and disposal of entity command buffers, on which counterparts to EntityCommands methods are invoked.

## Capture Variable Restrictions

Restrictions when lambda expression execute in a job(`ScheduleParallel()` or `Schedule()`, not `Run()`):

- You can only capture [native containers]() and [blittable]() types.
- A job can only write to captured variables that are **native containers**. To return a single value, create a native array with one element.

## Execute Lambda Expression

3 ways to execute the lambda expression:

- `ScheduleParallel()`
  - Execute the lambda expression on multiple job worker threads.
  - Each job instance process by [chunk](unity-entities-archetype.md#archetypes-chunk)
- `Schedule()`
- `Run()`
  - Execute the lambda expression on the main thread.
  - Blocking the main thread

Instructions

- When call `Schedule()` and `ScheduleParallel()` without arguments, the `SystemBase.Dependency` will be used as the job dependency.
  - Which is unlike [scheduling job](unity-jobs#job-dependency), no arguments means no dependency.
- When pass a `JobHandle` as argument, the `SystemBase.Dependency` will be replaced, not combined.

## Custom Delegate

## Limitations
