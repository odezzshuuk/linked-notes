# Rust - Closure

## What's It

> Similar concept: [Closure](javascript-closure.md) 

```rust
let x = 10;
let f = |y: i32| x + y;  // `f` is a closure that captures `x` from the environment
```

## What's Captured Variable

- varible outside the closure

## Closure Ownership and Borrow Rules

Borrowing immutably

```rust
let list = vec![1, 2, 3];
let only_borrows = || println!("{:?}", list);
let borrows_mutably = || list.push(4); // error
```

Borrowing mutably

- variable must be mutable
- closure must be mutable

```rust
let mut list = vec![1, 2, 3];
let mut borrows_mutably = || list.push(4);
borrows_mutably(); // works
```

Taking Ownership And Keep

- use `move` keyword

```rust
let list = vec![1, 2, 3];
thread::spawn(move || println!("{:?}", list)); // `move` forces the closure to take ownership of `list`
println!("{:?}", list); // Error: `list` has been moved into the closure
```

## Move Captured Values Out of Closure

3 closure [trait](rust-trait): 

- FnOnce
- FnMut
- Fn

## FnOnce

- **Every** closure implements at least `FnOnce`
- When captured variables are [moved](rust-ownership#when-ownership-moving-happens) out of the closure, the closure consumed
- If no captured variable ownership moving happens, the closure can be called multiple times

Ownership Moved

```rust
let s = String::from("hello");
let t = String::new();
let move_s_to_t = || t = s;
move_s_to_t(); // `s` is moved into the closure and can no longer be used
move_s_to_t(); // Error: closure can only be called once because it moves the captured variable `s`
```

No Ownership Moved

```rust
let s = String::from("hello");
let output_t = || println!("{}", s);
output_t(); // works fine
output_t(); // Ok
```

## FnMut

## Fn



