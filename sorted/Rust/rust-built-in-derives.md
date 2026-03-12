# Rust - Built-In Derives

## What It Is

- Built-in derives are standard [derive macros](rust-derive-macro.md) provided by the Rust standard library
- They auto-generate [trait](rust-trait.md) implementations for structs and enums using `#[derive(...)]`
- Multiple derives can be applied at once in a comma-separated list

```rust
#[derive(Debug, Clone, PartialEq)]
struct Point {
    x: f64,
    y: f64,
}
```

## Derives

- [Debug](#debug)
- [Clone](#clone)
- [Copy](#copy)
- [PartialEq and Eq](#partialeq-and-eq)
- [PartialOrd and Ord](#partialord-and-ord)
- [Hash](#hash)
- [Default](#default)

## Debug

- Implements `std::fmt::Debug`, enabling `{:?}` and `{:#?}` formatting
- Essential for printing values during development with `println!` or `dbg!`
- All fields must also implement `Debug`

```rust
#[derive(Debug)]
struct Color {
    r: u8,
    g: u8,
    b: u8,
}

let c = Color { r: 255, g: 128, b: 0 };
println!("{:?}", c);   // Color { r: 255, g: 128, b: 0 }
println!("{:#?}", c);  // pretty-printed
dbg!(&c);
```

## Clone

- Implements `std::clone::Clone`, providing an explicit `.clone()` method for deep copies
- All fields must also implement `Clone`

```rust
#[derive(Clone)]
struct Config {
    name: String,
    retries: u32,
}

let a = Config { name: String::from("app"), retries: 3 };
let b = a.clone(); // independent deep copy
```

## Copy

- Implements `std::marker::Copy`, enabling implicit bitwise copies instead of moves
- [`Clone`](#clone) must also be derived alongside `Copy`
- Only applicable when all fields are `Copy` types (e.g. integers, floats, `bool`, references)
- Heap-owning types like `String` or `Vec` cannot be `Copy`

```rust
#[derive(Debug, Clone, Copy)]
struct Vec2 {
    x: f32,
    y: f32,
}

let a = Vec2 { x: 1.0, y: 2.0 };
let b = a; // copy, not move — a is still valid
```

## PartialEq and Eq

- `PartialEq` implements `==` and `!=` operators by comparing fields one by one
- `Eq` is a marker trait that signals the equality is also reflexive (every value equals itself)
- Derive `Eq` only when all fields implement `Eq`; floating-point types (`f32`, `f64`) do not implement `Eq` because `NaN != NaN`

```rust
#[derive(PartialEq, Eq)]
struct UserId(u64);

let a = UserId(42);
let b = UserId(42);
assert!(a == b);
```

## PartialOrd and Ord

- `PartialOrd` enables `<`, `>`, `<=`, `>=` comparisons; requires [`PartialEq`](#partialeq-and-eq)
- `Ord` provides a total ordering (used by `.sort()`, `BTreeMap`, etc.); requires [`Eq`](#partialeq-and-eq)
- Field comparison follows declaration order — the first field is compared first

```rust
#[derive(PartialEq, Eq, PartialOrd, Ord)]
struct Version {
    major: u32,
    minor: u32,
    patch: u32,
}

let mut versions = vec![
    Version { major: 1, minor: 2, patch: 0 },
    Version { major: 1, minor: 0, patch: 5 },
];
versions.sort();
```

## Hash

- Implements `std::hash::Hash`, allowing values to be used as keys in `HashMap` and `HashSet`
- Requires [`PartialEq`](#partialeq-and-eq); if two values are equal (`==`), their hashes must also be equal
- All fields must implement `Hash`

```rust
use std::collections::HashSet;

#[derive(PartialEq, Eq, Hash)]
struct Tag(String);

let mut tags = HashSet::new();
tags.insert(Tag(String::from("rust")));
```

## Default

- Implements `std::default::Default`, generating a zero-value instance via `Default::default()`
- Default values per field type: `0` for numbers, `false` for `bool`, `""` for `String`, `None` for `Option`, empty collection for `Vec`
- Commonly paired with struct update syntax `..Default::default()` to fill in unspecified fields

```rust
#[derive(Debug, Default)]
struct AppConfig {
    verbose: bool,
    max_connections: u32,
    host: String,
}

let config = AppConfig {
    host: String::from("localhost"),
    ..Default::default() // verbose: false, max_connections: 0
};
```

## Tips & Tricks

- **Derive order doesn't matter** — `#[derive(Clone, Debug)]` and `#[derive(Debug, Clone)]` are equivalent
- **`Copy` implies cheap duplication** — only use it for small, stack-allocated types; prefer `Clone` for heap-owning types
- **`Ord` requires the full chain** — to derive `Ord`, you must also derive `PartialOrd`, `Eq`, and `PartialEq`
- **Custom derive macros** work the same way — see [rust-derive-macro.md](rust-derive-macro.md) for how to build your own

