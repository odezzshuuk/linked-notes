# Rust - Borrowing

* [Why Borrowing](#why-borrowing)
* [Borrow Checkers](#borrow-checkers)
* [Mutable borrow can only borrow once ](#mutable-borrow-can-only-borrow-once-)
* [Mutable borrow can't borrow immutable declared variable ](#mutable-borrow-can't-borrow-immutable-declared-variable-)
* [Immutable borrowing can borrow multiple times](#immutable-borrowing-can-borrow-multiple-times)
* [Mutable and immutable can exist in same code block(`{}`) ](#mutable-and-immutable-can-exist-in-same-code-block(`{}`)-)

## Why Borrowing

- Provide a way to reference a value without taking [ownership](#what-is-ownership) of it

```rust
let s = string:from("hello");
let r = &s; // r borrows s, r is a reference to s
println!("{}", r); // "hello"
println!("{}", s); // "hello", as well
```

fig.05 ![borrowing-01](img/rust-borrowing-01.svg)

## What's Borrow Checker

- Rust compiler compares scopes to determine whether all borrows are valid
- If any borrow out of scope, 
- It's about memory correctness, not about memory allocation

## Why Borrow Checker

- Borrow checker guarantee:
  - Dangling pointer eliminated
  - Each resource has a single owner
  - No data race
  - No Iterator invalidation
  - ...

## Borrow Checker check rules

1. [Mutable borrow can only borrow one at a time](#mutable-borrow-can-only-borrow-once)
2. [Mutable borrow can't borrow immutable declared variable](#mutable-borrow-cant-borrow-immutable-declared-variable)
3. [Immutable borrowing can borrow multiple times](#immutable-borrowing-can-borrow-multiple-times)
4. [Mutable and immutable can exist in same code block(`{}`)](#mutable-and-immutable-can-exist-in-same-code-block(`{}`))


## Mutable borrow can only borrow once 

```rust
fn main() {
    let mut x = 10;
    let a = &mut x; // mutable borrow
    let b = &mut x; // Error: cannot borrow `x` as mutable more than once at a time

    println!("{a}");  // first mutable used here
    println!("{b}");
}
```

## Mutable borrow can't borrow immutable declared variable 

```rust
fn main() {
    let x = 10; // x is immutable
    let a = &mut x; // Error: cannot borrow `x` as mutable because it is not declared as mutable

    println!("{a}");
}
```

## Immutable borrowing can borrow multiple times

- Cant mutable borrow while immutable borrow exists

```rust
fn main() {
    let mut x = 10;
    let a = &x;   // immutable borrow
    let b = &x;   // immutable borrow second time, Ok
    let c = &mut x;  // Error: cannot borrow `x` as mutable because it is also borrowed as immutable

    println!("{}, {}", a, b);
}
```

Meanwhile in c++

- Changing a pointer point to const(immutable) via a pointer to non-const(mutable) is allowed
- Which means in c++ behavior like `*c = 42` is allowed, but **forbidden** in Rust

```cpp
int main() {
    int x = 10;
    const int* a = &x;   // pointer to x
    int* c = &x;         // pointer to x, but this is a mutable

    std::cout << "x: " << x << std::endl;  // x: 10
    std::cout << "a: " << *a << std::endl; // a: 10
    std::cout << "c: " << *c << std::endl; // c: 10
    *a = 42;  // Error raised; pointer point value is unchanged, because a is a pointer to const
    *c = 42;  // but `a` point value can be changed via `c`, because `c` is a pointer to non-const
    std::cout << "x: " << x << std::endl;  // x: 42
    std::cout << "a: " << *a << std::endl; // a: 42
    std::cout << "c: " << *c << std::endl; // c: 42

}
```

## Mutable and immutable can exist in same code block(`{}`)

- **when there are no [lifetime](#reference-lifetime) overlap borrowing is allowed**
- [Last-use analysis](rust-concepts#last-use-analysis) allows non-overlapping borrows to coexist

```rust
fn main() {
    let mut x = 10;

    let r1 = &x;                 // --------+--'a
    let r2 = &x;                 //         | 
    println!("{}, {}", r1, r2);  // --------+

    let c = &mut x;              // --------+--'b
    println!("{}", c);           // --------+
}
```
