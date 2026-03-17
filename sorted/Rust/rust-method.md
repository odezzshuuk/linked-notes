# Rust - Method

## Method Declaration

- Method are function defined in the context of a struct, enum, or trait object
- Their first parameter is always `self`, which represents the instance of the type that the method is being called on
- `impl TypeName { fn methodName(&self) -> ReturnType { ... } }` 

```rust
struct Rectangle {
  width: u32,
  height: u32,
}
impl Rectangle {
  fn area(&self) -> u32 {
    self.width * self.height
  }
}
```

## 3 Kinds of `self` in method

- `&self`: [immutable borrow]
- `&mut self`: [mutable borrow]: 
  - When involve instance [mutation](rust-variable-binding#declaration-default-immutable)
- `self`: [taking ownership]
  - Consume the instance
  - Usually used when the when [transforming]/[destroying] the instance

## Associated Function

- Defined in `impl` block but without `self` parameter
- Called by `::`, `Rectangle::square(3)`

Constructor-like method in other languages

```rust
impl Rectangle {
  fn square(size: u32) -> Self {
    Rectangle { width: size, height: size }
  }
}
```

- Declaration funtion that return `Self` is a common pattern for constructor-like method in Rust
- `new()` is nothing special in Rust, just like a convention for constructor method

## Method Auto-Deref

In c++

- if object is a pointer, use `->`
- `ptr->method()` is equivalent to `(*ptr).method()`

In Rust

- Rust automatically adds `&`, `&mut`, or `*` as needed when calling a method
- `ptr.distance()` is equivalent to `(*ptr).distance()`

