# C++ - const

## const Object

- A `const` object cannot be modified after creation, so a `const` object **must be initialized**.
- The initializer can be any valid expression.
- With the `extern` keyword, a `const` object can be defined in one translation unit and declared in others.
- You cannot apply `const` to a function itself (functions cannot be `const` objects).

## const expression

[const expression](c++-const-expression.md)

## Const reference

[const reference](c++-const-reference.md)

## Pointer And Const

[pointer and const](c++-const-and-pointer.md)

## Top-level const vs Low-level const

> The distinction between top-level const and low-level const is: does the `const` qualify the object (the pointer) itself, or the type the pointer/reference refers to?

- **Top-level const**:
  - Applies to the object itself (it makes the object a constant).
  - Example: in `const int a = i;` the `const` on `a` is a top-level const.
  - For pointers, a top-level const means the pointer itself is constant (you cannot change which object it points to): `int *const p`.

- **Low-level const**:
  - Applies to the pointed-to or referenced type (most common for compound types like pointers and references).
  - For pointers/references, a low-level const means the object being pointed to or referenced is const: `const int *p` or `const int &r`.
  - If the underlying object is non-const, it may still be modified through other means; the low-level const only prevents modification via that particular pointer/reference.
  - Example: in `const int &a = i;` the `const` is a low-level const.

## keywords

[mutable](c++-keyword-mutable.md)


