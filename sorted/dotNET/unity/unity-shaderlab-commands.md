# Unity - ShaderLab Commands

## What's ShaderLab Commands For

3 purposes

- For setting the render state on the GPU
- Commands that create a [pass](#pass) with a specific purpose
- Legacy commands for "fixed function style"

setting render state commands

- [AlphaToMask](#alphatomask)
- [Blend](#blend):
- [BlendOp](#blendop): blend operation, such as add, subtract, reverse subtract, minimum, maximum...
- [ColorMask](#colormask)
- [Conservative](#conservative)
- [Cull](#cull)
- [Offset](#offset)
- [Stencil](#stencil)
- [ZClip](#zclip)
- [ZTest](#ztest)
- [ZWrite](#zwrite)

Pass Commands

- [UsePass](#usepass)
- [GrabPass](#grabpass)

## AlphaToMask

## Blend

[Blend](unity-shaderlab-commands-blend.md)

## BlendOp

- operation in the blending equation

## ColorMask

## Conservative

## Cull

[Cull](unity-shaderlab-commands-cull.md)

## Offset

## Stencil

[Stencil](unity-shaderlab-commands-stencil.md)

## ZClip

## ZTest

Z represents the depth

- Disabled
- Never
- Less
- Equal
- LEqual: means less or equal, **default value**
- Greater: Draw geometry that is behind existing geometry
- NotEqual
- GEqual
- Always

## ZWrite

- set whether [depth buffer](unity-shader-terminology.md#depth-buffer) are updated during rendering
- `ZWrite On` or `ZWrite Off`

## UsePass

What's For

- Insert a pass from another shader object into the current pass
- For Reusing shader code

`UsePass "<ShaderName>/<PassName>"`

## GrabPass


