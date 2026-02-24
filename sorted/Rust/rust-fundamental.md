# Rust - Fundamental

## Variable Binding

[Variable](rust-variable-binding.md)

## Data Type

[Type](rust-data-type.md)

## Function

return value

```rust
fn add(x: i32, y: i32) -> i32 {
    return x + y;
}
fn only_one_number() -> i32 {
    5
}
fn add(x: i32, y: i32) -> i32 {
    x + y
    // x + y;  // return type is `()`, unit type
}
```

> [unit type definition here](rust-data-type#unit)

## Statement

Not value

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

