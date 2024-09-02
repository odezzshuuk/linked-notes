# Unity ShaderLab Commands - Blend

## What's for

- combines the output of the **fragment shader**

## Blend Equation

`finalValue = sourceFactor * sourceValue operation destinationFactor * destinationValue`

## Command syntax

- `Blend [render target] state`
  - `Blend Off`: disable blending
- `Blend [render target] SrcFactor DstFactor`
- `Blend [render target] SrcFactor DstFactor, SrcFactorA DstFactorA`: separate blend factors for color and alpha channels
  - `SrcFactorA` and `DstFactorA` is factor that separate alpha from RGBA

## Instruction

- `state`: Off, On
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
