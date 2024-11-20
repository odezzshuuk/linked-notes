# Unity - HLSL Language 

* [Semantic](#semantic)
* [Variable](#variable)
* [Function](#function)
* [Built-in Functions](#built-in-functions)
* [Operators](#operators)

## Semantic

[Semantic](unity-hlsl-semantic.md)

## Variable

[Data Types](unity-hlsl-data-types.md)

Modifier

- `uniform`: constant throughout the shader, global variable is default uniform
- `extern`
- `precise`
- `nointerpolation`
- `shared`
- `groupshared`
- `static`
- `volatile`

## Function

Declaration

- A return type
- A function name
- An argument list (optional)
- An input/output semantic (optional)
- An annotation (optional)

Argument Modifier

- in
- inout
- out: the last value of the parameter should be copy out
- uniform

## Built-in Functions

[Built-in Functions](unity-hlsl-built-in-functions.md)

## Operators

`*`: scale multiplication

- `(1, 2, 3) * (4, 5, 6) = (1 * 4, 2 * 5, 3 * 6) = (4, 10, 18)`

dot product

```c
float3 a = float3(1, 2, 3);
float3 b = float3(4, 5, 6);
float dotProduct = dot(a, b);
```

