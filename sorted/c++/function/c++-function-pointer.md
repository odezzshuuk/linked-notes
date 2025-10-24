# C++ - Function Pointer

[[c++_Class_Member_Function_Pointer]]

- A function pointer points to a specific **type**
  - So it can be used as the type declaration for a function parameter
- **The type of a function** is determined by its **return type** and **parameter types**, and has nothing to do with the function name
- That is, the function a function pointer points to must have the same return type and parameter types as the function pointer declaration
- To declare a pointer to a function, replace the function name with a pointer, e.g. `bool (*pf)(const string &, const string &);`
  - pf is an uninitialized function pointer instance
  - The parentheses around `(*pf)` are required; otherwise, it would mean the return type is a bool pointer
- When using a function name as a value and assigning it to a variable, the value of that variable is the function pointer
  - You can assign a function name to a function pointer
  - It can also be nullptr or 0
- Function pointers can be called directly without dereferencing
- Like function declarations, function pointer declarations can be simplified using `typedef` or `decltype`

```c++
// Three equivalent declarations: funcp0, func1, funcp2 are all function pointers to the same type of function
bool (*funcp0)(const string&, const string&);
typedef bool (*funcp1)(const string&, const string&);
typedef decltype(funcp0) funcp2;
```

## Function Pointer as Parameter

- When a function type (return type, parameter types) is used as a parameter, it is automatically converted to a pointer to the function
  - Function pointer declaration: `bool (*pf)(const string &, const string &);`
  - Function parameter: `bool (*pf)(const string &, const string &)`, pf is the parameter name
- For example: for the function `bool lengthCompare(const string &, const string &) {...}`, `lengthCompare` can be used as an argument to a function
