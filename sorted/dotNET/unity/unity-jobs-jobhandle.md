# Unity Jobs - JobHandle

## What It Is

- A struct that represents a handle to a job or a group of jobs.

## How To Get It

- returned by the `Schedule()` method

## What's JobHandle Can Do

Manage dependencies

```cs
JobHandle jobAHandle = jobA.Schedule();
JobHandle jobBHandle = jobB.Schedule(jobAHandle);
```

- jobB depends on jobA

Synchronize jobs

- `Complete()` for main thread to wait until the job is finished
- If the job is uncompleted when `Complete()` is called, it will block the main thread

```cs
jobHadle.Complete();
```

## Method

Static

`CheckFencelsDependencyOrDidSyncFence()`

`CombineDependencies()`

`CompleteAll()`

`ScheduleBatchedJobs()`


