# Rust - `From` and `Into` Traits

## Conversion Between Types

Rust implements conversion through the `From<T>` and `Into<T>` traits

- `From`

```rust
use std::convert::From;

#[derive(Debug)]
struct Number {
    value: i32,
}

impl From<i32> for Number {
    fn from(item: i32) -> Self {
        Number { value: item }
    }
}

fn main() {
    let num = Number::from(30);
    println!("My number is {:?}", num);
}
```

- `Into`

```rust
use std::convert::Into;

#[derive(Debug)]
struct Number {
    value: i32,
}

impl Into<Number> for i32 {
    fn into(self) -> Number {
        Number { value: self }
    }
}

fn main() {
    let int = 5;
    // Try removing the type annotation
    let num: Number = int.into();
    println!("My number is {:?}", num);
}
```

## Why Choosen Built-in Trait Over Implementing Struct Directly

`From` and `Into` are interchangeable

- Which means do not need to provide an implementation for both traits
- There is a [blanket implementation](rust-where-clause.md#blanket-impls) of `Into<T>` for any type that implements `From<T>`
- When you implement `From<T>` for a type, you get the `Into<T>` implementation for free

```rust
impl<T, U> for T where U: From<T> {
  fn into(self) -> U {
    U::from(self)
  }
}
```

## Best Practices

- Always prefer implementing `From<T>` over `Into<T>` because of the blanket implementation that provides `Into<T>` for free
- Only implement `Into<T>` when: 
  - Targeting a version prior Rust 1.41
  - **And** converting to a type outside the current crate

```rust
fn func<T: Into<Number>>(num: T) {
    let num = num.into();
    println!("number is {:?}", num);
}
```

- Prefer using `Into<T>` when speficifying trait bounds to ensure that types that only implement `Into<T>` can be used as well

