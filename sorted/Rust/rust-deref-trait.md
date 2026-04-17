# Rust - Deref Trait

## Overview

- Type that implements `Deref` trait: 
  - Can be dereferenced with the [`*` operator](rust-deref-operator.md)
  - Can take advantage of [deref coercion](#deref-coercion)

## Declaration in std

```rust
pub trait Deref {
  type Target: ?Sized;
  fn deref(&self) -> &Self::Target;
}
```

## Work With Deref 

```rust
fn main() {
    let x = 5;
    let y = &x;

    assert_eq!(5, x);
    assert_eq!(5, *y); }
```

Use `Box<T>` which implements `Deref` trait

```rust
fn main() {
    let x = 5;
    let y = Box::new(x);

    assert_eq!(5, x);
    assert_eq!(5, *y);
}
```

- when `*y` is evaluated, Rust actually performs `*(y.deref())`

As Contrast

- define `MyBox<T>`, a tuple struct, without implementing `Deref` trait

```rust
struct MyBox<T>(T);
imple<T> MyBox<T> {
    fn new(x: T) -> MyBox<T> {
        MyBox(x)
    }
}

fn main() {
    let x = 5;
    let y = MyBox::new(x);

    assert_eq!(5, x);
    assert_eq!(5, *y); // error: cannot dereference `MyBox<{integer}>`
}
```

- without `deref` trait, Rust can only dereference `&` references

## Deref Coercion

What's It

- Convert references that implement `Deref` trait into references of another type

When It Happens

- When pass a [reference/borrow type(&)](rust-borrowing.md) to a particular type's value as an ARGUMENT to a **FUNCTION** or **METHOD CALL**

Deref Corecion is recursive

```rust
fn hello(name: &str) {
    println!("Hello, {}!", name);
}

fn func() {
    let name = Arc::new(String::from("Rust"));  // type of name is Arc<String>
    hello(&name);
}
```

- Chained Deref Coercion: `&Arc<String>` → `&String` → `&str`

## Mutable Deref Coercion

1. From `&T` to `&U` when T: `Deref<Target=U>`
2. From `&mut` `T` to `&mut U` when T: `DerefMut<Target=U>`
3. From `&mut T` to `&U` when T: `Deref<Target=U>`

## A Minimal Implementing of `Deref` trait

```rust
use std::ops::Deref;

struct MyBox<T>(T);
impl<T> Deref for MyBox<T> {
    type Target = T;

    fn deref(&self) -> &T {
        &self.0
    }
}
```

- `Target` defines an associated type
- `.0` access the first field of the [tuple](rust-struct#tuple-struct) struct `MyBox<T>`

## Deref In dot operator method access

[deref in method](rust-method#method-call-resolution)

### When Deref Is Appropriate

1. Smart Pointer

- `Box<T>`, `Arc<T>`, `RefCell<T>`, `MutexGuard<T>`, etc.

2. Transparent "thin" wrapper

- Such as `String` -> `str`, `Vec<T>` -> `[T]`, `PathBuf` -> `Path`

3. New type geneuinely is the inner type

- `struct Hostname(String);`

### When Deref Is An Anti-Pattern

1. Domain types with invariant

- For example `Email` deref to `&str`, method `.split_at()`, `.trim()` can be called on `Email` text which may break the email format, such as missing `@` symbol, etc.
- Because of `Deref`, all `str` methods become available on `Email` value 

2. Types where you want to restricted API
3. Fake inheritance


