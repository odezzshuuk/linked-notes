# Unity - Shader Code

* [HLSLPROGRAM](#hlslprogram)
* [HLSLINCLUDE](#hlslinclude)
* [Preprocessor Directives](#preprocessor-directives)
* [HLSL Language](#hlsl-language)

## HLSLPROGRAM

- Code inside `HLSLPROGRAM` need to be written in [`Pass`] block

```c
Shader "Sort/Foo"
{
    SubShader
    {
        Pass
        {
            Name "PassOne"
            Tags { "LightMode" = "ForwardBase" }

            HLSLPROGRAM
                // vertex shader
            ENDHLSL
        }

    }
}
```

## HLSLINCLUDE

- Use to share common code in the same source file
- Code inside `HLSLINCLUDE` will be included in all [`HLSLPROGRAM`](#hlslprogram) blocks in the same source file
- Not neccessary to be write in [Pass block](unity-shaderlab.md#pass) 

```c
Shader "Sort/Foo"
{
    SubShader
    {
        HLSLINCLUDE
            // shader code i want to share
        ENDHLSL

        Pass
        {
            Name "PassOne"
            Tags { "LightMode" = "ForwardBase" }

        }

    }
}
```


## Preprocessor Directives

[Preprocessor Directives](unity-shader-preprocessor-directives.md)

## HLSL Language
