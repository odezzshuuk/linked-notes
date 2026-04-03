# Rust - Thread

## Spawn a thread

```rust
fn func() {
    std::thread::spawn(|| {
        println!("Hello from a thread!");
    });
}
```

## Closure In Thread

- keyword [`move`](rust-closure#closure-ownership-and-borrow-rules)

```rust
pub fn func_3() {
  let v = vec![1, 2, 3];
  let print_v = || println!("Here's a vector: {v:?}");
  let handle = thread::spawn(move || {
    println!("Here's a vector: {v:?}");
  });
}
```

