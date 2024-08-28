# Unity Shader - Preprocessor Directives

* [What's For](#whats-for)
* [`#include`](#include)
* [`#include_with_pragma`](#include_with_pragma)
* [`#pragma`](#pragma)
  * [Shader Stages](#shader-stages)
  * [Shader variants and keywords](#shader-variants-and-keywords)


## What's For

- configure the preprocessor

## `#include`

- to tell instruct compiler to include the content of another HLSL file

## `#include_with_pragma`

- Extension of `#include` to include `#pragma` in the include file

## `#pragma`

> [pragma in c/c++](c-preprocessor-pragma.md)

- [`.shader`](unity-shader-object.md) file has additional `#pragma` directives added by Unity
- Can be used to declare shader [keywords](unity-shader-keywords.md) which can be used in conditional statements

### Shader Stages

`#pragma vertex <name>`

- Specifies the [vertex shader](unity-shader-terminology.md#shader-stage) entry point
- **Required** in regular graphics shaders

`#pragma fragment <name>`

- Specifies the [fragment shader](unity-shader-terminology.md#shader-stage) shader entry point
- **Required** in regular graphics shaders

`#pragma geometry <name>`

- This statement will auto turn on `#pragma require geometry`
- Not required

### Shader variants and keywords

`#pragma multi_compile <keywords>`

`#pragma shader_feature <keywords>`

`#pragma hardware_tier_variants <values>`

`#pragma skip_variants <list of keywords>`




