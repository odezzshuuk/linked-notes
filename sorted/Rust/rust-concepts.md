# Rust - Concepts

## Ownership

[Ownership](rust-ownership-model.md#what-is-ownership)

## Borrowing

[Borrowing](rust-ownership-model.md#borrowing)

## Variable Value Behavior

- [Copy](#copy-value)
- [Move](#move-value)
- [Borrow](#borrow-value)

## Immutable

## Mutable

## Copy Value

```rust
fn main() {
    let x = 5; // x is a copy type
    let y = x; // y is a copy of x, x is still valid
    println!("x: {}, y: {}", x, y); // x: 5, y: 5
}
```

built-in copy types

- i8 i16 i32 i64 i128
- u8 u16 u32 u64 u128
- isize usize
- f32 f64
- bool
- char

## Move Value

```rust
fn main() {
    let s1 = String::from("hello"); // s1 is a move type
    let s2 = s1; // s2 is a move of s1, s1 is no longer valid
    println!("s2: {}", s2); // s2: hello
    // println!("s1: {}", s1); // Error: borrow of moved value: `s1`
}
```

- owns heap memory
- manage resources
- has destructor(drop)
- use [RAII](cpp-raii.md) semantics
- For example:
  - `String`
  - [Struct](rust-struct)
  - `Vec<T>`
  - `Box<T>`
  - `HashMap<K, V>`
  - `Rc<T>`
  - `Arc<T>`
  - `Mutex<T>`

Features

- Ownership should be aware

## Borrow Value

> Neither copy nor move, but borrow

```rust
fn main() {
    let x = 10; // x is a move type
    let a = &x; // a is an immutable borrow of x
    let b = &x; // b is another immutable borrow of x, allowed

    println!("a: {}, b: {}", a, b); // a: 10, b: 10
}
```

- [Pointer-like] value: &T, &mut T, *const T, *mut T

## Stack-stored variable

> Data structure: [stack](data-structure-stack)

- known size at compile time
- Fast allocation and deallocation

Example

```rust
let a: i32 = 10;
let b: bool = true;
let c: f64 = 3.13;
let arr: [i32; 3] = [1, 2, 3];

struct Point {
    x: f64,
    y: f64,
}
let p = Point { x: 1.0, y: 2.0 };
let tuple: (i32, f64, bool) = (42, 3.14, false);
```

## Heap-stored variable

> Data structure: [stack](data-structure-heap)

- Size known only at runtime
- Dynamic growth
- Requires explicit allocation and deallocation (managed by ownership)
- Data on heap, pointer on stack
- Access via pointer-like owner

Examples:

```rust
let v = Vec::new();
let s = String::from("hello");
let b = Box::new(42);
let m = HashMap::new();
let rc = Rc::new(String::from("shared data"));
```

## Mixed Storage

```rust
struct Node {
    value: i32, // stored on stack
    next: Option<Box<Node>>, // Box<Node> is a pointer to heap
}
let node1 = Node { value: 1, next: None };
```

## Unit

[Unit](rust-data-type#unit)

## Statement

Not a value

```rust
let x = 5;
```

## Expression

- evaluate to a value
- remove last semicolon `;` to represent a expression with `{}` block, 

```rust
let x = {
    let y = 6;
    y + 1
}
```
