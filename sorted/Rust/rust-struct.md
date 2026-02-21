# Rust - Struct

## Keyword `struct`

- `struct` in rust is fundamentally different from `struct` in [C#](csharp-struct)

## Features

- An ownership-awaring type

## Tuple Structure

```rust
struct Pair(i32, f32);
```

## C-like Structure

[C-like structure](c-structure)

```rust
struct Point {
  x: f32,
  y: f32,
}
```

## Unit Structure

Declaration

- `struct Marker;`

Features

- Doesn't have any fields
