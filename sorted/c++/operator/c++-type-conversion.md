# Type Conversion

- C++ does not directly add values of two different types.
- Implicit conversions are performed automatically by the compiler.
- Implicit conversions try to avoid loss of precision.
- Conditions for implicit conversion:
  - Integer values smaller than int are promoted to a larger integer type.
  - In **conditions**, non-bool values are converted to the bool type.
  - During initialization, the initial value is converted to the variable's type.
  - In an assignment statement, the right-hand operand is converted to the type of the left-hand operand.
- In operations with multiple objects of multiple types, they are converted to the same type.
- When converting to bool, a pointer or arithmetic type with a value of 0 is converted to false.

```c++
int val = 3.14 + 3;
/* 
3.14 is a double, 3 is first converted to a double and added to 3.14, resulting in a double.
During the initialization of the int object, the double is truncated to an int.
*/
```

- downcast: base class to derived class
- upcast: derived class to base class

## static_cast

- [static_cast](c++-static-cast.md)

## dynamic_cast

- Performs a type check before conversion.

## const_cast

## reinterpret_cast
