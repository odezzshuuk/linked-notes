# Rust - Smart Pointers

## Summary

| Smart Pointer          | Main Trait(s) impl | Can be shared? | Can mutate through it?   | Thread-safe? | Heap allocation?     | Size on stack    |
| ---------------------- | ------------------ | -------------- | ------------------------ | ------------ | -------------------- | ---------------- |
| Box<T>                 | "Deref, DerefMut"  | ✗              | ✓                        | ✗            | Yes                  | usize (pointer)  |
| Rc<T>                  | Deref              | ✓              | ✗                        | ✗            | Yes                  | usize × 2        |
| Rc<RefCell<T>>         | Deref              | ✓              | ✓ (runtime check)        | ✗            | single-threaded"     | Yes,usize × 3–4  |
| Arc<T>                 | Deref              | ✓              | ✗                        | ✓            | Yes                  | usize × 2        |
| Arc<Mutex<T>>          | Deref              | ✓              | ✓ (mutex lock)           | ✓            | Yes                  | usize × 3–4      |
| Arc<RwLock<T>>         | Deref              | ✓              | ✓ (read or write lock)   | ✓            | Yes                  | similar to Mutex |
| Weak<T> / Weak<Arc<T>> | —                  | ✓ (but weak)   | ✗                        | ✓ / ✗        | —                    | usize × 2–3      |
| Cell<T>                | —                  | ✓              | ✓ (no borrow)            | ✗ (mostly)   | No (usually)         | same as T        |
| RefCell<T>             | Deref (via borrow) | ✓              | ✓ (runtime borrow check) | ✗            | Usually inside Rc    | usize × 3        |
| Mutex<T>               | —                  | —              | ✓ (via .lock())          | ✓            | No (can be on stack) | small + T        |
| RwLock<T>              | —                  | —              | ✓ (read/write locks)     | ✓            | No (can be on stack) | small + T        |

> Type that implements `Deref` trait can be treated like a reference

## Use Case

- `Box<T>`
- `Rc<T>`
- `Rc<RefCell<T>>`
- `Arc<T>`
- `Arc<Mutex<T>>`
- `Arc<RwLock<T>>`
- `Weak<T> / Weak<Arc<T>>`
- `Cell<T>`
- `RefCell<T>`
- `Mutex<T>`
- `RwLock<T>`

## `Box<T>`

When to use

- Generally say an unknown size type 
- Rank use case by frequency
  - recursive data structure, e.g. `enum List { Cons(i32, Box<List>), Nil }`
  - [trait object](), e.g. `Box<dyn Trait>`
  - large structs array, e.g. `Box<[u8; 1_000_000]>`

When not to use


