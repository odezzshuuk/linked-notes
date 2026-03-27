# Rust - Method

* [Method Declaration](#method-declaration)
* [3 Kinds of `self` in method](#3-kinds-of-`self`-in-method)
* [Associated Function](#associated-function)
* [Method Auto-Deref](#method-auto-deref)
* [Method Call Resolution](#method-call-resolution)

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

## 2 Kinds Of Method In Rust

- [Instance method](#instance-methods)
- [Associated function](#associated-functions)

## Instance Methods

3 kinds of instance method

- `&self`: [immutable borrow]
- `&mut self`: [mutable borrow]: 
  - When involve instance [mutation](rust-variable-binding#declaration-default-immutable)
- `self`: [taking ownership]
  - Consume the instance
  - Usually used when the when [transforming]/[destroying] the instance

```rust
fn method(self);
fn method(&self);
fn method(&mut self);
```

- all the method are called with `value.method()`, but under the hood, what actually are called:
  - `value.method()`
  - `(&value).method()`
  - `(&mut value).method()`

## Associated Functions

- Defined in `impl` block but without `self` parameter
- Called by `::`, `Rectangle::square(3)`

```rust
impl Rectangle {
  fn square(size: u32) -> Self {
    Rectangle { width: size, height: size }
  }
}
```

- Declaration funtion that return `Self` is a common pattern for constructor-like method in Rust

```rust
impl Rectangle {
  fn new(width: u32, height: u32) -> Self {
    Rectangle { width, height }
  }
}
```

- this is a constructor-like behavior method in other languages
- `new()` is nothing special in Rust, just like a convention for constructor method

## Method Auto-Deref

In Rust

- Rust automatically adds `&`, `&mut`, or `*` as needed when calling a method
- `ptr.distance()` is equivalent to `(*ptr).distance()`

In c++

- if object is a pointer, use `->`
- `ptr->method()` is equivalent to `(*ptr).method()`


## Method Call Resolution

Rust not just [auto-deref](#method-auto-deref), but performs step-by-step search, for variable `p` as instance:

1. method on `p`
2. method on `&p`
3. method on `&mut p`
4. method on `*p`
5. if not found, repeat the 1-4 on `*p` 

For example:

- An instance of type `A` who can deref to `B`, and `B` can deref to `C`
- Method on `B` and `C` can be accessed by one dot(`.`) operator. For instance `let value = A(B(C))`
  - `value.method_on_b()`
  - `value.method_on_c()`
  - both ok

```rust
use std::ops::Deref;

struct C;
impl C {
    fn method_on_c(&self) {
        println!("C method");
    }
}

struct B(C);
impl B {
    fn method_on_b(&self) {
        println!("B method");
    }
}
impl Deref for B {
    type Target = C;

    fn deref(&self) -> &C {
        &self.0
    }
}

struct A(B);
impl Deref for A {
    type Target = B;

    fn deref(&self) -> &B {
        &self.0
    }
}

pub fn func() {
    let value = A(B(C));

    value.method_on_b(); // works
    value.method_on_c(); // also works
}
```

