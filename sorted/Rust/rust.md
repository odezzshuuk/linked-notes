# Rust

[Concepts](rust-concepts.md)

## Ownership Model

Example:

- this rust code will not compile

```rust
fn main() {
    let s = String::from("hello");
    let t = s; // s1 is moved to s2, s1 is no longer valid
    println!("{}", s); // This would cause a compile-time error
    println!("{}", t); // This works fine
}
```

- Similar behavior in c++
- This c++ code will compile without any errors
- But when executed,  

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

Why Rust is designed this way:

- Enforces memory safety at compile time without a garbage collector

## Borrowing Checker

## Lifetimes

## Zero-cost Abstractions

## Algebraic Data Types

## No Null

## Error Handling Via Types(not exceptions)

## Fearless Concurrency(Data-race freedom)

## `unsafe` Is Explicit And Contained

## Trait System(Different from OOP)



