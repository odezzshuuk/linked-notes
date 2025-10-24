# Cpp - Local Object

- Function parameters and variables defined inside a function are collectively called local variables
- Automatic objects: objects that exist only during the execution of a block
  - Parameters are a kind of automatic object: their scope is within the function body
- Sometimes you need the lifetime of a variable to extend beyond the function call

## Local Static Object

- When you need the lifetime of a local variable to extend beyond the function call, define the variable as static
- The object is initialized the first time it is encountered, and destroyed when the program ends
- If a static variable does not have an explicit initial value, it will be [value-initialized](c++-initialize.md)

  ```c++
  size_t count_calls()
  {
      static size_t ctr = 0;  // ctr remains valid after the call ends
      return ++ctr;
  }
  ```
