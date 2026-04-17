# Rust - AsRef<T>

## Declaration in std

```rust
pub trait AsRef<T> where
    T: ?Sized,{
    // Required method
    fn as_ref(&self) -> &T;
}
```

## Features

- Used for [cheap] **reference-to-reference** conversions
- As counterpart to [`Into<T>`](rust-from-and-into)

## Implementing AsRef<T> Correctly

A minimal implementation

```rust
struct Email(String);
impl AsRef<str> for Email {
    fn as_ref(&self) -> &str {
        &self.0
    }
}
```

Generic forwarding pattern

- Convert `&T` to `&U`

```rust
struct Wrapper<T>(T);
impl<T, U> AsRef<U> for Wrapper<T> where T: AsRef<U> {
    fn as_ref(&self) -> &U {
        self.0.as_ref()
    }
}
```

Type implement `Deref` Should Consider Implementing `AsRef` like that

```rust
impl<T> AsRef<T> for SomeType
where
    T: ?Sized,
    <SomeType as Deref>::Target: AsRef<T>,
{
    fn as_ref(&self) -> &T {
        self.deref().as_ref()
    }
}
```

## As trait bound or parameter

- when we only need to **read** data from the parameter

> It indicate that type can be converted to a reference of type `&T` by calling `as_ref()` method

```rust
fn file_exists(path: &Path) -> bool {
    path.exists()
}
file_exists(Path::new("/tmp/test.txt"));  // Awkward

// ✅ Accept anything that can behave as a &Path
fn file_exists(path: impl AsRef<Path>) -> bool {
    path.as_ref().exists()
}

// or
fn file_exist<T>(path: T) -> bool where T: AsRef<Path> {
    path.as_ref().exists()
}

file_exists("/tmp/test.txt");                    // &str ✅
file_exists(String::from("/tmp/test.txt"));      // String ✅
file_exists(Path::new("/tmp/test.txt"));         // &Path ✅
file_exists(PathBuf::from("/tmp/test.txt"));     // PathBuf ✅
```

## What AsRef Should Not Used To

```rust
let x = Box::new(5);
let y = y.as_ref(); // Avoid this, but allowed by compiler
let y = &x;  // Better this
```

