# Rust - Handle Null

- A special enum in Rust std library
- `Some(T)` is something like 
  - `T | undefined` in TypeScript
  - `T?` in C#

```rust
enum Option<T> {
    None,
    Some(T),
}
```

Why `Option<T>`?

- Rust doesn't have `null`
- Rust use `Option<T>` to represent a value that can be either something or nothing

## Use Cases

1. Return value that might not exist

```rust
fn find_user_by_id(id: u64) -> Option<User> { ... }
fn get_config_value(key: &str) -> Option<String> { ... }
```

2. Handle optional parameters

- Rust use `Option<T>` to represent optional parameters, must explicitly pass into
- ...

```rust
let title = String::from("Dr.");
fn greet(name: &str, title: Option<&str>) {
    match title {
        Some(t) => println!("Hello, {} {}!", t, name),
        None => println!("Hello, {}!", name),
    }
}

greet("Alice", Some(&title));
greet("Bob", None);
greet("Charlie");   // Error
```

## unwrap_or_else

> Another `unwrap_or_else` of two is [here](rust-error-handling#unwrap_or_else)

Method Signature

```rust
impl<T> Option<T> {
    pub fn unwrap_or_else<F>(self, f: F) -> T
    where
        F: FnOnce() -> T
    {
        match self {
            Some(x) => x,
            None => f(),
        }
    }
}
```

- `F`: the [closure](rust-closure.md) type

Use cases

```rust
let some_val = Some("hello");
let none_val: Option<&str> = None;
let result1 = some_val.unwrap_or_else(|| "default");  // result1 is "hello"
let result2 = none_val.unwrap_or_else(|| "default");  // result2 is "default"
```

