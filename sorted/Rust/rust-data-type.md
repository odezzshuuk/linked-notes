# Rust - Type

* [Scalar Type](#scalar-type)
* [Compound Type](#compound-type)
* [Tuple](#tuple)
* [Unit](#unit)
* [String](#string)
* [Slice/Array](#slice/array)

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

## String

[String](rust-string.md)

## Collections

[Collections](rust-collections.md)

