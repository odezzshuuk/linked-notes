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

- keyword `move`

```rust
pub fn func_3() {
  let v = vec![1, 2, 3];
  let print_v = || println!("Here's a vector: {v:?}");
  let handle = thread::spawn(move || {
    println!("Here's a vector: {v:?}");
  });
}
```

- `move` perform on actually copy for [copy type](rust-concepts#copy-value)

```rust
pub fn func() {
  let mut counter = 0;
  let mut handles = vec![];

  for _ in 0..10 {
    let handle = thread::spawn(move || {
      counter += 1;
    });
    handles.push(handle);
  }

  let mut increment_by_one = || counter += 1;
  increment_by_one();

  for handle in handles {
    handle.join().unwrap();
  }

  println!("Final counter value: {}", counter);
}
```

- Final counter value is always 1,
- Because `counter` is copied into each thread and the main thread, 
- So they all have their own separate `counter` variable

