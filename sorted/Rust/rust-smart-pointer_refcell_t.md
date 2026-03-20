# Rust Smart Pointer - RefCell<T>

* [What It Is](#what-it-is)
* [Key feature](#key-feature)
* [What's It For](#what's-it-for)
* [borrow_mut() and borrow()](#borrow_mut()-and-borrow())
* [Dynamically Enforced Borrow Rules](#dynamically-enforced-borrow-rules)
* [Tips & Tricks](#tips-&-tricks)

## What It Is

- `RefCell<T>` is a smart pointer that enforces **borrow rules at runtime** rather than at compile time.

## Key feature

- Allows you to mutate contents through an immutable reference
- Uses **interior mutability** pattern for runtime borrow checking
- [Tracks borrows dynamically and panics if rules are violated](#dynamically-enforced-borrow-rules)
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

## borrow_mut() and borrow()

```rust
use std::cell::RefCell;

struct Point {
  x: i32,
  y: i32,
}

impl Point {
  fn new(x: i32, y: i32) -> Self {
    Point { x, y }
  }

  pub fn move_point(&mut self, x: i32, y: i32) {
    self.x += x;
    self.y += y;
  }

  pub fn print(&self) {
    println!("Point({}, {})", self.x, self.y);
  }
}

fn func() {
  let p_cell = RefCell::new(Point::new(0, 0));

  {
    let mut p_m = p_cell.borrow_mut();
    p_m.move_point(3, 4);  // Ok
  }

  {
    let p_r = p_cell.borrow();
    p_r.print();  // Ok
    p_r.move_point(1, 2);  // Error: cannot borrow `*p_r` as mutable, as it is behind a `Ref`
  }
}
```

## Dynamically Enforced Borrow Rules

For code in previous section

```rust
fn func() {
    let p_cell = RefCell::new(Point::new(0, 0));

    let mut p_m = p_cell.borrow_mut();
    p_m.move_point(3, 4);  // Ok

    let p_r = p_cell.borrow();  // Panic will occur here
    p_r.print();
    p_r.move_point(1, 2);  // Error: cannot borrow `*p_r` as mutable, as it is behind a `Ref`
}
```

- At line `let p_r = p_cell.borrow();`, panic will occur, and no compile error raised
- Panic say: RefCell already mutably borrowed
- Which indicates that RefCell check [borrow rules](rust-borrowing#borrow-checker-check-rules) at runtime not compile time

## Tips & Tricks

- **Error handling**: Use `try_borrow()` and `try_borrow_mut()` for graceful failure handling instead of panicking
- **Reference cycles**: Be careful with `RefCell` inside `Rc<T>` as circular references can cause memory leaks
- **Thread safety**: If needed, use `Arc<Mutex<T>>` instead
- **Borrow scope**: Keep borrows as short as possible by using explicit blocks `{ let borrow = ... }`

