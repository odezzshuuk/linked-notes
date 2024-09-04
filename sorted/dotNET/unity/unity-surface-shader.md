# Unity - Surface Shader

## Features

- interact with light
- Not support in [URP](unity-universal-render-pipeline.md)

## How to write

Caveat:

- MUST placed in [Subshader] block, not in pass.

[pragma] Directive

- `#pragma surface surfName lightModel [optionalparams]`

Surface output structure

- looks like

```c
struct SurfaceOutput {
    fixed3 Albedo;
    fixed3 Normal;
    fixed3 Emission;
    fixed Specular;
    fixed Gloss;
    fixed Alpha;
};
```

Surface function


