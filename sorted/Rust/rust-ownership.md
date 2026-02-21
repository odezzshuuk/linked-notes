# Rust - Ownership Model

## What Is Ownership

- Rust core mechanism for memory management

Rules

- Every value has an owner
- There can only be one owner at a time
- When the owner goes out of scope, the value will be dropped

Example that cause ownership transfer

```rust
fn main() {
    let s = String::from("hello");
    let t = s; // s1 is moved to s2, s1 is no longer valid
    println!("{}", s); // This would cause a compile-time error
    println!("{}", t); // This works fine
}
```

## Why Ownership Model

Use `String` to Instruction

```rust
let s1 = String::from("hello");
let s2 = s1;
```

What `s1` looks like under cover

![ownership-model-01](img/rust-ownership-model-01.svg)

- **Info Part**, located on stack
  - a pointer to the heap memory where the string data is stored
  - a length field that indicates the length of the string
  - a capacity field that indicates the total allocated memory for the string
- **Data Part**, located on heap
  - the actual string data "hello" stored in heap memory

When `let s2 = s1;`

- if Rust performs a shallow copy(fig.02), both `s1` and `s2` would point to the same heap memory
- when both `s1` and `s2` go out of scope and try to free the same memory.
  - which could lead to [double free](c-double-free.md) errors 

fig.02 ![ownership-model-02](img/rust-ownership-model-02.svg) 

- if Rust performs a deep copy, 
- it could be very expensive when heap data is large

fig.03 ![ownership-model-03](img/rust-ownership-model-03.svg)

Here is what Rust do

- when `let s2 = s1;` happens, Rust considers `s1`  as no longer valid
- Known as [move](c++-move-constructor)

fig.04 ![ownership-model-04](img/rust-ownership-model-04.svg)

## When Ownership Transfer Happens

- TODO

## What Is Borrowing

- A way to reference a value without taking ownership of it

![borrowing-01](img/rust-borrowing-01.svg)

How to Borrow

## Borrow Checker

- Cant mutable [borrow] while will immutable [borrow] exists

```rust
fn main() {
    let mut x = 10;

    // let c = &mut x; // ❌forbidden: mutable + immutable
    let a = &x;   // immutable borrow
    let b = &x;   // immutable borrow OK
    // let c = &mut x; // ❌forbidden: mutable + immutable

    println!("{}, {}", a, b);
}
```

- While in c++

```cpp
int main() {
    int x = 10;
    const int* a = &x;   // pointer to x
    int* c = &x;         // pointer to x, but this is a mutable

    std::cout << "x: " << x << std::endl;  // x: 10
    std::cout << "a: " << *a << std::endl; // a: 10
    std::cout << "c: " << *c << std::endl; // c: 10
    *c = 42;
    std::cout << "x: " << x << std::endl;  // x: 42
    std::cout << "a: " << *a << std::endl; // a: 42
    std::cout << "c: " << *c << std::endl; // c: 42

}
```


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



