# Unity Jobs - Parallel Jobs

* [What's This](#what's-this)
* [Features](#features)
* [How To](#how-to)
* [parameters of `ScheduleParallelByRef`:](#parameters-of-`scheduleparallelbyref`:)
* [Handle Delta Time](#handle-delta-time)
* [IJobFor](#ijobfor)
* [IJobParallelFor](#ijobparallelfor)

## What's This

- When schedule a job, it can only run on one worker thread
- Sometimes you need to perform the **same** operation on a lot of objects

## Features

- A job run on multiple [worker]() threads
- A job that performs same operation **independently** 
  - On each element of a native container 
  - Or on fixed number of iterations
- Each worker thread has an exclusive index to access shared data between worker threads

> Operation's independence is crucial

## How To

Use [`IJobFor`](#ijobfor) as instruction

1. Implement `IJobFor` interface
2. Commonly a `NativeArray<T>` field to store source data
3. Implement `Execute(int index)` method(Each `index` execute once)
4. Schedule with method [`ScheduleParallelByRef(int length, int batchSize, dependency)`](#parameters-of-scheduleparallelbyref)

```cs
public struct IncrementByDeltaTimeJob : IJobParallelFor {
    public NativeArray<float> values;
    public float deltaTime;

    public void Execute(int index) {
        float temp = values[index];
        temp += deltaTime
        values[index] = temp;
    }
}
```

- About why [`values` update that way](unity-jobs-nativecontainer.md#how-to-change-elements-value)

## parameters of `ScheduleParallelByRef`:

- `length`: number of iterations
- `batchSize`: number of iterations per worker thread
  - when there is a lot of work in each iteration, a value of 1 can be sensible
  - when there is very little work, values of 32 or 64 can make sense
- `dependency`: job handle to wait for before running the job

## Handle Delta Time

Delta time must be copied to the job

- Jobs generally don't have concept of a frame
  - Jobs are decoupled from the main thread
  - jobs are executed on worker threads
- which means `position += velocity * Time.deltaTime` is not valid

```cs
public struct ExampleJob : IJobFor
{
    public NativeArray<Vector3> position;
    public float deltaTime;

    public void Execute(int index)
    {
        position[index] += new Vector3(0, 10, 0) * deltaTime;
    }
}
```

## IJobFor

- Same as [IJobParallelFor](#ijobparallelfor)
- But allows you to schedule the job so it doesn't run in parallel

## IJobParallelFor

- mostly for backward compatibility


