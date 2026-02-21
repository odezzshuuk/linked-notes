# c++ - const member function

```c++
int func() const {}
```

- Indicates that the implicit parameter `this` for a member function cannot be used to modify the class's data members.
- A const member function is not allowed to modify the object's data members.
- For member functions that do not change the object pointed to by `this`, declaring `this` as `const Sales_data *const` can make the function more flexible.
- The `const` keyword is allowed after a member function's parameter list to declare the function as const.

```mermaid
graph TB
A["'this' is the implicit parameter of member functions"] --> C["const objects cannot call non-const member functions"]
B["By default `this` refers to the (non-const) object"] --> C
C --> D["'this' can be declared as a const pointer to const (e.g., const Sales *const)"]
D --> E["When a member is declared const, place the 'const' after the parameter list"]
```
