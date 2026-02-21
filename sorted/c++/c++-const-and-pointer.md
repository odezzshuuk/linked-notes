# C++ - Pointer And Const

- `int *ptr` — a normal pointer that points to a non-const object.

## Pointer to a const object

- `const int *ptr`
- There is no requirement that the pointed-to object must be const; the pointer can point to either a const object or a non-const object.
- It only means you cannot modify the pointed-to object through that pointer.
- The type of `ptr` is `const int*`.
- For pointers or references to const, you cannot modify the value via the const pointer/reference. If the underlying object is non-const, it can still be modified through other means — this is known as low-level const (the const applies to the pointer/reference, not necessarily to the object itself).

```cpp
const double pi = 3.14;
double *ptr = &pr;
const double *cptr = &pi;
*cptr = 42; // error: cannot assign through a pointer-to-const
```

## Const Pointer

- The pointer itself is constant — this is a top-level const.
- `int *const ptr;` declares `ptr` as a const pointer to a (non-const) `int` object.
- `const int *const ptr;` declares `ptr` as a const pointer to a `const int` object.

```cpp
const double pi = 3.14159;
const double *const piptr = &pi;  // piptr is a const pointer point to a const double
```

- Indicates `ptr` is a const pointer that points to an `int` object.

