# Unity - Subshader

## Features

- Only one of subshaders in shader block is executed at a time
- Separate shader object into different parts for compatibility
- Include One or more [pass objects](#pass)

```c
{
    SubShader
    {
        LOD 200
        Tags { "name1"="value1", "name2" = "value2" }
        Pass
        {

        }
    }
    SubShader
    {
        LOD 100
        Tags { "name1"="value1", "name2" = "value2" }
        Pass
        {

        }
    }

}
```

## LOD

- Level of Detail, the higher the number, the more detailed the shader.

## Tag

- Include predefined tags and user-defined tags

Predefined tags

- unity use them to determine how and when to use which shader

predefined tags:

|                      | description                                                             |
| -------------------- | ----------------------------------------------------------------------- |
| RenderPipeline       |                                                                         |
| Queue                |                                                                         |
| RenderType           |                                                                         |
| ForceNoShadowCasting |                                                                         |
| DisableBatching      |                                                                         |
| IgnoreProjector      |                                                                         |
| PreviewType          | how to display a material that use this subshader in material inspector |
| CanUseSpriteAtlas    |                                                                         |

## Predefined Tags

`"RenderPipeline"="[name]"`: whether subshader is compatible with the universal render pipeline,

- Available values are `UniversalRenderPipeline` and `HDRenderPipeline`, other names represent that subshader is not compatible with the render pipeline

`"Queue"="[name]"`: tell unity which render queue to use

- Available values are `Background`, `Geometry`, `AlphaTest`, `Transparent`, `Overlay`
- `Queue="Transparent + 1"`: give offset after the named queue
  - In C# script
    - `Shader.renderQueue`: get the queue tag of active subshader
    - `material.renderQueue`: set the queue tag of the material

`"RenderType"="[name]"`:

- User-defined tags: can be accessed from c# script, for example `material.GetTag("tagname")`
- Available values
  - `Opaque`: default value
  - `Transparent`:
  - `Cutout`:
  - `Fade`:

`"ForceNoShadowCasting"="True"`: disable shadow casting

`"DisableBatching"="True"`: disable batching

`"IgnoreProjector"="True"`: ignore projector

`"PreviewType"="[name]"`: how to display a material that use this subshader in material inspector

## how unity select the subshader

- ...
