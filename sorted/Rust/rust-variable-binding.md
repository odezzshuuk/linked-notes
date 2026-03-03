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

- Immutable in Rust is deep immutable(fields of instance also immutable)

> which is different from const in [javascript](javascript-variable-declaration#const-declaration)

```rust
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let p = Point { x: 1, y: 2 }; // p is immutable
    // p.x = 3; // This would cause a compile-time error
}
```

## Immutable VS Const

`const` data type must annotated

```rust
const MAX_POINTS: u32 = 100_000;
```
