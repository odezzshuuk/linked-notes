# Rust - Enum

## What's It

- Enum but not on enum

## Declaration

```rust
enum IpAddr {
    V4(String),
    V6(String),
}

enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}
```

## Usage

`match`

```rust
enum Message {
    Quit,                        // no data
    Move { x: i32, y: i32 },     // struct-like
    Write(String),               // tuple-like
    ChangeColor(i32, i32, i32),  // tuple-like
}
fn describe(msg: Message) {
    match msg {
        Message::Quit => { println!("Quit message – no data"); }
        Message::Move { x, y } => { println!("Move to x:{x}, y:{y}"); }
        Message::Write(text) => { println!("Text message: {text}"); }
        Message::ChangeColor(r, g, b) => { println!("Color change: RGB({r}, {g}, {b})"); }
        _ => { println!("Unknown message"); }
    }
}

- `-` to match all other cases

let msg = Message::Move { x: 10, y: 20 };
describe(msg);
```

`if let`

```rust
let msg = Message::Move { x: 10, y: 20 };
if let Message::Move { x, y } = msg {
    println!("Move to x:{x}, y:{y}");
} else {
    println!("Not a Move message");
}
```

## Option

- A special enum in Rust std library
- Rust doesn't have `null`
- Rust use `Option<T>` to represent a value that can be either something or nothing

```rust
enum Option<T> {
    None,
    Some(T),
}
```

Usage

1. Return value that might not exist

```rust
fn find_user_by_id(id: u64) -> Option<User> { ... }
fn get_config_value(key: &str) -> Option<String> { ... }
fn parse_number(s: &str) -> Option<i32> { s.parse().ok() }
```

2. Handle optional parameters

- Rust use `Option<T>` to represent optional parameters, must explicitly pass into
- 

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

