# C++ - Move Constructor

- The first parameter is an rvalue reference to the class type (see c++-rvalue-reference.md).
- Example: `Foo(Foo &&f) noexcept {}`
- Move constructors typically do not allocate new memory.
- After a move, the source (moved-from) object must remain safe to destroy.
- A move constructor should ensure it is safe for the moved-from object to run its destructor.

Synthesized move constructor

- Never implicitly defined as a deleted function.
- An explicitly `= default` move constructor will be defined as deleted if the compiler cannot move all members.
- The compiler will not synthesize move operations for certain classes, such as: 
  - a class defines its own [copy constructor], [copy assignment operator], or [destructor]
- Move operations are not mandatory; if absent, a class will fall back to copy operations.

Conditions for the compiler to synthesize a move constructor:

- The class does not define any of its own copy-control members (copy constructor, copy assignment, destructor)
- All data members are movable-constructible or movable-assignable

## Example

```cpp
#include <iostream>
#include <vector>
#include <utility>

// Custom move constructor: transfers ownership of a heap buffer
struct Buffer {
  int *data = nullptr;
  std::size_t size = 0;

  Buffer(std::size_t n) : data(new int[n]), size(n) {}

  // custom move constructor
  Buffer(Buffer &&other) noexcept
    : data(other.data), size(other.size)
  {
    other.data = nullptr;   // leave moved-from in a safe state
    other.size = 0;
  }

  ~Buffer() { delete[] data; }

  // disable copy for clarity
  Buffer(const Buffer&) = delete;
  Buffer& operator=(const Buffer&) = delete;
};

// Synthesized move constructor example: all members are movable
struct Holder {
  std::vector<int> v; // vector is movable, so Holder gets a synthesized move constructor
};

int main() {
  Buffer a(10);
  Buffer b = std::move(a); // calls custom move ctor; a is left empty but safe to destroy

  Holder h1; h1.v = {1,2,3};
  Holder h2 = std::move(h1); // synthesized move: underlying vector moved

  std::cout << "a.size=" << a.size << " b.size=" << b.size << "\n";
  std::cout << "h1.v.size=" << h1.v.size() << " h2.v.size=" << h2.v.size() << "\n";
}
```

Notes:
- The `Buffer` example shows a manual move constructor that transfers ownership and leaves the source in a safe-to-destroy state.
- The `Holder` example demonstrates when the compiler will synthesize a move constructor (because `std::vector` is movable and `Holder` defines no copy-control members).

