# Unity ShaderLab Commands - Stencil

## What's for

- Configure the [stencil test](#stencil-test)
- And what to write to the [stencil buffer](#stencil-buffer)
- Use stencil buffer as a mask to control what to draw and what to discard

## Features

- Can be used in [pass](unity-shaderlab.md#pass) block or [subshader](unity-shaderlab.md#subshader) block

## Most use case

To create one shader object that masks out areas of the screen that other shader objects cannot draw to, To do this:

- configure the first shader object to always pass the stencil test and write to the stencil buffer
- configure the others to perform a stencil test and not write to the stencil buffer

## Stencil Buffer

- Stencil buffer stores an **8-bit integer value**(0-255)
- for **Each Pixel** in the frame buffer

## Stencil Test

- GPU compare the current value in the stencil buffer with the given value
- If stencil test passes, GPU perform depth test
- If stencil test fails, GPU skip the rest of the rendering process **for that pixel**

## Test equation

`(ref & readMask) comparisonOperation (stencilBufferValue & readMask)`

## Signature

```
Stencil
{
    Ref <ref>
    ReadMask <readMask>
    WriteMask <writeMask>
    Comp <comparisonOperation>
    Pass <passOperation>
    Fail <failOperation>
    ZFail <zFailOperation>
    CompBack <comparisonOperationBack>
    PassBack <passOperationBack>
    FailBack <failOperationBack>
    ZFailBack <zFailOperationBack>
    CompFront <comparisonOperationFront>
    PassFront <passOperationFront>
    FailFront <failOperationFront>
    ZFailFront <zFailOperationFront>
}
```

- `ref`: The value that GPU compares
- `readMask`
  - Value Range: 0 ~ 255(b11111111)
  - used as readMask in [test equation](#test-equation)
- `writeMask`:
  - Control what value can be written to the stencil buffer

