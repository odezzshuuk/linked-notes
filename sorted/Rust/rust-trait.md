# Rust - Trait

## What's Trait

- A trait define shared method signatures that types can implement

## Declaration

```rust
pub trait Summary {
    fn summarize(&self) -> String;
}

// trait provide default implementation 
pub trait Display {
    fn display(&self) -> String {
        String::from("(Read more...)")
    }
}
```

## Implementing A Trait

```rust
impl Summary for NewsArticle {
    fn summarize(&self) -> String {
        format!("{}, by {} ({})", self.headline, self.author, self.location)
    }
}
```

## Trait As Parameter Type Annotation 


```rust
fn notify(item: &impl Summary) {
    println!("Breaking news! {}", item.summarize());
}
```

## Trait As Return Type Annotation

- When Use `impl Trait` as return type
- It is not allow to return different types even they both implement the demanded trait

```rust
pub trait Summary {
  fn summarize(&self) -> String;
}

pub struct GoodNews { }
impl Summary for GoodNews {
  fn summarize(&self) -> String {
    return String::from("This is a good news!");
  }
}

pub struct BadNews { }
impl Summary for BadNews {
  fn summarize(&self) -> String {
    return String::from("This is a bad news!");
  }
}
pub fn returns_summarizable(switch: bool) -> impl Summary {
  if switch {
    GoodNews { }
  } else {
    BadNews { }  // Error: `if` and `else` have incompatible types
  }
}
```

## Trait As Generic type parameter

```rust
fn notify<T: Summary>(item: &T) {
    println!("Breaking news! {}", item.summarize());
}
```

## Trait Bound with Multiple Traits

> like [generic constraint in c#](csharp-generic-constraint.md)

```rust
pub fn notify(item: &(impl Summary + Display)) { }
pub fn notify<T: Summary + Display>(item: &T) { }
```

- item must implement both `Summary` and `Display` traits

Function with multiple generic type parameters write like this

```rust
pub fn notify<T: Summary + Display, U: Clone + Debug>(item: &T, other: &U) -> i32 { }
```

- Or use `where` to for more clearer

```rust
pub fn notify<T, U>(item: &T, other: &U) -> i32
where T: Summary + Display,
      U: Clone + Debug
{ }
```

## Trait Object

