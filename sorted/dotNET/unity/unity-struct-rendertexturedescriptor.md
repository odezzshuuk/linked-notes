# Unity Render Pipeline API - Struct RenderTextureDescriptor

## What's This

- Contains information about a [render texture](unity-shader-terminology.md#render-texture)
- **Avoid** using constructor to create a `RenderTextureDescriptor` object as it dose not initialize some flags with the recommended values
- Inherit from `TextureDesc`

RenderTextureDescriptor mostly get from `UniversalCameraData`

```c
public override void RecordRenderGraph(RenderGraph renderGraph, ContextContainer frameData) {
    // ...

    // cameraData.cameraTarget is a TextureHandle object 
    RenderTextureDescriptor desc = caremaData.cameraTargetDescriptor;
}
```
