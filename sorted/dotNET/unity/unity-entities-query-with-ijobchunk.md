# Unity Entities - Query with IJobChunk

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
