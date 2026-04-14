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
- Use it when we only need to **read** data from the parameter

## As trait bound or parameter

When using `AsRef<T>` as trait bound or [parameter](rust-trait#trait-as-parameter-type-annotation)

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

## VS Deref

For `*` operator

- If a type implements `AsRef<T>` but not `Deref<Target=T>`, `*` operator cannot be used to dereference it to `T`

State

- `AsRef<T>` is used **explicitly** by calling `as_ref()` method.
- `Deref` is used **implicitly**.

Number Of Convert Target

- `AsRef<T>` can be implemented for any type to convert it to a reference of type `&T`
- `Deref`: there is always one unambiguous type to convert
 
Where they are used

- `AsRef` mainly for API design
- `Deref` mainly for smart pointer types 

