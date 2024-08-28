# Unity - Shader

> here is the [webgl shader](webgl-shader.md)

* [What's For](#what's-for)
* [Features](#features)
* [When Talking About Shader](#when-talking-about-shader)
* [ShaderLab](#shaderlab)
* [Workflow](#workflow)
* [Shader Types](#shader-types)
* [Shader Object](#shader-object)
* [Shader Variant](#shader-variant)

## What's For

- Use shader object with materials to determine the appearance of scene

Explaination of how shader effect what material looks

- For Physically Based Rendering (PBR), material is appearence changes as the light changes
- For non-PBR, for example toon shader, which will make 3D scene looks like 2D cartoons

## Features

- There are multiple [subshader]() in [shader object](), which Shader would be used depend on [render pipeline](unity-render-pipeline.md) 

## HLSL Language

[HLSL Language](unity-hlsl-language.md)

## When Talking About Shader

[Terminology](unity-shader-terminology.md)

[Compilation](unity-shader-compilation.md)

## ShaderLab

[ShaderLab](unity-shaderlab.md)

## Workflow

## Shader Types

- shader graph: visual shader editor
- Unlit shader: do not interact with light
- Image Effect Shader: [post processing](unity-post-processing.md) effect
- Compute Shaders

## Shader Object

[Shader Object](unity-shader-object.md)

## Shader Variant
