# C++ - Pointer VS Reference

- `&` and `*` are not primitive data types.
- `&` and `*` act as declarators when used on the left side of a declaration.

```cpp
int* ptr; // ptr is a pointer to an int

int number = 42;
int& ref = number; // ref is a reference to an int
```

`&` and `*` act as operators when used on the right side of an expression:

- `&` takes the address of an object

```cpp
int number = 42;
int* ptr = &number; // ptr now holds the address of number
```

- `*` dereferences a pointer

```cpp
int number = 42;
int* ptr = &number; // ptr holds the address of number
int value = *ptr; // value is now 42, dereferencing to get the value
*ptr = 100;
```
