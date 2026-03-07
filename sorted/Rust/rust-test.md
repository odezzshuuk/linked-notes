# Rust - Test

* [What It Is](#what-it-is)
* [What's It For](#what's-it-for)
* [Introduction to cfg](#introduction-to-cfg)
* [Test Organization](#test-organization)
* [Unit tests live with the code](#unit-tests-live-with-the-code)
* [Integration tests](#integration-tests)
* [Common Assertions](#common-assertions)
* [Running Tests](#running-tests)
* [Attrubutes In Test](#attrubutes-in-test)
* [Testing with `Result<T, E>`:**](#testing-with-`result<t,-e>`:**)
* [Documentation Tests](#documentation-tests)
* [Test Helpers and Setup](#test-helpers-and-setup)
* [Tips & Tricks](#tips-&-tricks)

## What It Is

Rust's built-in testing framework for writing and running unit tests, integration tests, and documentation tests. Key features:

- Built into the Rust toolchain via `cargo test`
- Supports assertions, test organization, and parallel execution
- Includes documentation testing from code examples

## What's It For

Testing ensures code correctness and prevents regressions:

- **Unit tests**: Verify individual functions and modules in isolation
- **Integration tests**: Test public API interactions across modules
- **Documentation tests**: Ensure code examples in docs stay working
- **Benchmarking**: Measure performance (requires nightly Rust)

## Introduction to cfg

[cfg](rust-conditional-compilation.md)

## Test Organization

2 way to organize tests:

- [test live with code](#unit-tests-live-with-the-code)
- [Integration tests](#integration-tests)

## Unit tests live with the code

- Place on `#[cfg(test)]` modules in the same file as the implementation:

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(2, 3), 5);
    }

    #[test]
    fn test_add_negative() {
        assert_eq!(add(-1, 1), 0);
    }
}
```

## Integration tests

- live in `tests/` directory:**

```rust
// tests/integration_test.rs
use my_crate::process_data;

#[test]
fn test_public_api() {
    let result = process_data("world");
    assert_eq!(result, "WORLD");
}
```


## Common Assertions

**Equality and inequality:**

```rust
#[test]
fn test_assertions() {
    assert_eq!(2 + 2, 4);
    assert_ne!(2 + 2, 5);
    
    assert!(true);
    assert!(!false);
}
```

**Custom failure messages:**

```rust
#[test]
fn test_with_message() {
    let result = calculate_something();
    assert_eq!(
        result, 
        42, 
        "Expected 42, got {} instead", 
        result
    );
}
```

**Approximate float comparison:**

```rust
#[test]
fn test_floats() {
    let result = 0.1 + 0.2;
    let expected = 0.3;
    assert!((result - expected).abs() < 1e-10);
}
```

## Running Tests

**Run all tests:**

```bash
cargo test
```

**Run specific test:**

```bash
cargo test test_name
```

**Run tests matching pattern:**

```bash
cargo test add  # Runs all tests with "add" in name
```

**Show output from passing tests:**

```bash
cargo test -- --show-output
```

**Run tests in single thread:**

```bash
cargo test -- --test-threads=1
```

## Attrubutes In Test

Testing with expected panics

- Use `#[should_panic]` to mark tests that must panic to pass:

```rust
#[test]
#[should_panic]
fn test_divide_by_zero() {
    let result = 10 / 0;
}

#[test]
#[should_panic(expected = "index out of bounds")]
fn test_out_of_bounds() {
    let v = vec![1, 2, 3];
    v[99];
}
```

## Testing with `Result<T, E>`:**

```rust
#[test]
fn test_with_result() -> Result<(), String> {
    if 2 + 2 == 4 {
        Ok(())
    } else {
        Err(String::from("Math is broken"))
    }
}
```

ignored expensive tests

- Use `#[ignore]` to skip a test by default (only runs with `cargo test -- --ignored`):

```rust
#[test]
#[ignore]
fn expensive_test() {
    // Only runs with: cargo test -- --ignored
}
```

## Documentation Tests

**Tests in doc comments:**

Rust automatically tests code examples in doc comments (triple backticks in `///` comments). Each example is compiled and run during `cargo test`:

```rust
/// Adds two numbers together.
///
/// # Examples
///
/// ```
/// use my_crate::add;
///
/// let result = add(2, 3);
/// assert_eq!(result, 5);
/// ```
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

**Marking doc tests as non-runnable:**

- Use the `no_run` attribute in doc test code fences to compile but skip executing:

```rust
/// # Examples
///
/// ```no_run
/// // This compiles but doesn't run
/// loop {
///     println!("Forever!");
/// }
/// ```
```

## Test Helpers and Setup

**Shared test helpers:**

```rust
#[cfg(test)]
mod tests {
    use super::*;

    fn setup() -> TestFixture {
        TestFixture::new()
    }

    #[test]
    fn test_with_setup() {
        let fixture = setup();
        assert!(fixture.is_valid());
    }
}
```

**Test modules for organization:**

```rust
#[cfg(test)]
mod tests {
    use super::*;

    mod unit_tests {
        use super::*;

        #[test]
        fn test_internal_logic() {
            // Unit test
        }
    }

    mod integration_tests {
        use super::*;

        #[test]
        fn test_full_flow() {
            // Integration test
        }
    }
}
```

## Tips & Tricks

**Use `cargo test --help` to see all options:**

The `--` separates cargo arguments from test binary arguments:
- Before `--`: cargo test options (e.g., `--release`)
- After `--`: test binary options (e.g., `--nocapture`)

**Test private functions:**

Unit tests in the same file can access private functions:

```rust
fn internal_helper(x: i32) -> i32 {
    x * 2
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_private_function() {
        assert_eq!(internal_helper(5), 10);
    }
}
```

**Use `Result` for cleaner error handling:**

Return `Result` from tests to use `?` operator:

```rust
#[test]
fn test_with_question_mark() -> Result<(), Box<dyn std::error::Error>> {
    let file = std::fs::read_to_string("test.txt")?;
    assert!(file.len() > 0);
    Ok(())
}
```

**Benchmark tests (nightly only):**

Use `#[bench]` (requires nightly Rust and `#![feature(test)]`) to measure code performance. The `b.iter()` method runs the closure repeatedly and measures execution time:

```rust
#![feature(test)]
extern crate test;

#[bench]
fn bench_add(b: &mut test::Bencher) {
    b.iter(|| {
        (0..100).fold(0, |a, b| a + b)
    });
}
```

**Testing compile failures with trybuild:**

For library authors testing that code should NOT compile, use the `trybuild` crate to test compile-time errors.


