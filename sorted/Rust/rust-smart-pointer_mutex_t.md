# Rust - Mutex<T>

## What It Is

`Mutex<T>` is a smart pointer from `std::sync` that provides
mutual exclusion for shared data.

- `Mutex` stands for mutual exclusion
- Only one thread can access the protected value at a time
- Locking returns a guard object (`MutexGuard<T>`) that unlocks automatically when it is dropped

## Key Features

- Thread-safe interior mutability for multi-threaded programs
- Runtime lock acquisition (`lock()`) with automatic unlock via RAII
- Poisoning support: if a thread panics while holding the lock, later lock attempts return a `PoisonError`
- Usually combined with `Arc<T>` for shared ownership across threads

## What's For

- Use `Mutex<T>` when multiple threads must read and write the same value, and you need correctness before raw throughput.

## Get The Lock

Call `lock()` to get a guard

- `lock()` method blocks the local thread until it can acquire the lock
- `lock()` will not return on second call, it might panic or deadlock
- Return a `LockResult<MutexGuard<'_, T>>` type value
- An [RAII] guard is returned
- When the guard goes out of scope, the mutex will be unlocked

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
	let counter = Arc::new(Mutex::new(0_i32));
	let mut handles = Vec::new();

	for _ in 0..10 {
		let shared = Arc::clone(&counter);
		handles.push(thread::spawn(move || {
			let mut n = shared.lock().unwrap();
			*n += 1;
		}));
	}

	for handle in handles {
		handle.join().expect("worker thread panicked");
	}

	println!("counter = {}", *counter.lock().expect("mutex poisoned"));
}
```

- Commonly used pattern `mutex.lock().unwrap()`
  - `lock()` return `LockResult<MutexGuard<'_, T>>`
  - `unwrap()` return `MutexGuard<'_, T>` or panic if the lock is poisoned

## Poisoning

What Is Poisoning?

- Mutex get poisoned when a thread [panics](rust-error-handling#panic) while holding the lock
  - `lock()` will return an error when acquired
  - But The mutex still can be acquired
  - Acquired mutex will be contained in the returned error

> This means `lock()` and `try_lock()` will return a `Result`

```rust
fn func() {
  let mutex = Arc::new(Mutex::new(0));
  let mutex_clone = Arc::clone(&mutex);

  let handle = thread::spawn(move || {
    let mut data = mutex_clone.lock().unwrap();
    *data += 1;

    println!("Thread 1: Holding lock and about to panic...");
    panic!("Intentional panic to poison the mutex");
  });

  let _ = handle.join();

  match mutex.lock() {
    Ok(_) => println!("Successfully locked!"),
    Err(poison_err) => {
      println!("Error: The mutex is poisoned! {}", poison_err);

      let data = poison_err.into_inner();
      println!("Recovered data value: {}", *data);
    }
  }
}
```

- use `PoisonError.into_inner()` to get the data out of the poisoned mutex

## MutexGuard<T>

## Prefer alternatives when possible

- Use channels (`std::sync::mpsc`) for message passing
- Use atomics (`AtomicUsize`, etc.) for simple numeric state
- Use `RwLock<T>` when reads are much more frequent than writes



