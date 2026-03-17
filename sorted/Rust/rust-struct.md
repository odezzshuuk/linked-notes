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

## Instantiate a struct

Specify field values

```rust
struct Point {
  x: f32,
  y: f32,
}

let p = Point {
  x: 3.0,
  y: 4.0,
};
```

Shorthand

```rust
fn create_point(x: f32, y: f32) -> Point {
  Point { x, y }
}
```

## Unit Structure

What It Is

- Doesn't have any fields

Declaration

- `struct Marker;`

