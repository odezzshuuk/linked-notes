# Rust - Trait

* [What's Trait](#what's-trait)
* [Features](#features)
* [keyword `impl`](#keyword-`impl`)
* [Declaration](#declaration)
* [Implementing A Trait](#implementing-a-trait)
* [Trait As Parameter Type Annotation ](#trait-as-parameter-type-annotation-)
* [Trait As Return Type Annotation](#trait-as-return-type-annotation)
* [Trait As Generic type parameter](#trait-as-generic-type-parameter)
* [Trait Bound](#trait-bound)
* [Trait Members](#trait-members)
* [Supertrait](#supertrait)
* [Trait Object](#trait-object)

## What's Trait

- A trait define shared method signatures that types can implement

## Features

- Trait Can't directly be used at where size is not known at compile time

## keyword `impl`

- implementing trait: `impl TraitName for TypeName { ... }`
- as type annotation: `fn function_name(param: impl TraitName) { ... }`

## Declaration

```rust
pub trait Summary {
    fn summarize(&self) -> String;
}

// trait provide default implementation 
pub trait Display {
    fn display(&self) -> String {
        String::from("(Read more...)")
    }
}
```

## Implementing A Trait

```rust
impl Summary for NewsArticle {
    fn summarize(&self) -> String {
        format!("{}, by {} ({})", self.headline, self.author, self.location)
    }
}
```

## Trait As Parameter Type Annotation

```rust
fn notify(item: &impl Summary) {
    println!("Breaking news! {}", item.summarize());
}
```

vs `&dyn Summary`

```rust
fn func_1(a: &impl Animal) {
  a.run();
}
fn func_2(a: &dyn Animal) {
  a.run();
}
let x = if cond { &Dog } else { &Cat };
func_1(x); // error: `if` and `else` have incompatible types
func_2(x); // OK
```

## Trait As Return Type Annotation

When use Trait as return type

- Keyword `impl` is required 
- It is not allow to return different types even they both implement the demanded trait

```rust
pub trait Summary {
  fn summarize(&self) -> String;
}

pub struct GoodNews { }
impl Summary for GoodNews {
  fn summarize(&self) -> String {
    return String::from("This is a good news!");
  }
}

pub struct BadNews { }
impl Summary for BadNews {
  fn summarize(&self) -> String {
    return String::from("This is a bad news!");
  }
}
pub fn returns_summarizable(switch: bool) -> impl Summary {
  if switch {
    GoodNews { }
  } else {
    BadNews { }  // Error: `if` and `else` have incompatible types
  }
}
```

## Trait As Generic type parameter

```rust
fn notify<T: Summary>(item: &T) {
    println!("Breaking news! {}", item.summarize()); 
} 
```

## Trait Bound

> like [generic constraint in c#](csharp-generic-constraint.md)

```rust
pub fn notify(item: &(impl Summary + Display)) { }
pub fn notify<T: Summary + Display>(item: &T) { }
```

- item must implement both `Summary` and `Display` traits

Function with multiple generic type parameters write like this

```rust
pub fn notify<T: Summary + Display, U: Clone + Debug>(item: &T, other: &U) -> i32 { }
```

- Or use `where` to for more clearer

```rust
pub fn notify<T, U>(item: &T, other: &U) -> i32
where T: Summary + Display,
      U: Clone + Debug
{ }
```

`'static` trait bound, `T: 'static`

- Reprensent the type `T` must not contain any non-static reference
- For following function signature

```rust
fn func<T: 'static>(p: &T) { }
```

- both `ExampleA`, `ExampleB` type value can be passed to `func`
- `ExampleC` is not fit the function

```rust
struct ExampleA {
  x: i32,
  y: i32,
}

struct ExampleB {
  x: i32,
  y: i32,
  name: &'static str,
}

struct ExampleC<'a> {
  x: i32,
  y: i32,
  name: &'static str,
  desc: &'a str,
}
```

## Trait Members

[Methods](rust-method.md)

[Associated Types](rust-associated-types.md)

[Associated Constants]

## Supertrait

For instance, struct `User`, and traits `Person`, `Student`, `Programmer`, and `ComSciStudent`

```rust
struct User {
  username: String,
  email: String,
}
trait Person {
  fn name(&self) -> String;
}
trait Student: Person {
  fn grade(&self) -> u8;
}
trait Programmer {
  fn fav_language(&self) -> String;
}
trait ComSciStudent: Programmer + Student {
  fn git_username(&self) -> String;
} 
```

Any type that want to implement `subTrait` must also implement all the super trait

- for example, to implement `ComSciStudent`, the type must also implement `Programmer` and `Student`

## Trait Object

[Trait Object](rust-trait-object.md): Dynamic dispatch of trait methods

## Trait Receiver

```rust
trait Example { 
    fn foo(&self);
}
```

- `&self` is the receiver
- Also represent the instance that calls the method

Smart Pointer As Receiver

```rust
trait A {
  fn method_a(self: Box<Self>);
}
struct Point { x: i32, y: i32 }
impl Example for Point {
  fn method_a(self: Box<Self>) {
    println!("Point({}, {})", self.x, self.y);
  }
}
fn func() {
  let p = Box::new(Point { x: 3, y: 5 });
  p.method_a();
}
```
