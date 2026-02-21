# Rust - Modules

> similar concepts: [namespace](csharp-namespace)

## Take A Look

declare and import modules both use keyword `mod`

- declare mod
- `pub` for control visibility

```rust
mod mod_a {
  fn private_function() {
    println!("This is a private function in mod_a");
  }

  pub fn public_function() {
    println!("This is a public function in mod_a");
  }

  pub mod nested_mod {

  }

  mod private_nest_mod {

  }
}
```

- import mod

```rust
mod mod_a;
```

## File hierarchy

main.rs

```rust
mod modules_10;
fn main() {
}
```

Directory structure that support import mod `modules_10` with `mod modules_10;`

- Use `mod.rs` as mod entry point

```
.
├── Cargo.toml
├── main.rs
├── modules_10
│   ├── a.rs
│   ├── b.rs
│   └── mod.rs
└── rustfmt.toml
```

- Or rust file name same as directory name

```
.
├── Cargo.toml
├── main.rs
├── modules_10.rs
├── modules_10
│   ├── a.rs
│   └── b.rs
└── rustfmt.toml
```


