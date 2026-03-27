# Rust - Trait Object

* [What It Is](#what-it-is)
* [Declaration](#declaration)
* [Trait `Sized`](#trait-`sized`)
* [What Is Dynamic Dispatch](#what-is-dynamic-dispatch)
* [Dyn Compatibility](#dyn-compatibility)
* [Associated Function Dispatchable](#associated-function-dispatchable)
* [VS Trait Bound](#vs-trait-bound)
* [VS `impl TraitName`](#vs-`impl-traitname`)

## What It Is

- Rust use trait object to achieve [dynamic dispatch(polymorphism)](#dynamic-dispatch)
- It is not a concrete object

It is actually a fat pointer

- Why it is a pointer
  - Dynamic [Sized Type](#trait-sized) is always put behind a pointer
- Why it is fat, because it contains two pointer:
  - one point to the data
  - one point the vtable

- [Dyn compatibility](#dyn-comatibility) defines when `dyn Trait` is valid

## Declaration

Use `dyn` keyword

- `dyn TraitName`

## Trait `Sized`

[Trait `Sized`](rust-trait-sized.md)

## What Is Dynamic Dispatch

- Method to call is determined at runtime, not compile time
- Rust will search method in the [vtable](c++-virtual-function-vtable) of the trait object

```rust
trait Shape {
    fn area(&self) -> f64;
}

struct Circle {
    radius: f64,
}
struct Rectangle {
    width: f64,
    height: f64,
}

impl Shape for Circle {
    fn area(&self) -> f64 {
        3.14 * self.radius * self.radius
    }
}
impl Shape for Rectangle {
    fn area(&self) -> f64 {
        self.width * self.height
    }
}

fn print_area(shape: &dyn Shape) {
    println!("Area = {}", shape.area());
}
fn main() {
    let c = Circle { radius: 2.0 };
    let r = Rectangle { width: 3.0, height: 4.0 };

    print_area(&c);
    print_area(&r);
}
```

## Dyn Compatibility

In One Words 

- `Sized` trait is not dyn compatible

A trait can be the base trait of a trait object if it has the following qualities:

- All [supertraits]() must also be dyn compatible
- [`Sized`] must not be `supertrait`. such as: 
  - `trait SuperA: Sized`
  - `trait SuperA where Self: Sized`
- It must not have any [associated constants](rust-trait#trait-members)
- It must not have any associated types with generic parameters
- [Associated functions must dispatchable](#associated-function-dispatchable)
- It explicitly non-dispatchable require

## Associated Function Dispatchable

- All associated functoins must either be [dispatchable](#dynamic-dispatch) from a trait object or be explicitly non-dispatchable. 

Dispatchable functions must:

1. Not have any type parameters
2. Be a method that does not use `Self` except in the type of the [receiver](rust-trait#trait-receiver)

```rust
trait Foo {
    fn foo(&self);            // dispatchable
    fn foo(&self);            // dispatchable
    fn foo(&mut self);        // dispatchable
    fn foo(self: Box<Self>);  // dispatchable
    fn bar(&self) -> Self;    // not dispatchable
}
```

3. Have a [receiver]() with one of the following types:

- `&Self` (i.e. `&self`)
- `mut Self`(i.e. `&mut self`)
- `Box<Self>`(i.e. `self: Box<Self>`)
- `Rc<Self>`(i.e. `self: Rc<Self>`)
- `Arc<Self>`(i.e. `self: Arc<Self>`)
- `Pin<P>` where `P` is one of the types above 

4. Not have an opaque return type, which means:

- Not have an `async fn`
- Not have a return position `impl Trait` type(`fn func(&self) -> impl Trait`)

## VS Trait Bound

[Trait bound](rust-trait#trait-bound) 

- For helping define generic type parameters
- For restricting generic type parameters

```rust
fn func<T: TraitName>(x: T) {
    // ...
}

fn func<T: dyn TraitName>(x: T) {   // is not allowed

}
```

Trait object

- For Passing to generic type parameters with polymorphic behavior

```rust
struct Example {
  field: Box<dyn TraitName>,
}
```

## VS `impl TraitName`

## Define Generic Function With Unknown Sized Type Parameters

```rust
struct S { }
trait A { }
impl A for S { }

fn func<T: ?Sized>(x: &T) {
    // ...
}
fn main() {
  let s = S { };
  func::<dyn A>(&s);
}
```

- Because generic type parameters have an [implicit `Sized` bound](rust-trait-sized.md#Features)
- So `fn func<T>(x: &T)` is not allowed to be called with `dyn A` as type parameter

