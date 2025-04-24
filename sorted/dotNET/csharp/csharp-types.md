# CSharp - Types

## Primitive Types

## Built-in Types

## Unmanaged Types

- All [primitive types](#primitive-types)
- Any [Enum type]()
- Any [pointer types]()
- A [tuple] whose element types are all unmanaged types
- Any user-defined [struct types](csharp-struct.md) that contains fields of unmanaged types only

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

