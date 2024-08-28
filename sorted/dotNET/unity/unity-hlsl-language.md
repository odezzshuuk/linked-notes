# Unity - HLSL Language 

## Semantic

[Semantic](unity-hlsl-semantic.md)

## Variable

Data Types

- float

Modifier

- uniform: constant throughout the shader, global variable is default uniform
- extern
- precise
- nointerpolation
- shared
- groupshared
- static
- volatile

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

- tex2D(s, t)
