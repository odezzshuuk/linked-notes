# Unity - Jobs

* [What's For](#what's-for)
* [Features](#features)
* [Job Types](#job-types)
* [How To Create Job](#how-to-create-job)
* [Job Complete](#job-complete)
* [NativeContainer](#nativecontainer)
* [Job Dependency](#job-dependency)
* [Parallel Jobs](#parallel-jobs)
* [Avoid Long Running Jobs](#avoid-long-running-jobs)
* [JobHandle](#jobhandle)

## What's For

- Create **multithread** code

## Features

- Only access [blittable](csharp-types#primitive-types) data types
- Only main thread can [schedule]() and [wait complete](#job-complete) jobs

## Job Types

- [IJob](#IJob)
  - A job run on one worker thread
- [IJobFor](#IJobFor): 
  - A job run on multiple worker threads
  - A job that performs same operation on each element of a native container
  - Each worker thread has an exclusive index to access shared data between worker threads
  - Same as IJobParallelFor
  - But allows you to schedule the job so it doesn't run in parallel
- IJobParallelFor: 
  - A job run on multiple worker threads
  - Each worker thread has an exclusive index to access shared data between worker threads
- IJosParallelForTransform

## How To Create Job

1. Implement IJob interface
2. Schedule the job
3. Wait for the job to complete

Implement IJob interface

```cs
public struct ExampleJob: IJob
{
    public NativeArray<float> data; // Thread-safe container
    public float multiplier;

    public void Execute()
    {
        for (int i = 0; i < data.Length; i++)
        {
            data[i] *= multiplier; // Example operation
        }
    }
}
```

Schedule the job

```cs
public class ExampleBehaviour : MonoBehaviour {
    private NativeArray<float> result;
    private JobHandle jobHandle;

    void Start() 
    {
        data = new NativeArray<float>(10, Allocator.TempJob);
        for (int i = 0; i < data.Length; i++)
        {
            data[i] = i; // Initialize data
        }
    }

    void Update()
    {
        result = new NativeArray<float>(10, Allocator.TempJob);

        for (int i = 0; i < result.Length; i++) {
            result[i] = i * 1.0f; // Initialize result data
        }

        var job = new ExampleJob
        {
            data = result,
            multiplier = 2.0f
        };
        jobHandle = job.Schedule(); // Schedule the job
    }

    void LateUpdate()
    {
        jobHandle.Complete(); // Wait for the job to complete

        // Dispose of the NativeArray
        result.Dispose();
    }
}
```

## Job Complete

Explicitly wait for a job to complete in main thread

- It is not mandatory
- Call `JobHandle.Complete()` to wait for the job to finish
- Best practice is to call `Complete()` as late as possible

## Job Dependency

- If one job depends on the result of another job, Must explicitly set the dependency
- A job must wait for its dependencies to [complete](#job-complete) before it can run
- Which means when a job set as a dependency, it will be implicitly waited for its completion

Adding dependency

- Passing a [JobHandle](unity-jobs-jobhandle) to `Job.Schedule(dependency)` method

```cs
JobHandle jobA = jobA.Schedule();
jobB.Schedule(jobA);
```

- `jobB` depends on `jobA`

Combining/merging dependencies

- Method `JobHandle.CombineDependencies`

```cs
NativeArray<JobHandle> jobHandles = new NativeArray<JobHandle>(4, Allocator.TempJob);
JobHandle mergedHandle = JobHandle.CombineDependencies(jobHandles);
```

## Parallel Jobs

[Parallel Jobs](unity-jobs-parallel-jobs.md)

## Avoid Long Running Jobs

- Unlike thread, jobs dont yield execution
- Once a job starts, job worker thread commits to completing the job **before running any other job**.

So best practice is to break long-running jobs into smaller jobs.

- One job depends on another job

## JobHandle

[JobHandle](unity-jobs-jobhandle.md)

## Thread Safety

[NativeContainer](unity-jobs-nativecontainer.md)


