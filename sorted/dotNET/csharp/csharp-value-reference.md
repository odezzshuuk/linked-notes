# CSharp - Value and Reference

## Value VS Reference

Value type variable initialization

- Variable has its own memory

Reference type variable initialization

- Is a alias of the object
- Point to the same memory in heap

## Value

- Value Type stored in stack, only need one memory
- They Are Value Type: `sbyte`, `byte`, `float`, `short`, `float`, `short`, `ushort`, `double`, `int`, `uint`, `char`, `long`, `ulong`, `decimal`, `bool`
- Value Defined By User：[`struct`](csharp-struct.md), [`enum`](csharp-enum.md)

## Reference

- Reference Type need two memory
  - Reference, in stack or heap, point to the actual data in heap
  - Actual Data, in heap
- Predefined Reference Type：object, string, dynamic
- Reference Type Defined By User: class, interface, delegate, array
  
## Similar Concepts

[memory layout of c program](linux-c-program-memory-layout.md)

[javascript value and reference](javascript-variable-copy-and-reference.md)
