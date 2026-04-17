# Rust - Ownership

* [What is Ownership](#what-is-ownership)
* [Rules](#rules)
* [Single Ownership Demonstration](#single-ownership-demonstration)
* [Why Ownership Model](#why-ownership-model)
* [When Ownership Moving Happens](#when-ownership-moving-happens)
* [Ownership For Copy Types](#ownership-for-copy-types)

## What is Ownership

- Rust core mechanism for memory management
- Owner is pointer-like variable

## Rules

- Every value has an owner
- There can **only be one** owner at a time
- For [moveable types](rust-concepts#move-value), ownership can be moved
- For [copy types](rust-concepts#copy-value), ownership is not moved, but copied
- When the owner goes out of scope, the value will be dropped

## Ownership Moving Demonstration

```rust
fn main() {
    let s = String::from("hello");
    let t = s; // s1 is moved to s2, s1 is no longer valid
    println!("{}", s); // Error
    println!("{}", t); // This works fine
}
```

- Ownership moved

## Why Ownership Model

Use `String` for instruction

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

fig.02 ![ownership-model-02](img/rust-ownership-model-02.svg) 

**Reason 1**

- if Rust performs a shallow copy(fig.02), both `s1` and `s2` would point to the same heap memory
- when both `s1` and `s2` go out of scope and try to free the same memory.
  - which could lead to [double free](c-double-free.md) errors 

fig.03 ![ownership-model-03](img/rust-ownership-model-03.svg)

**Reason 2**

- if Rust performs a deep copy, 
- it could be very expensive when heap data is large

Here is what Rust do

- When `let s2 = s1;` happens, Rust considers `s1`  as no longer valid
- Known as [move](c++-move-constructor)

fig.04 ![ownership-model-04](img/rust-ownership-model-04.svg)

## When Ownership Moving Happens

1. Assignment: `let s2 = s1;`
2. Function call: `take_ownership(s1);`
3. Return value
4. Struct field move
5. Pattern matching
6. Container Extraction

> Variable type must be [moveable](rust-concepts.md#move-value)

No ownership moving happens when `let y = &x`, it called [borrowing/reference](rust-borrowing.md)

## Ownership For Copy Types

When matters: reference to a variable before copy

```rust
fn main() {
    let mut x = 10;

    let m = &mut x;
    let y = x; // ❌ ERROR: cannot use `x` while mutably borrowed

    println!("{m}");
}
```

When doesn't matter: assignment to a new variable

```rust
fn main() {
    let x = 10; // i32 is a copy type
    let y = x; // ✅ OK: `x` is copied, not moved
    println!("x: {}, y: {}", x, y); // x: 10, y: 10
}
```
