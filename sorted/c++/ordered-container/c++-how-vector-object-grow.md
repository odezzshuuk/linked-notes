# How Vector Objects Grow

- When there is not enough space to accommodate new elements, the old elements are [**moved**](c++-object-move.md) to a larger space, and then the new element is added.

## Steps

- The `size()` member function returns the current number of elements.
- The `capacity()` member function returns how many elements the container can hold without allocating new memory space.
- The `reserve()` member function allocates memory space for at least n elements.
- When a vector needs to allocate new space, it doubles its current capacity.
- The `shrink_to_fit()` member function requests the vector to return excess memory back to the system.

> `shrink_to_fit` is only a request; the standard library does not guarantee that memory will be returned.
