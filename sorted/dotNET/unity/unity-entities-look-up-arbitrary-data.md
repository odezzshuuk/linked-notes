# Unity Entities - Look Up Arbitrary Data

## What's This

> Similar function as [GetComponent() and TryGetComponent()](unity-monobehaviour.md) method in MonoBehaviour, but for Entities.

- A [native container](unity-jobs-nativecontainer.md) 
- Providing access to all data of components of type T

## Usage

```cs
public partial class ExampleJob: IJobEntity 
{
    public ComponentLookup<LocalToWorld> EntityPositionsLookup;
    public float deltaTime;

    public void Execute(ref LocalTransform transform, in Target target)
    {
        Entity targetEntity = target.entity;
        LocalToWorld ltw = EntityPositionsLookup[targetEntity];  // access by entity index

        if (EntityPositionsLookup.TryGetComponent(targetEntity, out LocalToWorld entityPosition))  // access LocalToWorld component after check
        {
            // Update translation to move the chasing entity toward the target
            float3 targetPosition = entityPosition.Position;
            float3 chaserPosition = transform.Position;

            float3 displacement = targetPosition - chaserPosition;
            transform.Position = chaserPosition + displacement * deltaTime;
        }
    }
}
```

Former code shows the use cases

- Access `LocalToWorld` component data by entity index
- Use `TryGetComponent()` to check if the component exists before accessing it

## The Way You Look Up Is Depends

How to look up is depend on following situations:

- For look up in `Entities.ForEach()` or `Job.WithCode()`, use `SystemAPI.GetComponent<T>(Entity)`
- For BufferLookup, ...
- Look up in Job

## Look Up In Job

1. Declare a field type `ComponentLookup<T>` or `BufferLookup<T>` in the job struct
2. Set the field value before job schedule

```cs
[RequireMatchingQueriesForUpdate]
public partial class MoveTowardsEntitySystem : SystemBase
{
    private EntityQuery query;

    [BurstCompile]
    private partial struct MoveTowardsJob : IJobEntity
    {

        // Read-only data stored (potentially) in other chunks
        [ReadOnly]
        public ComponentLookup<LocalToWorld> EntityPositions;
        public float deltaTime;

        public void Execute(ref LocalTransform transform, in Target target, in LocalToWorld entityPosition)
        {
            Entity targetEntity = target.entity;

            // Update translation to move the chasing entity toward the target
            float3 targetPosition = entityPosition.Position;
            float3 chaserPosition = transform.Position;

            float3 displacement = targetPosition - chaserPosition;
            transform.Position = chaserPosition + displacement * deltaTime;
        }
    }

    protected override void OnCreate()
    {
        // Select all entities that have Translation and Target Component
        query = this.GetEntityQuery
            (
                typeof(LocalTransform),
                ComponentType.ReadOnly<Target>()
            );
    }

    protected override void OnUpdate()
    {
        // Create the job
        var job = new MoveTowardsJob();

        // Set the component data lookup field
        job.EntityPositions = GetComponentLookup<LocalToWorld>(true);
        job.deltaTime = SystemAPI.Time.DeltaTime;

        // Schedule the job using Dependency property
        Dependency = job.ScheduleParallel(query, Dependency);
    }
}
```
