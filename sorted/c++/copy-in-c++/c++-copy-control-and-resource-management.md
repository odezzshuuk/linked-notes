# Copying in C++

- Function declarations:
  - Default constructor `Foo();`
  - Copy constructor `Foo(const Foo&) {}`
  - Move constructor `Foo(Foo&&) {}`
  - Copy assignment operator `Foo& operator= (const Foo&) {}`
  - Move assignment operator `Foo& operator=(Foo &&rhs) noexcept`
  - Destructor `~Foo() {}`

```c++
string dots(10, '.');  // direct initialization
string s(dots);   // direct initialization
string s2 = dots;  // copy initialization
```

[Copy Constructor](c++-copy-constructor.md)

[[Copy Assignment Operator]]

[Destructor](c++-destructor.md)

[[Rule of Three/Five]]

[[Explicit =default]]

[[Preventing Copying]]

[[Classes that Act Like Values]]

[[Classes that Act Like Pointers]]

[Object Move](c++-object-move.md)

[[Dynamic Memory Management]]
