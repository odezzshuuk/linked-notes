# Unity - Render Graph

* [What's This](#what's-this)
* [What's Benefit](#what's-benefit)
* [3 steps of render graph system process ](#3-steps-of-render-graph-system-process-)
* [Resource Of Render Graph](#resource-of-render-graph)
* [Two Types Of Resources](#two-types-of-resources)
* [Create Resource](#create-resource)
* [RenderGraphBuilder](#rendergraphbuilder)

## What's This

- A high-level representation of the render [passes](unity-shaderlab-pass.md)
- Explicitly indicate how the render pass use the resources(materials, textures, etc)

## What's Benefit

- Efficient memory management
- Automatic synchronization point generation
- Maintainability

## 3 steps of render graph system process 

- **Setup**: setup for all render passes
- **Compilation**: 
- **Execution**
  - Executing in declaration order
  - [Create And Release Resources](csharp-idisposable.md#using-statement)
    - Before each render process, create the **resources**
    - After each render process, release the **resources**

## Resource Of Render Graph

When talking about the resource of render graph, we are talking about the `TextureHandle` and `RTHandle`

- Texture that can be mapped onto 3D surface, such as Normal Map, Albedo Map, Color Map
- [Render texture](unity-shader-terminology.md#render-texture)
- Various buffers, such as Depth Buffer, Stencil Buffer
- Render target, where the output of the render pass is written to
- Shaders

Accessing Resource from c# aspect

- [`TextureHandle`]() for texture resource
- [`RTHandle`]() for render texture resource
- `BufferHandle` for buffer resource

## Two Types Of Resources

1. Internal resources

- Cannot access outside the render graph
- Cannot be pass from one to another render pass

2. Imported resources

- Typical example: Camera Color Buffer

## Create Resource

- Resource is never created directly
- Resource is **managed by the render graph system**

> More clearly speaking, Resource is allocated and disposed by RenderGraph instance

```c
// Create a texture
public TextureHandle RenderGraph.CreateTexture(in TextureDesc desc);
public Texturehandle RenderGraph.CreateComputeBuffer(in ComputeBufferDesc desc);

// Import a texture
public TextureHandle RenderGraph.ImportTexture(RTHandle rt);
public TextureHandle RenderGraph.ImportBackbuffer(RenderTargetIndentifier rt);
public BufferHandle RenderGraph.ImportBuffer(Computebuffer, computerBuffer);
```

> [`RenderGraphBuilder`](#rendergraphbuilder) has similar resource create api

## RenderGraphBuilder

What It Is

- The entry point to build the information relating to the render pass

What It Can Do

- Declaring resource usage
  - Declaring whether the render pass needs read and/or write access to the [resources](#resource-of-render-graph)
- Declaring rendering function
- Creating internel resource
  - Create internal resource use the **same parameters** as the corresponding function in `RenderGraph` API

Work with [`using`](csharp-idisposable.md#using-statment) statement

```c
using (var builder = renderGraph.AddRenderPass<RenderPassData>("Render Pass", out var passData)) { }
```

- At the end of the `using` scope, the render pass is added to the render graph

