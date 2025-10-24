# Return Type

## Returning Array Pointers

- The return value is a pointer to an [array](c++-array.md)
- Since **arrays cannot be copied**, a function cannot return an array, but it can return a pointer or reference to an array
- Function format: `Type (*function(parameter)) [dimension]`
  - Type: indicates the **element** type
  - dimension: indicates the size of the array dimension
- Function declaration breakdown:
  - `func (int i)`  &nbsp; function name, parameter type and name
  - `(*func (int i))` &nbsp; dereference the **return value** of the function call
  - `(*func(int i))[10]` &nbsp; gets an array of size 10
  - `int (*func(int i))[10]` &nbsp; declares the element type

## Trailing Return Type
- `auto func(int i) -> int(*)[10];` returns a pointer to an array of 10 elements
- Any function can be defined with a trailing return type, but it is especially suitable for complex return types
