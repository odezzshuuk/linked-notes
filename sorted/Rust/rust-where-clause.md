# Rust - Where Clause

## What Is It 

Using where clause, Rust can implement more expressive generic constraints

```rust
use std::fmt::Debug;

trait PrintInOption {
    fn print_in_option(self);
}

// Because we would otherwise have to express this as `T: Debug` or
// use another method of indirect approach, this requires a `where` clause:
impl<T> PrintInOption for T where
    Option<T>: Debug {
    // We want `Option<T>: Debug` as our bound because that is what's
    // being printed. Doing otherwise would be using the wrong bound.
    fn print_in_option(self) {
        println!("{:?}", Some(self));
    }
}

fn main() {
    let vec = vec![1, 2, 3];

    vec.print_in_option();
}
```

Trait bound equally where clause, just for readability

```rust
pub fn notify<T, U>(item: &T, other: &U) -> i32
where T: Summary + Display,
      U: Clone + Debug
```

- which is equivalent to:

```rust
pub fn notify<T: Summary + Display, U: Clone + Debug>(item: &T, other: &U) -> i32
```

## Power Of Where Clause

> Some of those are impossible for most other languages

1. [Blanket impls](#blanket-impls)
2. [Associated types](#associated-types)
3. [Higher-ranked trait bounds](#higher-ranked-trait-bounds)

## Blanket impls

For example

- Add method to every type that satisfies constraints defined by where clause

```rust
use std::fmt::Debug;

trait PrintInOption {
    fn print_in_option(self);
}

impl<T> PrintInOption for T where
    Option<T>: Debug {
    fn print_in_option(self) {
        println!("{:?}", Some(self));
    }
}

fn main() {
    let vec = vec![1, 2, 3];
    vec.print_in_option();
}
```

- Add method to every type that satisfies the condition [`Option<T>: Debug`](rust-built-in-derives.md#debug)

Even more expressive way

```rust
fn build_stream<T>(
    device: &cpal::Device,
    config: &cpal::SupportedStreamConfig,
    sample_tx: mpsc::Sender<Vec<f32>>,
    channels: usize,
) -> Result<cpal::Stream, cpal::BuildStreamError>
where
    T: Sample + SizedSample + Send + 'static,
    f32: cpal::FromSample<T>,
{
    // ...
}
```

- The trait bound defined in function signature where clause `f32: cpal::FromSample<T>` means:
  - For sample type `T`, `f32` must implement the trait `cpal::FromSample<T>`
  - Which means there must a valid conversion existing from `cpal::FromSample<T>` to `f32`

> About [conversion](rust-conversion.md) 
> About crate [cpal](rust-cpal.md)

## Higher Ranked Trait Bounds(HRTBs)

[HRTBs](rust-higher-ranked-trait-bounds.md)

