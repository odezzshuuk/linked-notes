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

## String

[String](rust-string.md)


## Slice/Array

- Slice type is `&[T]`, `[T]` represents a sequence of `T` values
- For string slice, it is `&str`
- Slice reference stores: 
  - a pointer to the first element of the slice
  - the length of the slice

String Slice

```rust
let s = String::from("hello world");

let hello = &s[0..5];
let world = &s[6..11];
```

Other Slice

```rust
let a = [1, 2, 3, 4, 5]; // type of a: [i32; 5]
let slice = &a[1..3]; // type of slice: &[i32]
```

- Syntax Sugar

```rust
let a = [3; 5]; // [3, 3, 3, 3, 3]
```

When use slice as generic type parameter

- `&[T]` is slice type, it has a pointer and a length, and it is sized type
- `[T]` is the value of slice type point to, it is unsized type

