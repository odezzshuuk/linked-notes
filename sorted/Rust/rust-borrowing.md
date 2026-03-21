# Rust - Borrowing

* [What's Borrowing](#what's-borrowing)
* [Why Borrowing](#why-borrowing)
* [What's Borrow Checker](#what's-borrow-checker)
* [Why Borrow Checker](#why-borrow-checker)
* [Borrow Checker check rules](#borrow-checker-check-rules)
* [When Borrowed Value Back To Owner](#when-borrowed-value-back-to-owner)

## What's Borrowing

- Variable being borrowed can be access from its borrowers
- During a variable is borrowed:
  - Original variable can't be used

immutable borrow

```rust
let x = 10;
let r = &x; // r borrows x, r is a reference to x
```

mutable borrow

```rust
let mut x = 10;
let r = &mut x; // r mutably borrows x, r is a mutable
```

Assignment to a mutable reference with `*` operator

```rust
let mut x = 10;
let r = &mut x; // r mutably borrows x
*r += 1; // r is a mutable reference to x, so we can change x
```
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

[5 Rules](rust-borrow-rules.md)

## When Borrowed Value Back To Owner

1. out of scope

```rust
let mut x = 10;

{
    let r = &mut x;
    *r += 1;
} // r goes out of scope → borrow ends here

x += 1; // ✅ allowed again
```

2. [Non-Lexical Lifetimes(NLL)](rust-reference-lifetime.md)

```rust
let mut x = 10;
let r = &x;
println!("{}", r);
x += 1;
```

3. drop()

```rust
let cell = RefCell::new(5);

let r = cell.borrow(); // borrow starts
drop(r); // borrow explicitly ends

let m = cell.borrow_mut(); // ✅ now allowed
```
