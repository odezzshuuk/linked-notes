# CSharp - Generic Constraint

## use `where` to constraint type and order

Constraint Statement

`where TypeParam : type1, type2,...`

class

```cs
public void PrintData<S, T>(S p, T t) where S: Person
```

method

```c
void Foo<T>() where T : type1, type2 { }
```

`where T : <base_class_name>`

- the type argument must be or derive from the specified base class

`where T : <interface_name_1>, <interface_name_2>,...`

- the type argument must be or implement the specified interface
- multiple interface constraints can be specified

`where T : new()`

- the type argument must have a public **parameterless constructor**
- used together with other constraints, it must be the last

`where T : struct`


