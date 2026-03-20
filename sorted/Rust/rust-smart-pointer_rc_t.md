# Rust Smart Pointer - Rc<T>

* [What It Is](#what-it-is)
* [Features](#features)
* [Why `Rc<T>`](#why-`rc<t>`)
* [Use Cases](#use-cases)
* [Get Reference Count](#get-reference-count)

## What It Is

- A shared ownership smart pointer
- It enables multiple ownership for same heap-allocated value

## Features

- `Rc<T>` is NOT thread safe, 
- `Arc<T>` is the thread-safe version of `Rc<T>`
- `Rc::clone(&value)`: create a new reference
- `Rc::strong_count(&value)`: get the reference count of the value

## Why `Rc<T>`

Why `Rc<T>` when Rust normally allows [single owner](rust-ownership#single-ownership-demonstration) for a value? There are some case multiple ownership is needed:

- [Graph structure](data-structure-graph) 
- Trees with shared nodes
- Multiple struct referencing same data

## Use Cases
- Here are two data that both want to own the same data

![smart-pointer](img/rust-smart-pointer-01.svg)

- To implement structure like picture shown, the code might look like
- `b` and `c` both want to own `a`
- but it disobeys [ownership rules](rust-ownership#ownership-rules) and causes compile error

```rust
enum List {
    Cons(i32, Box<List>),
    Nil,
}

use crate::List::{Cons, Nil};

fn main() {
    let a = Cons(5, Box::new(Cons(10, Box::new(Nil))));
    let b = Cons(3, Box::new(a));
    let c = Cons(4, Box::new(a));  // Error: use of moved value: `a`
}
```

- Its naturally think that `Cons` should hold a List reference, then the code may change to
- But lifetime annotation involved, 
- And more variables are needed to keep the data alive

```rust
enum List<'a> {
  Cons(i32, &'a List<'a>),
  Nil,
}

use crate::List::{Cons, Nil};

fn func() {
  let nil = Nil;
  let list_10 = Cons(10, &nil);
  // let list_10 = Cons(10, &Nil); // Error: temporary value dropped while borrowed
  let a = Cons(5, &list_10);
  let b = Cons(3, &a);
  let c = Cons(4, &a);
}
```

- Implement with `Rc<T>`

```rust
enum List {
    Cons(i32, Rc<List>),
    Nil,
}

use crate::List::{Cons, Nil};
use std::rc::Rc;

fn main() {
    let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
    let b = Cons(3, Rc::clone(&a));
    let c = Cons(4, Rc::clone(&a));
}
```

- Reference `a` with `a.clone()` are the same

## Get Reference Count

```rust
fn main() {
    let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
    println!("count after creating a = {}", Rc::strong_count(&a));
    let b = Cons(3, Rc::clone(&a));
    println!("count after creating b = {}", Rc::strong_count(&a));
    {
        let c = Cons(4, Rc::clone(&a));
        println!("count after creating c = {}", Rc::strong_count(&a));
    }
    println!("count after c goes out of scope = {}", Rc::strong_count(&a));
}
```

## Clone Method Return A Temporary Value


