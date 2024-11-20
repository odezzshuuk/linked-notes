# Unity - Shader

> here is the [webgl shader](webgl-shader.md)

* [What's For](#what's-for)
* [When Talking About Shader](#when-talking-about-shader)
* [Features](#features)
* [Best Practice](#best-practice)
* [HLSL Language](#hlsl-language)
* [ShaderLab](#shaderlab)
* [Data Flow](#data-flow)
* [Shader Types](#shader-types)
* [Shader Object](#shader-object)
* [Shader Variant](#shader-variant)

## What's For

- Use shader object with materials to determine the appearance of scene

Explaination of how shader effect what material looks

- For Physically Based Rendering (PBR), material is appearence changes as the light changes
- For non-PBR, for example toon shader, which will make 3D scene looks like 2D cartoons

## When Talking About Shader

[Terminology](unity-shader-terminology.md)

## Features

- There are multiple [subshader]() in [shader object](), which Shader would be used depend on [render pipeline](unity-render-pipeline.md) 

## Best Practice

[Best Pracctice](unity-shader-best-practice.md)

## HLSL

[HLSL Language](unity-hlsl-language.md)

[Compilation](unity-shader-compilation.md)

[HLSL in unity](unity-hlsl-in-unity.md)

## ShaderLab

[ShaderLab](unity-shaderlab.md)

## Data Flow

Most common shader process is [vertex-fragment stage](unity-shader-terminology.md#shader-stage) process

Data Flow Direction: Vertex -> Fragment

Explaination By Code

```c
v2f vert (appdata_t v)
{
    v2f o;
    o.pos = UnityObjectToClipPos(v.vertex);
    return o;
}

fixed4 frag (v2f i) : SV_Target // i is the input from vertex shader
{
    // ...
}
```

## Shader Types

[built-in render pipeline](unity-render-pipeline.md#supported-render-pipeline) has following shader types

- [Vertex-fragment](unity-vertex-fragment-shader.md)
- [Surface shader](unity-surface-shader.md)
- Compute Shaders

## Shader Object

[Shader Object](unity-shader-object.md)

## Shader Variant
