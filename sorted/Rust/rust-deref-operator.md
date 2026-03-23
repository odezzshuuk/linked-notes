# Rust - Deref Operator

```rust
let mut n = 5;
let ptr = &mut n;
*ptr = 10;
```

`*` doesn't recursively dereference `ptr` to get the value of `n`

```rust
use std::rc::Rc;

let x = Rc::new(Box::new(5));
let a = &*x;  // &Box<i32>
let b = **x;  // i32
```

`*` operator apply to the entire method chain

```rust
*p.method_one().method_two()
```

- equivalent to `*(p.method_one().method_two())`

`*` operator implicitly add when method call

- [method call](rust-method#method-auto-deref)

