# Array

- Explicitly initialize an array: `int arr[size] = {0, 1, 2, ..., size-1}`
  - The number of initial elements can be **less than or equal to** size, but cannot exceed size
  - size can be omitted, and the dimension is determined by the number of initial elements
- Compared to vector, arrays have better performance but poorer flexibility
- An array is not a class
  - Therefore, `begin` and `end` are not member functions. The usage involves passing the array as an **argument** to `begin(arr)` and `end(arr)`
  - `begin` returns a **pointer** to the first element, and `end` returns a **pointer** to the **one-past-the-end** element
  - The `begin` and `end` functions are defined in the `<iterator>` header file
- The dimension must be a [constant expression](c++-constexpr.md), and the dimension can be considered part of the type
- References are not objects, so array elements cannot be references (same as vector)
- **Copying** and **assignment** are not allowed

> Therefore, arrays cannot be **directly** used as function parameters—they are automatically converted to pointers to the array.
> Some compilers support array assignment as a **compiler extension**, which is a non-standard feature.

- Understand the difference between **an array of pointers** and **a pointer to an array**
  - `int *ptr[10];` `ptr` is an **array of pointers**
  - `int (*Parray)[10];` `Parray` is a **pointer to an array**
  - **<font color="red">The type declaration of an array declares the element type</font>**, meaning the element type of `ptr` is `int*`, and the element type of `*Parray` is `int`
- Distinct from `std::array`

## Pointers and Arrays

- The **array name** is replaced by the compiler with a **pointer** to the **first element** of the array
- If `ia` is an array, `auto ia1(ia);` infers `ia1` as a pointer type
- If `ia` is an array, `decltype(ia) ia2;` declares `ia2` as an array with the same type and dimension as `ia`
- The **one-past-the-end pointer** points to a non-existent element. You can obtain the **address** of the **one-past-the-end pointer**, but you **cannot** dereference it to access an element
- Pointers to array elements support the same [operations](c++-iterator#operations) as iterators
- Subscripts and pointers

```c++
int ia[] = {0, 2, 4, 6, 8};  // 
int *p = &ia[2];  // p is a pointer pointing to the element at index 2 of array ia
int j = p[1];  // p[1] is equivalent to *(p + 1),
```

## Multi-Dimensional arrray

