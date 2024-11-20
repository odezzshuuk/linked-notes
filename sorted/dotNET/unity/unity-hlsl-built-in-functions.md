# Unity HLSL - Built-in Functions

* [clamp](#clamp)
* [step](#step)
* [smoothstep](#smoothstep)
* [lerp](#lerp)
* [tex2D](#tex2d)
* [tex2Dproj](#tex2dproj)

## clamp

`float clamp(x, min, max)`

- return value range `[min, max]`

## step

`float step(y, x)`

- return value range 0 or 1

## smoothstep

`float smoothstep(min, max, x)`

- return value range `[0, 1]`

## lerp

`float lerp(x, y, s)`

- return value range `[x, y]`

## tex2D

`float4 tex2D(sampler2D s, float2 t)`

Paramater

- `sampler2D s`
- `float2 s`
  - mostly, it's texture [uv coordinate](computer-graphics-terminology.md#uv-coordinates)

Return Value

- `float4`: texture data on the coordinate `t`. Typically, it's a **color**

Use case

- In general, when you want to sample a texture based on uv without applying any perspective correction
- Such as sampling a texture assigned on a 3D model, or a texture on a 2D plane

## tex2Dproj

`float4 tex2Dproj(sampler2D s, float4 t)`

Description

- Samples a 2D texture using a [projective divide](computer-graphics-terminology.md#perspective-division)
- `t` is divided by `t.w` before the texture lookup

parameter

- `sample2D s`: [sampler state](unity-hlsl-data-types.md#sampler)
- `float4 t`: A coordinates in the

**Return**: 

- texture data on the projected coordinate `t`. Typically, it's a **color**

