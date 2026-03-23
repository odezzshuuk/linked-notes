# Rust - Deref Trait

## What's Deref Trait

```rust
fn main() {
    let x = 5;
    let y = &x;

    assert_eq!(5, x);
    assert_eq!(5, *y); } ```

Use `Box<T>` which implements `Deref` trait

```rust
fn main() {
    let x = 5;
    let y = Box::new(x);

    assert_eq!(5, x);
    assert_eq!(5, *y);
}
```

- when `*y` is evaluated, Rust actually performs `*(y.deref())`

## As contrast

- define `MyBox<T>`, a tuple struct, without implementing `Deref` trait

```rust
struct MyBox<T>(T);
imple<T> MyBox<T> {
    fn new(x: T) -> MyBox<T> {
        MyBox(x)
    }
}

fn main() {
    let x = 5;
    let y = MyBox::new(x);

    assert_eq!(5, x);
    assert_eq!(5, *y); // error: cannot dereference `MyBox<{integer}>`
}
```

- without `deref` trait, Rust can only dereference `&` references

## Implementing `Deref` trait

```rust
use std::ops::Deref;

impl<T> Deref for MyBox<T> {
    type Target = T;

    fn deref(&self) -> &T {
        &self.0
    }
}
```

- `Target` defines an associated type
- `.0` access the first field of the [tuple](rust-struct#tuple-struct) struct `MyBox<T>`

## Deref Coercion

What's It

- Convert references that implement `Deref` trait into references of another type

When It Happens

- When pass a reference to a particular type's value as an ARGUMENT to a **FUNCTION** or **METHOD CALL**

Deref Corecion is recursive

```rust
fn hello(name: &str) {
    println!("Hello, {}!", name);
}

fn func() {
    let name = Arc::new(String::from("Rust"));
    hello(&name);
}
```

- Chained Deref Coercion: `&Arc<String>` → `&String` → `&str`

## Mutable Deref Coercion

1. From `&T` to `&U` when T: `Deref<Target=U>`
2. From `&mut` `T` to `&mut U` when T: `DerefMut<Target=U>`
3. From `&mut T` to `&U` when T: `Deref<Target=U>`

## Deref In dot operator method access

[deref in method](rust-method#method-call-resolution)

