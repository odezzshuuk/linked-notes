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
> Type that implements `Drop` trait can be cleaned up when goes out of scope

## Deref Trait


```rust

```

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
  - [trait object](rust-trait#trait-object), e.g. `Box<dyn Trait>`
  - large structs array, e.g. `Box<[u8; 1_000_000]>`
  - ...
- recursive type and trait object take 60%~70% use case of `Box<T>`

## `Rc<T>`

[`Rc<T>`](rust-smart-pointer_rc_t.md): Ownership sharing smart pointer

## `RefCell<T>`

[`RefCell<T>`](rust-smart-pointer_refcell_t.md): Interior mutability smart pointer

## `Rc<RefCell<T>>`

> value wrapped by `Rc` and `RefCell` has the similar mechanism as [JavaScript object](javascript-object.md)

- `Rc<RefCell<T>>` is a common combination to achieve
  - shared ownership, heap allocation
  - interior mutability

## Arc<T>

- `Arc<T>` is the thread-safe version of [`Rc<T>`](#rct)

## Mutex<T>

[`Mutex<T>`](rust-smart-pointer_mutex_t.md): Mute inside `Arc<T>`

## Arc<Mutex<T>>

