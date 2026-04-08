# Rust - Generic

## Functions

```rust
struct A;          // Concrete type `A`.
struct S(A);       // Concrete type `S`.
struct SGen<T>(T); // Generic type `SGen`.

// Define a function `generic` that takes an argument `_s` of type `SGen<T>`.
// Because `SGen<T>` is preceded by `<T>`, this function is generic over `T`.
fn generic<T>(_s: SGen<T>) {}

fn main() {
    // Using the non-generic functions
    gen_spec_i32(SGen(6)); // Implicitly specified type parameter `i32`.

    // Explicitly specified type parameter `char` to `generic()`.
    generic::<char>(SGen('a'));

    // Implicitly specified type parameter `char` to `generic()`.
    generic(SGen('c'));
}
```

- define: `fn generic<T>(_s: SGen<T>)`
- explicitly type call: `generic::<char>(SGen('a'))`, via `::<char>`
- implicitly type call: `generic('c')`

## Implementation

```rust
struct S;
struct GenericVal<T>(T);

impl GenericVal<f32> { }
impl GenericVal<S> { }

impl<T> GenericVal<T> { }
```

## Trait

```rust
struct A;
trait DoubleDrop<T> {
  fn double_drop(self, _: T);
}

// implement `DoubleDrop<String>` for A struct
impl DoubleDrop<String> for A {
  fn double_drop(self, _: String) { }
}
// implement `DoubleDrop<T>` for any type `U`
impl<T, U> DoubleDrop<T> for U {
  fn double_drop(self, _: T) { }
}
```

## Where Clause

[Where Clause](rust-where-clause.md)

