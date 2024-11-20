# Unity HLSL - Semantic

## What Is Semantic

- String that attached to a variable
- Indicate that variable is passed between [shader stages](unity-shader-teminology.md#shader-stage)
- Semantic is **REQUIRED** for shader stages function's parameter and return value
- Semantic for Normal function is **OPTIONAL**

## Why Semantic

-  Inform GPU how to use the variable, such as position, color, etc.

## Where To Use

- After a structure member
- After an argument in a function's input argument list
- After the function's input argument list

- Used as parameter or return value of shader stage function
- Parameter and return value correspond to input and output of the shader stage
- Both wrapped in a struct or directly is allowed

> [Detail of available semantics of each shader stage](#catagories)

## Take A Look

Wrapped in a struct

```c
struct VertexOutput
{
  float3 position : POSITION;  // : POSITION is the semantic
  float2 uv : TEXCOORD0;  // : TEXCOORD0 is the semantic
}
struct VertexInput
{
  float4 vertex : POSITION;  // : POSITION is the semantic
  float2 uv : TEXCOORD0;  // : TEXCOORD0 is the semantic
}

VertexOutput verttex(VertexInput input)
{
  VertexOutput output;
  output.position = UnityObjectToClipPos(input.vertex);
  output.uv = input.uv;
  return output;
}
```

Directly

```c
struct v2f {
  float2 uv : TEXCOORD0;
  float4 pos : SV_POSITION;
}

v2f vertex_shader(
  float4 vertex : POSITION,
  float2 uv : TEXCOORD0
  )
{
  v2f o;
  o.pos = UnityObjectToClipPos(vertex);
  o.uv = uv;
  return o;
}

fixed4 fragment_shader(v2f i) : SV_Target  // : SV_Target is output semantic
{
  return tex2D(_MainTex, i.uv);
}
```

## Catagories

Vertex Shader Semantic

- Input semantics
  - `BINORMAL[n]`
  - `BLENDINDICES[n]`
  - `BLENDWEIGHT[n]`
  - `COLOR[n]`
  - `NORMAL[n]`
  - `POSITION[n]`
  - ...
- Output semantics
  - `COLOR[n]`
  - `FOG`
  - `POSITION[n]`
  - ...

Fragment(Pixel) Shader Semantic

- Input semantics
  - `COLOR[n]`
  - `TEXCOORD[n]`: 
    - **One material** can have **multiple** texture coordinates
    - `n` refers to the index/slot/channel of the texture coordinate
  - ...
- Output semantics
  - `COLOR[n]`
  - `DEPTH`

System-Value Semantic(Direct3D Only)
