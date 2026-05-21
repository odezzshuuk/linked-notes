# Rust - Future

## What It Is

- It is just a trait in core library

```rust
pub trait Future {
    type Output;
    fn poll(self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Self::Output>;
}
```

- It also a passive state machine
- passive means
  - `poll()` never called by user
  - Does nothing until an executor(like 'Tokio') calls `poll()`

## How It Works

