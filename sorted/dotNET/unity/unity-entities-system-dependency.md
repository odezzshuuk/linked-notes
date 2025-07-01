# Unity Entities - System Dependency

## What's This

- A Reference to a JobHandle instance 
- JobHandle of jobs need to be completed before `OnUpdate()`
  - writes to the same component that current system reads
  - reads the same component that current system writes

## Where It Exists

- The System's dependency is managed by the `Dependency` property.
- Either in [SystemState]() object or [SystemBase]() class

## Features

- there is overhead in
  - calculating before executing the system
  - considering system's jobs for next system's depenedency handle

## Implicit Dependency Management

- When scheduling with [`Entities.ForEach`](unity-entities-api-systembase-entities-foreach) or `Job.WithCode`, system specify JobHandle stored in property `Dependency` as its dependencies
- Jobs scheduled in system are automatically combined **IN SEQUENCE** to the system's `Dependency` property

## Explicit Dependency Management

When scheduling job with [explicit dependencies](unity-jobs#job-dependency)(e.g. passing a `JobHandle` to `Schedule()`)

- The job won't combined to `Dependency` property
- The `Dependency` property must be manually set to ensure that dependency of later system(new created same type system) correct

For Instruction:


```cs
public class ExampleSystem : SystemBase
{
    protected override void OnUpdate()
    {
        JobHandle One = Entities.WithName("ForEach_Job_One").ForEach((ref AComponent c) => { /*...*/ })
            .ScheduleParallel(this.Dependency);
        JobHandle Two = Entities.WithName("ForEach_Job_Two").ForEach((ref AnotherComponent c) => { /*...*/ })
            .ScheduleParallel(this.Dependency);

        // Combine the dependencies of the two jobs 
        JobHandle intermediateDependencies = JobHandle.CombineDependencies(One, Two);

        NativeArray<int> result = new NativeArray<int>(1, Allocator.TempJob);

        // Explicitly scheduling jobs with dependencies
        JobHandle finalDependency = Job.WithName("Job_Three").WithDisposeOnCompletion(result).WithCode(() =>
            {
                result[0] = 1;
            })
            .Schedule(intermediateDependencies);

        // manually set the final dependency to the system's Dependency property
        this.Dependency = finalDependency;
    }
}
```

- JobHandle `One`, `Two` are jobs that not depend on each other
- JobHandle `One`, `Two` won't affect the system's `Dependency` property
- final job depends on the result of `One` and `Two`
- Manually Assign final jobhandle to `Dependency` property to ensure dependency can be propagated to the subsequent systems

