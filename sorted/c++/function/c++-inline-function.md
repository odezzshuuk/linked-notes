# Inline Function

- `inline func(x)`

> An optimization in C++ to improve program runtime speed
> It is a suggestion to the compiler

- Member functions defined inside a class are inline by default
- Features: improves runtime efficiency, reduces compile-time efficiency, increases memory usage
- Usage conditions: function content is simple, such as class accessors
- Source files composed of inline functions use the `.inl` extension; when there are too many inline functions in a header file, include the inl file at the **end** of the header file using `#include`
