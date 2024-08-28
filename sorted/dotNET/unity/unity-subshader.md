# Unity - Subshader

## Features

- separate shader object into different parts for compatibility
- One or more [pass objects](#pass)

```sl
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

- include predefined tags and user-defined tags

### Predefined tags:

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

details:

- `"RenderPipeline"="[name]"`: whether subshader is compatible with the universal render pipeline,
  - available values are `UniversalRenderPipeline` and `HDRenderPipeline`, other names represent that subshader is not compatible with the render pipeline
- `"Queue"="[name]"`: tell unity which render queue to use
  - available values are `Background`, `Geometry`, `AlphaTest`, `Transparent`, `Overlay`
  - `Queue="Transparent + 1"`: give offset after the named queue
    - In C# script
      - `Shader.renderQueue`: get the queue tag of active subshader
      - `material.renderQueue`: set the queue tag of the material
- `"RenderType"="[name]"`:
  - user-defined tags: can be accessed from c# script, for example `material.GetTag("tagname")`

