# C++ - Scope in Inheritance

- The scope of a derived class is nested within the scope of its base class.
  - When a member is called through a reference or pointer,
  - if a name cannot be resolved within the scope of the derived class,
  - the compiler will continue to search for the definition of that name in the **outer** scope of the base class.
  > Search from the inside out.
  > Name lookup precedes type checking.
- A name in an inner scope **hides** a name in an outer scope.
  > Hiding means that when a member function of a derived class is called,
  - if the inner scope only has a member with the same name but different parameters, even if the outer scope has a member with the same name and parameters,
  - the compiler will report an error because it cannot find the corresponding member function in the outer scope.
- If the virtual functions of the base class and the derived class accept different arguments, the virtual function of the derived class cannot be called through a reference or pointer to the base class.

> Different parameters mean different function types; refer to the description of function types in [function pointer](c++-function-pointer.md).
