# Rust - Closure

## What's It

> Similar concept: [Closure](javascript-closure.md) 

```rust
let x = 10;
let f = |y: i32| x + y;  // `f` is a closure that captures `x` from the environment
```

## Captured Variable

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

3 [closure](#whats-it) [trait](rust-trait): 

- [FnOnce](#fnonce)
- [FnMut](#fnmut)
- [Fn](#fn)

**Closures automatically implement one, two, all the 3**

1. **Every** closure implements at least `FnOnce`
2. I can't explicitly specify which closure trait a closure implements

```rust
fn func_1() {
  let mut x = 5;
  let increase_by_one: impl FnMut() = || x += 1;  // Error
  println!("x: {x}");
}
```

## FnOnce

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

- Mutate the captured value
- Can be called more than once

```rust
let mut x = 5;
let mut increase_by_one = || x += 1;  // Auto implement `FnMut`
increase_by_one(); // works fine, x is now 6
// increase_by_one(); // 
```

- A method take `&mut self` as parameter
- **Closure `increase_by_one` can be considered as folowing**

```rust
struct IncreaseByOne<'a> {
  x: &'a mut i32,
}
impl IncreaseByOne<'_> {
  fn execute(&mut self) {
    *self.x += 1;
  }
}
fn main() {
  let mut x = 5;
  let mut increase_by_one = IncreaseByOne { x: &mut x };
  increase_by_one.execute();
  println!("x: {x}");
}
```

- method `execute(&mut self)` is similar to `FnMut` trait's `call_mut(&mut self)` method

## Fn

- Can be called more than once
- Can't move captured value out of the closure
- Can't mutate captured variable


```rust
let mut x = 5;
let read_x = || println!("x: {x}");  // Auto implement `Fn`
read_x(); 
read_x();
```

