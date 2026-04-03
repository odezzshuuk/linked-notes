# Rust - Lifetime

* [What's Lifetime](#what's-lifetime)
* [How To Annotate Lifetime](#how-to-annotate-lifetime)
* [Why Lifetime Annotation](#why-lifetime-annotation)
* [Static lfietime](#static-lfietime)
* [Struct Lifetime Annotation](#struct-lifetime-annotation)
* [Method Lifetime Annotation](#method-lifetime-annotation)

## What's Lifetime

- Also called Non-Lexical Lifetime
- Lifetime is another kind of generic type parameter
- Lifetime is apply to compile-time borrow(`&,` `&mut`)
- Not runtime borrow, such [`RefCell<T>`](rust-smart-pointer_refcell_t.md#borrow_mut()-and-borrow())

Take A Look

- `x` does not live long enough to be referenced by `r`

```rust
fn main() {
    let r;                // ---------+-- 'a
                          //          |
    {                     //          |
        let x = 5;        // -+-- 'b  |
        r = &x;           //  |       |  // error
    }                     // -+       |
                          //          |
    println!("r: {r}");   //          |
}                         // ---------+
```

- `x` lifetime larger than `r`, so `r` can reference `x`

```rust
fn main() {
    let x = 5;            // ----------+-- 'b
                          //           |
    let r = &x;           // --+-- 'a  |
                          //   |       |
    println!("r: {r}");   //   |       |
                          // --+       |
}                         // ----------+
```

## How To Annotate Lifetime

Define a lifetime

```rust
fn func<'a>(x: &'a str) -> &'a str { x }
struct Point<'a> { }
```

- `<'a>` is the definition of a lifetime parameter named `'a`

Annotate parameters and return type

```rust
&'a i32  // a reference with an explicit lifetime
&'a mut i32  // a mutable reference with an explicit lifetime
```

In function

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
  if x.len() > y.len() {
    x 
  } else {
    y 
  }
}
```

## Why Lifetime Annotation

Here is a function

```rust
fn longest(x: &str, y: &str) -> &str {  // error: missing lifetime specifier
  if x.len() > y.len() {
    x 
  } else {
    y 
  }
}
```

- For other type safe language(c++, c#, typescript), return type annotated `&str`, while the function indeed return a `&str`, that's fine
- Rust is not only a type safe language, but also a **Memory Safe Language**
- So Rust compiler has the feature to detect whether the returned reference fit the return lifetime annotation in function signature.


Back to the given function

- This is how to correctly annotate lifetime for this function

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
  if x.len() > y.len() {
    x 
  } else {
    y 
  }
}
```

- **Borrow checker** always know the lifetime of each reference in that function
- lifetime annotation is like that: 
  - you tell the borrow checker what you want to do
  - Let borrow checker check whether you do it right

```rust
fn longest<'a, 'b>(x: &'a str, y: &'b str) -> &'a str {
  if x.len() > y.len() {
    x 
  } else {
    y  // error
  }
}
```

- this function return a reference whose [lifetime]() named `'a`
- Incorrectly return `y` whose lifetime is `'b` will be avoid
- Lifetime annotation does not change the lifetime of the reference

## Struct Lifetime Annotation

```rust
struct A<'a> {
  data: &'a str,
}
```

## Static lfietime

> like [static member in c#](csharp-class#members), or typescript

- A reference is valid for the entire program

```rust
struct B {
  data: &'static str,
}
```

## Method Lifetime Annotation

```rust
impl<'a> ImportantExcerpt<'a> {
    fn announce_and_return_part(&self, announcement: &str) -> &str {
        println!("Attention please: {announcement}");
        self.part
    }
}
```

- first `<'a>` is the declaration of the lifetime parameter  
- second `<'a>` is the using

## Generic Type Parameter Syntax With Lifetime

- just another generic type parameter

```rust
use std::fmt::Display;
fn longest_with_an_announcement<'a, T>(x: &'a str, y: &'a str, ann: T) -> &'a str
where
    T: Display,
{
    println!("Announcement! {}", ann);
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```


