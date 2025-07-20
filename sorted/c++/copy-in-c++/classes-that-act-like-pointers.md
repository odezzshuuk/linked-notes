# Classes that Act Like Pointers

- The underlying data used is the same; changing the copy will change the original object.
- This can be implemented using `shared_ptr`.
- Direct resource management can also be performed using **reference counting**.
- Using **reference counting**:
  - When an object is **created**, the counter is initialized to 1.
  - **Copied objects** share the counter; the copy constructor increments the shared counter.
  - The **destructor** decrements the counter; when the counter is 0, the destructor releases the state.
  - **Copy assignment** increments the counter of the right-hand operand and decrements the counter of the left-hand operand.
  - One solution is to store the counter in [[dynamic memory]].
