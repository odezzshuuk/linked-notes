# HLSL In Unity

## Using Sampler State

Coupled textures and samplers

```c
sampler2D _MainTex;
half4 color = tex2D(_MainTex, uv);
```

Separate textures and samplers

```c
Texture2D _MainTex;
Texture2D _SecondTex;
Texture2D _ThirdTex;
SamplerState sampler_MainTex;

// reuse sampler state
half4 color = _MainTex.Sample(sampler_MainTex, uv);
color += _SecondTex.Sample(sampler_MainTex, uv);
color += _ThirdTex.Sample(sampler_MainTex, uv);
```

- Use name convention `sampler_` + <texture name> to define sampler state
- It is allowed to use the same sampler state for multiple textures

Use inline sampler state to config [texture filtering mode](unity-shader-terminology.md#texture-filter-mode)

> not supproted on some platforms

```c
Texture2D _MainTex;
SamplerState my_point_clamp_sampler;
half4 color = _MainTex.Sample(my_point_clamp_sampler, uv);
```

## Helper Functions

`float4 ComputeScreenPos(float4 clipPos)`

- Map [clip space](computer-graphics-terminology.md#clip-space) to [screen space](computer-graphics-terminology.md#screen-space)
- return value: `float4` screen position

## Built-in Variables

`<texture_name>_TexelSize`

- `<texture_name>`: name of the texture, such as `_MainTex`, `_CameraDepthTexture`, etc.
- variable of [texture element](computer-graphics-terminology.md) size

