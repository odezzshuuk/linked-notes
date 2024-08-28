# Unity - ShaderLab

* [What It Is](#what-it-is)
* [ShaderLab Syntax](#shaderlab-syntax)
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

- Properties that can be adjusted in the inspector
- Can be get or set in c# script with `material.GetColor("_Color")` or `material.SetColor("_Color", color)`

Property Declaration

`[optional: attribute] name("display name in inspector", type name) = default value`

```sl
Properties
{
    _Color ("Main Color", Color) = (1,1,1,1)
}
```

- `_Color`: the name used in c# script, for example `material.GetColor("_Color")` or `material.SetColor("_Color", color)`
- `Main Color`: Text displayed in inspector
- `Color`: Type of the property
- `"(1, 1, 1 ,1)"`: Default value

## SubShader

[Subshader](unity-subshader.md)

how unity select the subshader

- ...

## Pass

Inside pass

1. Name
2. Tags for pass, like subshader
3. [Shaderlab commands]
4. [Shader code](unity-shader-code.md)
5. PackageRequirements

```sl
Pass
{
    Name "PassName"
    Tags { "TagKey" = "TagValue" }

    // ShaderLab commands
    Cull Back
    ZWrite On
    ZTest LEqual

    // Shader code
    CGPROGRAM
    #pragma vertex vert
    #pragma fragment frag

    struct appdata_t
    {
        float4 vertex : POSITION;
    };

    struct v2f
    {
        float4 pos : SV_POSITION;
    };

    v2f vert (appdata_t v)
    {
        v2f o;
        o.pos = UnityObjectToClipPos(v.vertex);
        return o;
    }

    half4 frag (v2f i) : SV_Target
    {
        return half4(1, 0, 0, 1); // red color
    }
    ENDCG
}
```

## Commands

[Commands](unity-shaderlab-commands.md)

## Shader Code

[Shader Code](unity-shader-code.md)

## Shader Keywords

[Shader Keywords](unity-shader-keywords.md)

## Package Requirements

[Package Requirements](unity-shader-package-requirements.md)



