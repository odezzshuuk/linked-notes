# Rust - Trait `Sized`

## What It Is

- Type that implements `Sized` trait has a knon size at compile time

## Features

- Not [dyn compatible](rust-trait-object.md#dyn-comatibility)
- Automatically implemented for everything whose size is known at compile time

All [type parameter](rust-generic) have an implicit [bound](rust-trait.md#trait-bound) of `Sized`

- So type with generic is naturally uncompatible with trait object.

`T: ?Sized` To remomve the implicit `Sized` bound

```rust
struct Foo<T>(T);
struct Bar<T: ?Sized>(T);

struct FooUse(Foo<[i32]>);  // error: the trait `Sized` is not implemented for `[i32]`
struct BarUse(Bar<[i32]>);
```

Trait does not have an implicit `Sized` bound

- So a simple trait is always dyn compatible
- But `Sized` is allowed to be a supertrait of a trait, the trait won't be able to used it as a [trait object]()

```rust
trait Foo { }
trait Bar: Sized { }

struct Impl;
impl Foo for Impl { }
impl Bar for Impl { }

let x: &dyn Foo = &Impl;    // OK
// let y: &dyn Bar = &Impl; // error: the trait `Bar` cannot be made into an object
```

