# Unity HLSL - Data Types

* [float](#float)
* [Vector](#vector)
* [Matrix](#matrix)
* [Sampler](#sampler)
* [SamplerState](#samplerstate)

## float

## Vector

Declaration

```c
float3 a = {0.2f, 0.3f, 0.4f};
float3 b = float3(0.2f, 0.3f, 0.4f);
```

Components(members)

- vector contains up to four components
  - position : x, y, z, w
  - color set: r, g, b, a

```c
float4 pos = float4(0.2f, 0.3f, 0.4f, 1.0f);
pos.z; // 0.4f
pos.b; // 0.4f
```

swizzling

- Can be accessed one or more, but **cannot** mixed
- Read components by any order
- Can be read multiple times
- Multiple times writing is not allowed

```c
float4 pos = float4(0.2f, 0.3f, 0.4f, 1.0f);
float2 temp;

temp = pos.xy;  // valid
temp = pos.rg;  // valid
temp = pos.xg;  // invalid

temp = pos.xz;  // (0.2f, 0.4f)
temp = pos.zx;  // (0.4f, 0.2f)

temp = pos.xx; // (0.2f, 0.2f)

// write multiple times to same component is not allowed
temp.xx = pos.xy; // in valid
```

## Matrix

Definition

```c
int1x1 m;
double2x2 m = {
    1.0, 2.0, // row 1
    3.0, 4.0  // row 2
};
double2x3 m = {
    1.0, 2.0, 3.0, // row 1
    4.0, 5.0, 6.0  // row 2
};
matrix <float, 2, 3> m = {
    1.0f, 2.0f, 3.0f, // row 1
    4.0f, 5.0f, 6.0f  // row 2
};
```

Accessing

- zero-based index
  - _m00, _m01, _m02, _m03
  - _m10, _m11, _m12, _m13
  - _m20, _m21, _m22, _m23
  - _m30, _m31, _m32, _m33
- one-based index
  - _11, _12, _13, _14
  - _21, _22, _23, _24
  - _31, _32, _33, _34
  - _41, _42, _43, _44
- index(mutiple components read in not allowed)
  - `[0][0], [0][1], [0][2], [0][3]`
  - `[1][0], [1][1], [1][2], [1][3]`
  - `[2][0], [2][1], [2][2], [2][3]`
  - `[3][0], [3][1], [3][2], [3][3]`


```c
float2x2 m = {
    1.0f, 2.0f,
    3.0f, 4.0f
};
float2 temp;
temp = m._m00_m11; 
temp = m._11_22;
```

## Sampler

> Primarily used in Direct3D 9 and earlier

What It Is

Definition

```hlsl
SamplerType <Name>[index]
{
    Filter = Value;
    AddressU = Value;
    AddressV = Value;
    AddressW = Value;
    MipFilter = Value;
    MaxAnisotropy = Value;
    ComparisonFunc = Value;
    BorderColor = Value;
    MinLOD = Value;
    MaxLOD = Value;
    MipLODBias = Value;
    ElementIndex = Value;
    ComparisonFunc = Value;
    FilterMode = Value;
    AddressMode = Value;
    MipMapMode = Value;
    MaxAnisotropy = Value;
    BorderColor = Value;
    MinLOD = Value;
    MaxLOD = Value;
    MipLODBias = Value;
    ElementIndex = Value;
}
```

- `SamplerType` is one of the following
  - `sampler1D`
  - `sampler2D`
  - `sampler3D`
  - `samplerCUBE`
  - `sampler2DArray`
  - `sampler2DMS`
  - `sampler2DMSArray`
  - `samplerState`
  - `SamplerComparisonState`
- `Name` is variable name
- `index`: Direct3D 10 and later only, optional, represent array size
- `Filter, AddressU, ...`: they are called states

## SamplerState

> Introduced in Direct3D 10

Why SamplerState

- Decoupled samplers and textures

Features

- Modern and flexible

