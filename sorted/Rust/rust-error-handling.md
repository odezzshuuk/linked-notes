# Rust - Error Handling

* [Best Practice](#best-practice)
* [Error Handling](#error-handling)
* [Panic](#panic)
* [Unrecoverable Error ](#unrecoverable-error-)
* [Behavior On Panic](#behavior-on-panic)
* [Debug Panic](#debug-panic)
* [Recoverable Error](#recoverable-error)
* [Result](#result)
* [Handle `Result`](#handle-`result`)
* [match](#match)
* [? Operator](#?-operator)
* [unwrap and expect](#unwrap-and-expect)
* [unwrap_or_else](#unwrap_or_else)

## Best Practice

- Use `panic!` in library when you want to force caller to fix their mistake
- Use `Result<T, E>` for expected failures

## Error Handling

- Rust use the [`panic!`](#panic) [macro](rust-macro.md) to handle [unrecoverable errors](#unrecoverable-error)
- Use `Result<T, E>` for [recoverable errors](#recoverable-error), allowing the caller to decide how to handle the error

## Panic

Call `panic!` manually to trigger a panic:

```rust
fn main() {
    panic!("This is a panic!");
}
```

## Unrecoverable Error 

- Caused by unrecoverable errors, such as out-of-bounds array access or division by zero:

```rust
fn main() {
    let arr = [1, 2, 3];
    println!("{}", arr[10]); // This will cause a panic due to out-of-bounds access
}
```

## Behavior On Panic

- unwinding: unwind the stack, cleaning up resources(default behavior)
- aborting: immediately abort the program without unwinding

```rust
struct Resource {
    name: String,
}

impl Drop for Resource {
    fn drop(&mut self) {
        println!("Cleaning up resource: {}", self.name); // runs on unwind
    }
}

fn main() {
    let _r1 = Resource { name: String::from("DB connection") };
    let _r2 = Resource { name: String::from("File handle") };

    panic!("Something went horribly wrong");
}
```

- unwind -> [`drop()`](rust-drop) is called
- abort -> process exits immediately, no cleanup

Configurable via `Cargo.toml:`

```toml
[profile.release]
panic = 'abort' # or 'unwind'
```

## Debug Panic

```sh
RUST_BACKTRACE=1 cargo run
```

## Recoverable Error

- Errors are handled by [enum `Result<T>`](#Result)

```rust
use std::fs::File;

fn main() {
    let f = File::open("nonexistent.txt");
    match f {
        Ok(file) => println!("File opened: {:?}", file),
        Err(e) => println!("Could not open file: {}", e), // caller can decide what to do
    }
}
```

## Result

> Many std library functions return `Result`

Definition

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

- `T`: the type of the value returned on success
- `E`: the type of the error returned on failure

Example

```rust
fn main() {
    let f = File::open("nonexistent.txt");
    match f {
        Ok(file) => println!("File opened: {:?}", file),
        Err(e) => println!("Could not open file: {}", e),
    }
}
```

## Handle `Result`

1. [match `Result`](#match)
2. [unwrap and expect]()
3. `?` operator
4. unwrap_or_else()

Which To Use:

- `unwrap`/`expect`: prototypes/examples/tests
- `? operator`: propagate error to caller

## match

```rust
use std::fs::File;
use std::io::ErrorKind;

fn main() {
    let greeting_file_result = File::open("hello.txt");

    let greeting_file = match greeting_file_result {
        Ok(file) => file,
        Err(error) => match error.kind() {
            ErrorKind::NotFound => match File::create("hello.txt") {
                Ok(fc) => fc,
                Err(e) => panic!("Problem creating the file: {e:?}"),
            },
            _ => {
                panic!("Problem opening the file: {error:?}");
            }
        },
    };
}
```

## ? Operator

- If Err, immediately return [`Result`](#result)
- function containing `?` must return `Result` or `Option`

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file(path: &str) -> Result<String, io::Error> {
    let mut file = File::open(path)?;           // ? propagates open error
    let mut username = String::new();
    file.read_to_string(&mut username)?;        // ? propagates read error
    Ok(username.trim().to_string())
}
```

## unwrap and expect

- `unwrap()` will convert [recoverable error](#recoverable-error) into [`panic`](#panic) 
- `expect("msg")` is similar to `unwrap()`, but with custom panic message

```rust
use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt").unwrap();  // if error, panic with default message raised and program will exit

    println!("File opened successfully!");
    // ... you can now use greeting_file ...
}
```

## unwrap_or_else

- just do the same thing as [`match`](#match)

```rust
use std::fs::File;
use std::io::ErrorKind;

fn main() {
    let greeting_file = File::open("hello.txt").unwrap_or_else(|error| {
        if error.kind() == ErrorKind::NotFound {
            // Try to create the file when it doesn't exist
            File::create("hello.txt").unwrap_or_else(|create_err| {
                // If creation also fails → panic (or handle differently)
                panic!("Problem creating the file: {create_err:?}");
            })
        } else {
            // Some other error (permission denied, etc.) → panic
            panic!("Problem opening the file: {error:?}");
        }
    });
}
```

