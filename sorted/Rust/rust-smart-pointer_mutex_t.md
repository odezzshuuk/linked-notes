# Rust - Mutex<T>

## What It Is

`Mutex<T>` is a smart pointer from `std::sync` that provides
mutual exclusion for shared data.

- `Mutex` stands for mutual exclusion
- Only one thread can access the protected value at a time
- Locking returns a guard object (`MutexGuard<T>`) that unlocks automatically
  when it is dropped

## Key Features

- Thread-safe interior mutability for multi-threaded programs
- Runtime lock acquisition (`lock()`) with automatic unlock via RAII
- Poisoning support: if a thread panics while holding the lock, later lock attempts return a `PoisonError`
- Usually combined with `Arc<T>` for shared ownership across threads

## What's It For

- Use `Mutex<T>` when multiple threads must read and write the same value, and you need correctness before raw throughput.

Typical use cases:

- Shared counters and metrics
- Shared in-memory state in servers
- Shared caches or maps with simple access patterns

Prefer alternatives when possible:

- Use channels (`std::sync::mpsc`) for message passing
- Use atomics (`AtomicUsize`, etc.) for simple numeric state
- Use `RwLock<T>` when reads are much more frequent than writes

## How To Use

Basic pattern:

- Wrap state in `Mutex<T>`
- Wrap that mutex in `Arc<T>` if multiple threads own it
- Call `lock()` to get a guard
- Access data through the guard
- Let guard go out of scope quickly to reduce contention

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
	let counter = Arc::new(Mutex::new(0_i32));
	let mut handles = Vec::new();

	for _ in 0..10 {
		let shared = Arc::clone(&counter);
		handles.push(thread::spawn(move || {
			let mut n = shared.lock().expect("mutex poisoned");
			*n += 1;
		}));
	}

	for handle in handles {
		handle.join().expect("worker thread panicked");
	}

	println!("counter = {}", *counter.lock().expect("mutex poisoned"));
}
```

Run:

```bash
cargo run
```

## Why Mutex<T>


