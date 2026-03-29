# Idioms

## Use Borrow Type For Arguments

## Concatenate Strings With Format!

```rust
fn say_hello(name: &str) -> String {
  format!("Hello {name}!")
}
```

Advantages

- succinct and readable

Disadvantages

- Not most efficient way to combine strings
- A series of `push` on mutable string is usually the most efficient

