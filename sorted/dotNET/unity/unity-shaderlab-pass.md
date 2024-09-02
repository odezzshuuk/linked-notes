# Unity Shaderlab - Pass

## What Is This

- Fundamental element

## Features

- If A subshader is executed, **all passes** in the subshader are executed in sequence by **written order**
- Each pass is a [complete shader process](unity-shader-terminology.md#shader-stage)

## Inside pass

1. Name
2. Tags for pass, like subshader
3. [Shaderlab commands](unity-shaderlab-commands.md)
4. [Shader code](unity-shader-code.md)
5. PackageRequirements

## Multiple Passes



## Take A Look

```c
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
