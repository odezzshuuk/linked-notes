# Unity - Shader Terminology

* [Shader Program](#shader-program)
* [Shader Class](#shader-class)
* [Shader Object](#shader-object)
* [ShaderLab](#shaderlab)
* [Shader Graph](#shader-graph)
* [Shader Asset](#shader-asset)
* [Shader Graph Asset](#shader-graph-asset)
* [Shader Variant](#shader-variant)
* [Shader Variant Collection](#shader-variant-collection)
* [Shader Keywords](#shader-keywords)
* [Shader Stage](#shader-stage)
* [Vertex Shader](#vertex-shader)
* [Stencil Buffer](#stencil-buffer)
* [Depth Buffer](#depth-buffer)

## Shader Program

- A program that runs on a GPU

## Shader Class

A class used to write scripts for shader

- Mostly used **just** to check whether a shader is supported on hardware
- Which means shader class can't control the details of the shader

## Shader Object

what's this

- An instance of [`Shader`]() class

what's inside

- Information about the shader
- An optional fallback Shader object
- One or more SubShaders

2 ways for create Shader Object

> it's NOT created by [unity script](unity-script.md)

- write shader code with .shader extension
- use [Shader Graph](#shader-graph)

## ShaderLab

- A declarative language for writing structure shaders

## Shader Graph

A tool for creating shaders without writing code

## Shader Asset

A file with the .shader extension

## Shader Graph Asset

A file define a shader object

## Shader Variant

- One shader source file compiled into One Shader Program
- One shader program can have multiple variants for different conditions
- Which variant is used at runtime is configured by [shader keywords](#shader-keywords)

For example there are keywords sets, Set One

- `COLOR_RED`
- `COLOR_GREEN`
- `COLOR_BLUE`

Set Two

- `QUALITY_LOW`
- `QUALITY_MEDIUM`
- `QUALITY_HIGH`
- `QUALITY_ULTRA`

Then there are 12 variants

## Shader Variant Collection

- To ensure [shader variants](#shader-variant) that are required at runtime but not referenced in a scene are not excluded from the **build**

## Shader Keywords

- Use [conditional behavior]() to organize shader code

## Shader Stage

- specific step in the graphics rendering pipeline

Common Stages

1. [Vertex Shader](#vertex-shader)
2. Tesselation Shader(Hull and Domain Shaders)
3. Geometry Shader
4. Fragment Shader
5. Compute Shader

## Vertex-fragement Shader

- Most common shader process
- With two functions, vertex and fragment

Vertex-fragment shader function may call like this

> **Fragment shader will use the output of the vertex shader**

1. DATA type
2. Function signature
3. Executing the function

```c
// data type declaration
struct appdata {
    float4 vertex : POSITION;
    float4 color : COLOR;
};
struct v2f {
    float4 vertex : SV_POSITION;
    float4 color : COLOR;
};

// function signature
v2f vert(appdata v) { }
float4 frag(v2f i) : SV_Target { return i.color; }
void main(in appdata data, out float4 fragColor) {}

// main function call
appdata app_data;
main(app_data, frag(vert(app_data)));
```

## Vertex Shader

- Must output vertex position in homogeneous clip space
- Optional to output other data, such as vertex color, vertex lightning, texture coordinates, etc.

```c

```

## Stencil Buffer

- [stencil command](unity-shaderlab-commands-stencil.md#stencil-buffer)

## Depth Buffer





