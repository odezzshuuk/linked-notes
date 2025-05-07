# CSharp - Types

- [Primitive Types](#primitive-types)
- [Built-in Types](#built-in-types)
- [Unmanaged Types](#unmanaged-types)
- [Default Values](#default-values)
- [Value Types](#value-types)
- [Reference Types](#reference-types)
- [Conversion](#conversion)

## Primitive Types

## Built-in Types

## Unmanaged Types

- All [primitive types](#primitive-types)
- Any [Enum type]()
- Any [pointer types]()
- A [tuple] whose element types are all unmanaged types
- Any user-defined [struct types](csharp-struct.md) that contains fields of unmanaged types only

## Reference Types(managed type)

- Class, interface, delegate, [record](csharp-record.md)
- Array, such as `int[]`..., 

Features constrast between managed type and reference type

| Feature            | Unmanaged Types                        | Reference Types                        |
| ------------------ | -------------------------------------- | -------------------------------------- |
| Category           | Subset of value types                  | Distinct from value types              |
| Examples           | int, float, Vector3, unmanaged structs | string, object, int[], classes         |
| Memory             | Allocation Stack or inline (no GC)     | Heap (managed by GC)                   |
| Copy Semantics     | By value (full copy)                   | By reference (shared object)           |
| Performance        | Fast, no GC overhead                   | Slower, GC overhead                    |
| Interoperability   | Ideal for native code (P/Invoke)       | Requires marshaling for native code    |
| Serialization      | Efficient, direct byte copy            | Complex, requires custom serialization |
| Mutability         | Structs can be mutable or immutable    | Often mutable (except string)          |
| Garbage Collection | Not subject to GC                      | Subject to GC, can cause pauses        |

> struct can be unmanaged struct and reference struct

## Default Values

## Value Types

- integer numeric types: `byte`, `sbyte`, `short`, `ushort`, `int`, `uint`, `long`, `ulong`
- floating-point numeric types: `float`, `double`
- built-in numeric conversions
- bool
- char
- enumeration types
- struct types, ref struct types
- tuple types
- nullable value types

## Reference Types

## Conversion

Implicit conversion

```c
int intValue = 10;
long longValue = intValue;
```

Explicit cast

```c
double doubleValue = 3.14;
float floatValue = (float)doubleValue;

int intValue = (int)doubleValue;
```
