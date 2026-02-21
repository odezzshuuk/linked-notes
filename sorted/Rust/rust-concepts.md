# Rust - Concepts

## Last-use Analysis

## Copy Type

- i32, u32, f64, bool, char, usize, isize
- tuple

## Move Type

- owns heap memory
- manage resources
- has destructor(drop)
- use [RAII](cpp-raii.md) semantics
- For example:
  - `String`
  - [Struct](rust-struct)
  - `Vec<T>`
  - `Box<T>`
  - `HashMap<K, V>`
  - `Rc<T>`
  - `Arc<T>`
  - `Mutex<T>`

Features

- Ownership should be aware

