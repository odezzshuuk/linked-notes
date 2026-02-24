# Rust - Ownership Model

* [What Is Ownership](#what-is-ownership)
* [Why Ownership Model](#why-ownership-model)
* [When Ownership Transfer Happens](#when-ownership-transfer-happens)
* [Reference Lifetime](#reference-lifetime)
* [Borrowing](#borrowing)
* [Borrow Checker](#borrow-checker)
* [Benefits](#benefits)

## What Is Ownership

[Ownership](rust-ownership.md)

## Reference Lifetime

[Reference Lifetime](rust-reference-lifetime.md)

## Borrowing

[Borrowing](rust-borrowing.md)

## Benefits

- Allow rust to guarantee memory safety without a garbage collector
- Prevent entire classes of bugs(dangling pointer, double free, etc) at compile time

Use c++ as a comparison

- Similar behavior in c++
- This c++ code will compile without any errors
- Errors will raise at runtime

```cpp
#include <iostream>
#include <string>
using namespace std;
int main() {
    string* s = new string("hello");
    string* t = s;
    delete s;  // s is deleted, t is now a dangling pointer
    cout << *s << endl;  // Compiler do nothing here, but compiled program will crash here.

    // cout << *t << endl;  // This causes undefined behavior, generally a non-stop output
}
```



