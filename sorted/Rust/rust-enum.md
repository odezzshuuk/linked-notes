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
    }

    if let Message::Move { x, y } = msg {
        println!("Move to x:{x}, y:{y}");
    }
}
```

## Option Enum
