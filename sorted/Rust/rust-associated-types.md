# Rust - Associated Types

## Definition

- `type Item;` is the associated type

```rust
trait Iterator {
  type Item;
  fn next(&mut self) -> Option<Self::Item>;
}
```

## Implementation

```rust
struct Counter;
impl Iterator for Counter {
  type Item = u32;
  fn next(&mut self) -> Option<Self::Item> {
    // ...
  }
}
```

## Why not just generic `Iterator<T>`

- Rust allow implement same trait for different types

```rust
impl Iterator<u32> for Counter { ... }
impl Iterator<String> for Counter { ... }  // both allowed
```

- associated type avoid this

[Trait Bound]() on associated type

```rust
trait Iterator {
  type Item: Clone;
  fn next(&mut self) -> Option<Self::Item>;
}
```

## With Trait Object

Using trait with assiociated types as [trait object]() require specifying the type

```rust
let x: &dyn Iterator<Item = u32> = ...;
```

