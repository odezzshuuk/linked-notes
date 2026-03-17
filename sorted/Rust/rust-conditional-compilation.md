# Rust - Conditional Compilation

## What It Is

> c/c++: [`#ifdef`], C#/.NET: [`#if`]

Conditional compilation in Rust allows you to include or exclude code at compile time based on:

- Target operating system or architecture
- Enabled `cargo` features
- Debug vs release builds
- Custom configuration flags

The compiler removes excluded code entirely

- resulting in smaller binaries with no runtime overhead.

## Key Features

- Code is included or removed during compilation, not at runtime
- No performance cost for the conditional checks themselves
- Built-in predicates (`target_os`, `target_arch`, `debug_assertions`, `test`)
- Custom features via `Cargo.toml`
- Boolean combinations with `all()`, `any()`, `not()`

## How to Use

**Built-in predicates and how to trigger them:**

Platform targets (automatically evaluated):

```rust
#[cfg(target_os = "linux")]
fn temp_dir() { "/tmp" }
```

- command

```bash
cargo build --target x86_64-unknown-linux-gnu
```

Architecture (automatically evaluated):

```rust
#[cfg(target_arch = "x86_64")]
fn use_simd() { /* fast path */ }
```

- command

```bash
cargo build --target x86_64-unknown-linux-gnu
```

Debug assertions (set by build profile):

```rust
#[cfg(debug_assertions)]
fn validate() { assert!(self.is_valid()); }
```

- command

```bash
cargo build             # debug_assertions = true
cargo build --release   # debug_assertions = false
```

**Custom features and how to enable them:**

- Define in `Cargo.toml`:

```toml
[features]
serde = []
compression = []
```

```rust
#[cfg(feature = "serde")]
use serde::{Serialize, Deserialize};
```

```bash
cargo build --features "serde"
cargo build --features "serde,compression"
cargo build --all-features
cargo build --no-default-features
```

**Test cfg (automatically set when running tests):**

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn it_works() { assert_eq!(2 + 2, 4); }
}
```

- command

```bash
cargo test
```

**Boolean logic:**

- `all(...)`: All conditions must be true
- `any(...)`: At least one condition must be true

```rust
#[cfg(all(target_os = "linux", target_arch = "x86_64"))]
fn linux_x64() { }

#[cfg(any(target_os = "linux", target_os = "macos"))]
fn unix_like() { }

#[cfg(not(target_os = "windows"))]
fn non_windows() { }
```

**`cfg_attr` for conditional attributes:**

```rust
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub struct Config { value: i32 }
```

- command

```bash
cargo build --features "serde"
```

## Tips & Tricks

**Prefer `#[cfg]` over `cfg!()`:**

`#[cfg]` removes code; `cfg!()` keeps it but returns false. Use `#[cfg]` for actual code removal.

```rust
// ✅ Code not compiled
#[cfg(target_os = "windows")]
fn windows_only() { }

// ❌ Code compiled but condition checked at runtime
if cfg!(target_os = "windows") { }
```

**Avoid duplicating function signatures:**

Use `cfg` on the body, not the whole function:

```rust
// ✅ Good
pub fn home_dir() -> String {
    #[cfg(target_family = "unix")]
    { std::env::var("HOME").unwrap() }
    
    #[cfg(target_family = "windows")]
    { std::env::var("USERPROFILE").unwrap() }
}
```

**Document feature-gated `APIs`:**

```rust
/// Only available with `serde` feature enabled.
#[cfg(feature = "serde")]
pub fn serialize(&self) -> String { /* */ }
```

**Test multiple configurations in CI:**

```bash
cargo check --all-features
cargo check --no-default-features
cargo test --target x86_64-apple-darwin
```
