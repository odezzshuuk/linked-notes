# Rust - Associated Types

## Declaration


```rust
trait Iterator {
  type Item;
  fn next(&mut self) -> Option<Self::Item>;
}
```

- `type Item;` is the associated type

Declaring with [Trait Bound]()

```rust
trait Iterator {
  type Item: Clone;
  fn next(&mut self) -> Option<Self::Item>;
}
```

## Implementation

```rust
struct Counter;
impl Iterator for Counter {
  type Item = u32;
  fn next(&mut self) -> Option<Self::Item> {  }
  fn get_current_count(&self) -> Self::Item {
}
```

## Why not just generic type parameter

- Most cases, associated type and [generic type parameter](rust-generic.md) can be used interchangeably

But, for generic trait

- Implementing trait for a type multiple times with different generic type parameter is allowed

```rust

```rust
impl Iterator<u32> for Counter { ... }
impl Iterator<String> for Counter { ... }  // both allowed
```

Associated type avoid this

- Because rust cant implement a trait on a type multiple times

```rust
impl Iterator for Counter {
  type Item = u32;
}

impl Iterator for Counter {  // Error: conflicting implementations of trait `Iterator` for type `Counter`
  type Item = String;
}
```

## With Trait Object

Using trait with assiociated types as [trait object]() require specifying the type

```rust
let x: &dyn Iterator<Item = u32> = ...;
```

