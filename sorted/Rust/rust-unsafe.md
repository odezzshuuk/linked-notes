# Rust - Unsafe

## What's `unsafe`

- create a locally scoped to perform operations that the Rust compiler can't guarantee to be safe
- So programmer takes responsibility for safety

## Why `unsafe`

- Because some things are provably safe in reality but not provably to the compiler

## What can do with `unsafe`

| Action                                          | Normally forbidden by compiler? | Allowed inside unsafe? | Main danger if you get it wrong              |
| ----------------------------------------------- | :-----------------------------: | :--------------------: | -------------------------------------------- |
| "Dereference a raw pointer (\*const T \*mut T)" |               Yes               |          Yes           | "Use-after-free, null pointer, misaligned"   |
| Call an unsafe fn                               |               Yes               |          Yes           | Whatever the function promises not to do     |
| Implement unsafe trait                          |      Yes (for some traits)      |          Yes           | Breaking trait contract (very common!)       |
| Access or modify a static mut                   |               Yes               |          Yes           | "Data races, UB"                             |
| Union field access (mutable)                    |       Yes (in safe Rust)        |          Yes           | Breaking type invariants                     |
| Call FFI functions                              |   Yes (most FFI is unsafe fn)   |          Yes           | C / other language can do literally anything |
| Transmute between types                         |               Yes               |          Yes           | Creating invalid values of any type          |

```rust
unsafe {
  *ptr = value;
  prt.write(value);
  ptr.read();
  ptr.offset(3).write(42)
}
```
