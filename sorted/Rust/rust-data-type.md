# Rust - Type

## Scalar Type

- The type represents a single value. 
- Rust has four primary scalar types
  - integers
  - floating-point numbers
  - Booleans characters

## Compound Type

- [Tuple](#tuple)
- [Array](#array)

## Tuple

```rust
fn main() {
  let t: (i32, f64, u8) = (500, 6.4, 1);
  // Get value from tuple with pattern
  let (x, y, z) = t; 

  // Access tuple element by index
  let five_hundred = t.0; // access tuple element by index
  println!("The value of y is: {}", y);
}
```

- Access tuple element by index

## Unit

- A special [tuple](#tuple) without any value
- Unit type value: `()`

## Array

- Normal Declaration

```rust
let a: [i32; 5] = [1, 2, 3, 4, 5];
```

- Syntax Sugar

```rust
let a = [3; 5]; // [3, 3, 3, 3, 3]
```

## String

Declaration

```rust
let s = String::from("hello")
```

What's `str`

- dynamically sized type
- never use `str` directly
 
Relationship between `String` and `str`

- `String` essentially is a wrapper around a vector of bytes (`Vec<u8>`)
- `String` implements the [`Deref` trait](rust-deref-trait.md)

```rust
Derf<Target = str>
```

