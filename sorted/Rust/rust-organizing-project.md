# Rust - Organizing Project

## Project with multiple libraries

Example project structure

```
.
├── Cargo.toml
├── hello_macro
│   ├── Cargo.toml
│   └── src
│       └── lib.rs
├── hello_macro_derive
│   ├── Cargo.toml
│   └── src
│       └── lib.rs
├── hello_rust
│   ├── Cargo.toml
│   └── src
│       └── main.rs
└── rustfmt.toml
```

- `Cargo.toml` root directory: specify workspace

```toml
[workspace]
resolver = "3"
members = [
    "hello_macro",  # library crate
    "hello_macro_derive",  # library crate
    "hello_rust",  # binary crate
]
```

- `hello_macro/Cargo.toml`: `package`

```toml
[package]
name = "hello_macro"
version = "0.1.0"
edition = "2024"
```

- `hello_macro_derive/Cargo.toml` 

```toml
[package]
name = "hello_macro_derive"
version = "0.1.0"
edition = "2024"

[lib]
proc-macro = true

[dependencies]
syn = "2.0"
quote = "1.0"
```

- `hello_rust/Cargo.toml`: binary crate:

```toml
[package]
name = "hello_rust"
version = "0.1.0"
edition = "2024"

[dependencies]
hello_macro = { path = "../hello_macro" }
hello_macro_derive = { path = "../hello_macro_derive" }
```
