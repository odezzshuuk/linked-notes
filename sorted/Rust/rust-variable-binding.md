# Rust - Variable

## Declaration Default Immutable

- Variable bindings are immutable by default in Rust

```rust
fn main() {
    let x = 5; // x is immutable
    // x += 1; // This would cause a compile-time error

    let mut y = 10; // y is mutable
    y += 1; // This is allowed
}
```

## Immutable VS Const

`const` data type must annotated

```rust
const MAX_POINTS: u32 = 100_000;
```
