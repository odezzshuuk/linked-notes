# Rust - Macro

## What's Macro

- Expanded before the compiler interpret the code
- Metaprogramming

> Metaprogramming: [c++ #define](c++-preprocess.md#`#define`), [decorator](typescript-decorators.md)

## Macros Types

- [Declarative Macros](#declarative-macros)
- [Procedural Macros](#procedural-macros)
  - [Custom `derive` Macros](#custom-`derive`-macros)
  - [Function-like Macros](#function-like-macros)
  - [Attribute-like Macros](#attribute-like-macros)

## Declarative Macros

- `println!` is a declarative macro
- Take a [expression](rust-fundamental#expression) as argument

To define a declarative macro, use `macro_rules!` macro

- e.g. a simple `vec!` macro
- `#[macro_export]` indicates that this macro should be made available whenever the crate in which the macro is defeined is brought into scope.
  - Without `#[macro_export]`, the macro can only be used within the same crate where it is defined

```rust
#[macro_export]
macro_rules! vec {
  ( $($x:expr),* ) => {
    {
      let mut temp_vec = Vec::new();
      $(
        temp_vec.push($x);
      )*
      temp_vec
    }
  };
}
```

- $x

call a declarative macro

- `macro_name!(arguments)`

## Custom `derive` Macros

[Custom `derive` Macros](rust-derive-macro.md)

## Attribute Like Macros

- Similar to `derive` macros, but can be applied to other items: `functions`, `modules`, `fields`, `match` arms.
- [`cfg`](rust-conditional-compilation) is an attribute-like macro

A web application framework code may looks like

```rust
#[route(GET, "/")]
fn index() { }
```

The definition of `route` macro may like

```rust
#[proc_macro_attribute]
pub fn route(attr: TokenStream, item: TokenStream) -> TokenStream { }
```

## Function Like Macros

- unlike declarative macros, function-like take a `TokenStream`

The definition may like: 

```rust
#[proc_macro]
pub fn sql(input: TokenStream) -> TokenStream { }
```

The call may like:

```rust
let sql = sql!(SELECT * FROM users WHERE id = 1);
```
