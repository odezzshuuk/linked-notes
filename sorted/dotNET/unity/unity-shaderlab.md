# Unity - ShaderLab

* [What It Is](#what-it-is)
* [What's In .shader](#what's-in-.shader)
* [Shader Block Structure](#shader-block-structure)
* [Shader Declaration](#shader-declaration)
* [Properties](#properties)
* [SubShader](#subshader)
* [Pass](#pass)
* [Commands](#commands)
* [Shader Code](#shader-code)
* [Shader Keywords](#shader-keywords)
* [Package Requirements](#package-requirements)

## What It Is

- ShaderLab is a **Language** to create [shader object](unity-shader-object.md) in unity
- Write shader code in `.shader` file

## What's In .shader

- [Shader Main Parts](#shader-main-parts)
- [Subshader](#subshader)
- [Pass](#pass)
- [Shader Variants](#shader-variants)

## Shader Block Structure

Shader

- [Properties]
- [SubShader](#subshader)
- Pass
- FallBack

```sl
Shader "ShaderName/YourShader"
{
    Properties  // Optional
    {
        _Color ("Main Color", Color) = (1,1,1,1)
    }
    SubShader
    {
        // ...
        Pass
        {

        }
    }
    FallBack "Diffuse"  // Optional
}
```

## Shader Declaration

- Shader `ShaderCategory/ShaderName`

```c
Shader "MyShader/MyShader"
{
    // information about itself, such as name
    // An optional fallback shader object, unity will use if this one fails
    // One or more subshader objects
}
```

## Properties

[Properties](unity-shaderlab-properties.md)

## SubShader

[Subshader](unity-shaderlab-subshader.md)

## Pass

[Pass](unity-shaderlab-pass.md)

## Commands

[Commands](unity-shaderlab-commands.md)

## Shader Code

[Shader Code](unity-shader-code.md)

## Shader Keywords

[Shader Keywords](unity-shader-keywords.md)

## Package Requirements

[Package Requirements](unity-shader-package-requirements.md)



