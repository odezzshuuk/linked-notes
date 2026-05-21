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

```rust
pub fn func() {
  let v = vec![1, 2, 3];
  let print_v = || println!("Here's a vector: {v:?}");
  let handle = thread::spawn(move || {
    println!("Here's a vector: {v:?}");
  });
}
```

- Keyword [`move`](rust-closure#closure-taking-ownership) is required for taking the ownership of the variable outside the closure

Why needs `move`? 

- look at the signature of `thread::spawn()`

```rust
pub fn spawn<F, T>(f: F) -> JoinHandle<T>
where
    F: FnOnce() -> T,
    F: Send + 'static,
    T: Send + 'static,
{
    Builder::new().spawn(f).expect("failed to spawn thread")
}
```

- `'static` the closure cannot borrow anything with a shorter lifetime
- `Send` the closure()

