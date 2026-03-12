# Rust - Derive Macro

## What's It

- Automatically generate code for data structure: **struct**, **enum**, **union**
- Mostly used to provide default implementation for traits

## Usage

- used on **structs and enums**

```rust
#[derive(MacroName)]
struct MyStruct {
}
```

## How To Custom Derive Macro

- Custom derive macro must be defined in a separate crate.
- trait and derive in different crate is optional, but it is a common practice to define the trait in a separate crate and re-export the derive macro from that crate.

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

Crates:

- `hello_macro` crate: define the trait and re-export the derive macro
- `hello_macro_derive` crate: define the derive macro
- `hello_rust` crate: use the derive macro

Code manifest:

- `hello_rust/src/main.rs`

```rust
use hello_macro::HelloMacro;
use hello_macro_derive::HelloMacro;

#[derive(HelloMacro)]
struct Pancakes;

fn main() {
  Pancakes::hello_macro();
}
```

- `hello_macro/src/lib.rs`

```rust
pub trait HelloMacro {
    fn hello_macro();
}
```

- `hello_macro_derive/src/lib.rs`

```rust
use proc_macro::TokenStream;
use quote::quote;

fn impl_hello_macro(ast: &syn::DeriveInput) -> TokenStream {
    let name = &ast.ident;

    let generated = quote! {
        impl HelloMacro for #name {
            fn hello_macro() {
                println!("Hello, Macro! My name is {}", stringify!(#name));
            }
        }
    };
    generated.into()
}

#[proc_macro_derive(HelloMacro)]
pub fn hello_macro_derive(input: TokenStream) -> TokenStream {
    let ast = syn::parse(input).unwrap();
    impl_hello_macro(&ast)
}
```

Packages for create derive macro:

- `proc-macro`: compiler api that allow programmer to read and manipulate Rust code from programmer's code
- `syn`: parsing Rust code into a data structure/syntax tree
- `quote`: turns `syn` data back into Rust code

## Built-in

[Built-in Derive Macros](rust-built-in-derives.md)


