# C++ - Vector

- A vector represents a collection of **objects**. Since references are not objects, a vector cannot contain references.
- `vector` is a **class template** in C++, not a type.
- A **class template** requires **additional information (T)** to determine what kind of class to instantiate.
- Initialization methods:
  - **Default initialization**: Contains no elements, e.g., `vector<int> v1` in the code below.
  - **Copy initialization**: E.g., `vector<int> v2`.
  - **List initialization**: Multiple elements enclosed in curly braces, e.g., `v5`.
  - **Value initialization**: Arguments enclosed in parentheses, e.g., `v3, v4`.
  - **Initialization from an array**: Similar to value initialization, takes pointers to the first and one-past-the-end elements.
  > If the provided list does not match list initialization, the compiler will attempt value initialization for the vector object.

```c++
vector<T> v1;            // Empty vector
vector<T> v2(v1);        // v2 is a copy of v1
vector<T> v2 = v1;       // Equivalent to vector<T> v2(v1)
vector<T> v3(n, val);    // v3 contains n elements, each initialized to val
vector<T> v4(n);         // v4 contains n default-initialized elements of type T
vector<T> v5{a,b,c...};  // v5 contains the specified elements
vector<T> v5 = {a,b,c...}; // Equivalent to v5{a,b,c...}
vector<T> v6(begin(arr), end(arr)); // v6 is initialized from array arr
vector<T> v7(arr+1, arr+4); // v7 consists of elements 2 to 4 of array arr
```

- Supports element access via subscript (`object[ind]`), but does not support adding elements via subscript.
- Adding elements to a vector:
  - `vector_object.push_back()`; // Adds an element at the end
- **`vector<T>::size_type`**:
  - Similar to `string`, returned by the `size()` function
  - The type `T` must be specified
- **Vector objects** can only be compared if their **elements** are comparable
- [Adding Elements](c++_manual.md#sequential-container-adding-elements)
- [Removing Elements](c++_manual.md#sequential-container-removing-elements)
  - Removing elements without parameters: `vector.pop_back()`, `vector.pop_front()`
  - Removing elements via iterator parameter: `vector.erase(P)`
  - Cannot remove elements by passing their value as parameter
