# Rust Smart Pointer - RefCell<T>

## What It Is

`RefCell<T>` is a smart pointer that enforces **borrow rules at runtime** rather than at compile time.

## Key feature

- Allows you to mutate contents through an immutable reference
- Uses **interior mutability** pattern for runtime borrow checking
- Tracks borrows dynamically and panics if rules are violated
- Useful when the compiler can't prove correctness but you know the code is safe

## What's It For

Use `RefCell<T>` when:

- You have a single owner but need mutable access from an immutable reference
- You're implementing patterns like shared state in event handlers or testing
- You need interior mutability without the overhead of locking (like `Mutex<T>`)
- The single-threaded constraint is acceptable for your use case

Limitations:

- **Not thread-safe** — single-threaded only
- Use [`Mutex<T>`](rust-smart-pointer_mutex_t.md) for multi-threaded scenarios

## Examples

**The problem without RefCell:**

```rust
struct Cache {
    data: Vec<String>,  // ❌ Can't mutate this through &self
}

impl Cache {
    fn get_or_insert(&self, key: &str) -> String {
        // ❌ Won't compile: can't modify through &self
        // self.data.push(key.to_string());
        key.to_string()
    }
}
```

**Solution with RefCell - caching pattern:**

RefCell is necessary here because caching requires mutation but APIs typically expose `&self` methods:

```rust
use std::cell::RefCell;

struct Cache {
    data: RefCell<Vec<String>>,  // ✅ Interior mutability
}

impl Cache {
    fn new() -> Self {
        Cache { data: RefCell::new(Vec::new()) }
    }

    fn get_or_insert(&self, key: &str) -> String {
        // ✅ Can mutate cache through &self
        let mut cache = self.data.borrow_mut();
        
        if let Some(value) = cache.iter().find(|s| s == &key) {
            return value.clone();
        }
        
        cache.push(key.to_string());
        key.to_string()
    }
}

fn main() {
    let cache = Cache::new();
    cache.get_or_insert("hello");  // &self, not &mut self
    cache.get_or_insert("world");
    
    println!("Cached: {:?}", cache.data.borrow());
}
```

Why RefCell is necessary:
- Caching is logically immutable from the caller's perspective
- Internal state needs to change for performance optimization
- Cannot change API to require `&mut self` without breaking the abstraction

## Tips & Tricks

- **Error handling**: Use `try_borrow()` and `try_borrow_mut()` for graceful failure handling instead of panicking
- **Reference cycles**: Be careful with `RefCell` inside `Rc<T>` as circular references can cause memory leaks
- **Thread safety**: If needed, use `Arc<Mutex<T>>` instead
- **Borrow scope**: Keep borrows as short as possible by using explicit blocks `{ let borrow = ... }`

