# Unity Shader - Keywords

## Declaration

[`#pragma`](unity-shader-preprocessor-directives.md#pragma) is used to declare shader keywords

## This Is A Keyword Set

- COLOR_RED
- COLOR_GREEN
- COLOR_BLUE

## 3 Keywords Types

Multi compile

`#pragma multi_compile COLOR_RED COLOR_GREEN COLOR_BLUE`

- compile [shader variants](unity-shader-terminology.md#shader-variant) for all keywords in the set declared by `multi_compile`
- VS [properties](unity-shader-object.md#properties) block, **MAYBE**
  - `multi_compile` is more suitable for configure visual quality settings
  - Properties block is more suitable for game play effect

Shader feature

`#pragma shader_feature _COLOR_RED _COLOR_GREEN _COLOR_BLUE`

- Also compile all keywords in the set
- At build time, only the keyword in use will be compiled

Dynamic branch

## Multi Compile Or Shader Feature How To Choose

- Do not need change their value from C# scripts at runtime, then `shader_feature`
- Or choose `multi_compile`

## Use Keyword

```c
#pragma multi_compile QUALITY_LOW QUALITY_MEDIUM QUALITY_HIGH
if defined(QUALITY_LOW)
{
    // low quality code
}
```
