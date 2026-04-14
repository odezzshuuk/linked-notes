# Rust - Collections

## Overview

```rust
let numbers = [1, 2, 3, 4, 5];  // This is an array, type of numbers: [i32; 5]
let slice = &numbers[1..4]; // This is a slice, type of slice: &[i32]
let vec = vec![1, 2, 3, 4, 5]; // This is a vector, type of vec: Vec<i32>
```

- vector is dynamic size, heap allocated

## Slices

- Slice type is `&[T]`. 
  - A reference of `[T]`
  - `[T]` represents a sequence of `T` values, or called array
- For string slice, it is `&str`
- Slice **Reference** stores: 
  - a pointer to the first element of the slice
  - the length of the slice


String Slice

```rust
let s = String::from("hello world");

let hello = &s[0..5];
let world = &s[6..11];
```

`i32` Slice

```rust
let a = [1, 2, 3, 4, 5]; // type of a: [i32; 5]
let a_slice = &a[1..3]; // type of slice: &[i32]
let b = [3; 5]; // [3, 3, 3, 3, 3]
```

Slice as generic type parameter

- `&[T]` is slice type, it has a pointer and a length, and it is sized type
- `[T]` is the value of slice type point to, it is unsized type

## Vectors

Initialization

```rust
// Rust Vec initialization
let numbers = vec![1, 2, 3, 4, 5];  // vec! macro
let empty: Vec<i32> = Vec::new();   // Type annotation needed for empty
let sized = Vec::with_capacity(10); // Pre-allocate capacity

// From iterator
let from_range: Vec<i32> = (1..=5).collect();
let from_array = vec![1, 2, 3];
```

Operations

```rust
// Rust Vec operations
let mut vec = vec![1, 2, 3];

vec.push(4);                    // Add element
vec.insert(0, 0);               // Insert at index
vec.retain(|&x| x != 2);        // Remove elements (functional style)
vec.remove(1);                  // Remove at index
vec.clear();                    // Remove all

let first = vec[0];             // Index access (panics if out of bounds)
let safe_first = vec.get(0);    // Safe access, returns Option<&T>
let count = vec.len();          // Get count
let contains = vec.contains(&3); // Check if contains
```

## Map


## Work With Collections

```rust
fn process_numbers(numbers: &[i32]) {
    for &num in numbers {
        println!("Processing number: {}", num);
    }
}

fn func() {
    let array = [1, 2, 3, 4, 5];
    let vec = vec![1, 2, 3, 4, 5];
    
    // Same function works with both!
    process_numbers(&array);      // Array as slice
    process_numbers(&vec);        // Vector as slice
    process_numbers(&vec[1..4]);  // Partial slice
}
```

