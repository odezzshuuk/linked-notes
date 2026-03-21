# Rust Smart Pointer - RefCell<T>

* [What It Is](#what-it-is)
* [Key feature](#key-feature)
* [What's It For](#what's-it-for)
* [borrow_mut() and borrow()](#borrow_mut()-and-borrow())
* [Dynamically Enforced Borrow Rules](#dynamically-enforced-borrow-rules)
* [Tips & Tricks](#tips-&-tricks)

## What It Is

- Interior mutability smart pointer

What's It For

- You have a single owner but need mutable access from an immutable reference
- You're implementing patterns like shared state in event handlers or testing
- You need interior mutability without the overhead of [locking](rust-smart-pointer_mutex_t) (like `Mutex<T>`)
- The single-threaded constraint is acceptable for your use case

## Key feature

- Allows you to mutate contents through an immutable reference
- [Enforces **borrow rules at runtime** rather than at compile time](#enforced-borrow-rules-at-runtime)

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

## Enforced Borrow Rules At Runtime

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

## Limitations

- **Not thread-safe** — single-threaded only
- Use [`Mutex<T>`](rust-smart-pointer_mutex_t.md) for multi-threaded scenarios

## Tips & Tricks

- **Error handling**: Use `try_borrow()` and `try_borrow_mut()` for graceful failure handling instead of panicking
- **Reference cycles**: Be careful with `RefCell` inside `Rc<T>` as circular references can cause memory leaks
- **Thread safety**: If needed, use `Arc<Mutex<T>>` instead
- **Borrow scope**: Keep borrows as short as possible by using explicit blocks `{ let borrow = ... }`

