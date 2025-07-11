# Unity Entities - Query with IJobChunk

## What's This

- Its parallel iterating mechanism is similar to [`IJobFor`](unity-jobs-parallel-jobs#how-to)
  - but parallel by [chunk](unity-entities-archetype#archetypes-chunk)

## How To Write Execute Method

```cs
void Execute(
    in ArchetypeChunk chunk,
    int unfilteredChunkIndex,
    bool useEnabledMask,
    in v128 chunkEnabledMask)
{
}
```
