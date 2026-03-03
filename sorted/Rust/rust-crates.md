# Rust - Crates

- Smallest amount of code that the Rust compilter considers at a time
- Crate can come in one of two forms:
  - Binary crate: produces an executable program
  - Library crate: produces a library that can be used by other crates
    - Library Crate doesn't have a `main()` function

## `use` keyword

> [import statement](javascript-ecma-import#syntax) in javascript 
> [using static](csharp-namespace) in c#

What's For

- For short path to call functions, structs, enums, etc. from other modules or crates

Caveats

- `use` default search path is from the current crate root, normally the `Cargo.toml` file directory
- to use a item whose located in `./path/to/item.rs`, `use path::to::item;` or `use crate::path::to::item;`

For example

- For Mod file: `lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}
```

Entry file: `main.rs`

- with `use` keyword

```rust
mod lib;
use lib::front_of_house::hosting::add_to_waitlist;
fn main() {
  add_to_waitlist();
}
```

- Without `use` keyword
- You must specify the full path to the function to call

```rust
mod lib;
fn main() {
  lib::front_of_house::hosting::add_to_waitlist();
}
```
