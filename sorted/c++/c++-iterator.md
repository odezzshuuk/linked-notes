# CPP - Iterator

- Similar to pointers, iterators can be dereferenced to access the objects they point to.
- The type of an iterator is a **standard library type**, either `iterator` or `const_iterator`:
  - `std::vector<T>::iterator it`: `it` can read and write elements of type `T` in `vector<T>`.
  - `string::iterator it2`: `it2` can read and write characters in a `string` object.
- All standard library containers can use **iterators**, but only a few also support **subscript operators**.
- To obtain an iterator, **do not** use the address-of operator (`&`):
  - Types with iterators have member functions that return iterators.
  - The `begin` member returns an iterator pointing to the first element.
  - The `end` member returns a past-the-end iterator.

## Operations

- Can be understood as operations on the position pointed to by the iterator:
  - `iter + n`: Points to a new position `n` elements forward or the next position after the current one.
  - `>=, <, >, <=`: Compares the positions of the iterators in the container (lower to higher position).
  - `++iter, --iter`: Moves the iterator to the next/previous element.
  - `iter1 == iter2`: Checks whether the iterators point to the **same element**.
  - `iter->mem`: Dereferences the iterator, equivalent to `(*iter).mem`.

## 5 Types of Iterators

| Type                   | Description                                                                                                 |
| ---------------------- | ----------------------------------------------------------------------------------------------------------- |
| Input Iterator         | Read-only, single-pass traversal, can only increment.<br>Supports `==`, `!=`, and dereference operator `*`. |
| Output Iterator        | Write-only, single-pass traversal, can only increment.<br>Supports dereference operator.                    |
| Forward Iterator       | Read-write, multi-pass traversal, can only increment.<br>Supports all input and output iterator operations. |
| Bidirectional Iterator | Read-write, multi-pass traversal, can increment and decrement.<br>Supports all forward iterator operations. |
| Random Access Iterator | Read-write, multi-pass traversal.<br>Supports all iterator operations.                                      |
