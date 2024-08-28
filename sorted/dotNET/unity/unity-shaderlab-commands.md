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

Blend Equation

`finalValue = sourceFactor * sourceValue operation destinationFactor * destinationValue`

Command syntax

- `Blend [render target] state`
  - `Blend Off`: disable blending
- `Blend [render target] SrcFactor DstFactor` 
- `Blend [render target] SrcFactor DstFactor, SrcFactorA DstFactorA`: separate blend factors for color and alpha channels
  - `SrcFactorA` and `DstFactorA` is factor that separate alpha from RGBA

Instruction

- `state`: Off, 
- `render target`: from 0 to 7
- `***Factor`
  - One
  - Zero
  - SrcColor
  - SrcAlpha
  - SrcAlphaSaturate
  - DstColor
  - DstAlpha
  - OneMinusSrcColor: (1 - srcColor)
  - OneMinusSrcAlpha: (1 - srcAlpha)
  - OneMinusDstColor: (1 - dstColor)
  - OneMinusDstAlpha: (1 - dstAlpha)

Most Common Blend Combination

```sh
Blend SrcAlpha OneMinusSrcAlpha # Traditional transparency
Blend One OneMinusSrcAlpha # Premultiplied transparency
Blend One One # Additive blending
Blend OneMinusDstColor One # Soft Additive blending
Blend DstColor Zero # Multiplicative blending
Blend DstColor SrcColor # 2x Multiplicative blending
```

## BlendOp

- operation in the blending equation

## ColorMask

## Conservative 

## Cull

## Offset

## Stencil

## ZClip

## ZTest

## ZWrite

## UsePass

## GrabPass


