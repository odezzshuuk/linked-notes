# Unity Render Pipeline API - Struct TextureDesc

## What's This

- Used to describe a [texture resource](unity-scriptable-render-pipeline-render-graph.md#Resource-of-render-graph)

To get textureDesc, for instance:

- Pass `RenderGraph.GetTextureDesc` method a `TextureHandle` object

```c
public override void RecordRenderGraph(RenderGraph renderGraph, ContextContainer frameData) {
    // ...

    // cameraData.cameraTarget is a TextureHandle object 
    TextureDesc desc = renderGraph.GetTextureDesc(cameraData.cameraTarget);
}
```
