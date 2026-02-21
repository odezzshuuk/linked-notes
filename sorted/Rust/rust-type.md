# Rust - Type

## Scalar Type

- The type represents a single value. 
- Rust has four primary scalar types
  - integers
  - floating-point numbers
  - Booleans
  - characters

## Compound Type

Tuple Type

```rust
fn main() {
  let tup: (i32, f64, u8) = (500, 6.4, 1);
  let (x, y, z) = tup; // get value from tuple
  println!("The value of y is: {}", y);
}
```

Array Type

- Normal Declaration

```rust
let a: [i32; 5] = [1, 2, 3, 4, 5];
```

- Syntax Sugar

```rust
let a = [3; 5]; // [3, 3, 3, 3, 3]
```
