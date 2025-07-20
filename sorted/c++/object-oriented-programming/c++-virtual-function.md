# C++ - Virtual Function

## What is a Virtual Function

- These are functions that the **base class** expects the **derived class** to override, but the derived class can choose not to override virtual functions.
- The `virtual` keyword appears before the declaration statement inside the class.
- The return type of a virtual function in the derived class must be the same as that in the base class or satisfy an inheritance relationship conversion.
- Once a function is declared as a virtual function, it is a virtual function in all derived classes.

## Defining a Virtual Function

- Must be Defined; unlike normal functions, which can be declared without being defined.
- If a derived class overrides a virtual function, the parameter list must be the same as the overridden base class virtual function; more details in [Scope in Inheritance](c++-scope-in-inheritance.md).
- Cannot be defined [outside of the class]().

## Dynamic Binding

- <font color="red">The version of a virtual function is selected at runtime based on the actual type of the object bound to the pointer or reference, which is also called dynamic binding.</font>

> Normal functions are determined by the pointer type.

- When a virtual function is called using a **pointer** or **reference**, the call will be dynamically bound.
- A call to a virtual function through a **pointer** or **reference** is not resolved until runtime.

> That is to say: which virtual function is called is determined at runtime based on the bound object.

## `override` keyword

- Used in a **derived class**.
- After the **parameter list of the virtual function with the same name in the base class** and the [trailing return type](c++-function-return-type.md#trailing-return-type).
- <font color="red">Indicates that the function's parameter list must be exactly the same as the original function's; otherwise, the compiler will report an error.</font>

> <font color="red">Inconsistency is allowed but not recommended.</font>

> In a derived class, it is allowed to define a function with the same name as a virtual function in the base class but with a different parameter list; however, this is not recommended because it makes it difficult to debug and find errors, so the new standard added the `override` keyword.

## `final` keyword

- `final` indicates that the function cannot be overridden and is not intended to be inherited by other classes.
  - Used after the parameter list and trailing return type.
- Use `int i = B->A::func()` to forcibly call the member `func` in the base class A, even if `func` has been reimplemented in the derived class B.

## Pure Virtual Function

- Can be left undefined and be overridden by a derived class in its undefined state.
- Fill in `=0` at the function body to indicate that this is a pure virtual function, meaning that the function has no definition.
- If a definition is to be provided, it must be defined outside the class.
- A class containing a pure virtual function is called an abstract base class.
  - Defines an interface for derived classes to implement.
  - Cannot create objects of an abstract base class.
- Specifically used for inheritance to avoid writing meaningless code.

## [Virtual Function Table](c++-virtual-function-vtable.md)
