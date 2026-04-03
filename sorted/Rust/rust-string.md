# Rust - String

## Declaration

```rust
let s = String::from("hello")
```

## What's `str`

- dynamically sized type
- never use `str` directly

## Relationship between `String` and `str`

- `String` essentially is a wrapper around a vector of bytes (`Vec<u8>`)
- `String` implements the [`Deref` trait](rust-deref-trait.md)

```rust
Dref<Target = str>
```

## When to Use Which?

| Scenario                        | Use      | C# Equivalent                    |
| ------------------------------- | -------- | -------------------------------- |
| String literals                 | `&str`   | `string` literal                 |
| Function parameters (read-only) | `&str`   | `string` or `ReadOnlySpan<char>` |
| Owned, mutable strings          | `String` | `StringBuilder`                  |
| Return owned strings            | `String` | `string`                         |



