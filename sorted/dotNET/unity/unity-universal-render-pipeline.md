# Unity - Universal Render Pipeline

* [What It Is](#what-it-is)
* [What's For](#what's-for)
* [Mechanism](#mechanism)
* [Asset References](#asset-references)
  * [Universal Render Pipeline Asset](#universal-render-pipeline-asset)
  * [Universal Renderer Asset](#universal-renderer-asset)
  * [Render Feature And Render Object](#render-feature-and-render-object)
  * [Volume Component](#volume-component)
* [Scriptable Render Pipeline](#scriptable-render-pipeline)
* [Shaders Provided by URP](#shaders-provided-by-urp)
* [Lit Shader](#lit-shader)

## What It Is

- Prebuilt Scriptable Render Pipeline

## What's For

- quick and easy create optimized graphics across a range of platforms

## Mechanism

## Asset References

### Universal Render Pipeline Asset

- Hold a member `Renderer List` member that made up of A list of [Renderer Assets](#universal-renderer-asset)

### Universal Renderer Asset

- Hold a member `Renderer Features` that made up of A list of [Render Feature Assets](#render-feature-and-render-object)

### Render Feature And Render Object

### Volume Component

## Scriptable Render Pipeline

[Scriptable Render Pipeline](unity-scriptable-render-pipeline.md)

## Shaders Provided by URP

- Lit: Suitable for most real world materials
- Complex Lit: For simulating advance materials that require more complex lightning evaluation
- Simple Lit
- Baked Lit
- Unlit
- Terrain Lit
- Particles Lit
- Particles Simple Lit
- Particles Unlit
- SpeedTree
- Decal
- Autodesk Interactive
- Autodesk Interactive Transparent
- Autodesk Interactive Masked

## Lit Shader

Properties

- `Workflow Mode`
  - workflow that fits your Textures, either Metallic and Specular.
  - refers to [built-in standard shader](unity-shader-object.md#standard-shader)

