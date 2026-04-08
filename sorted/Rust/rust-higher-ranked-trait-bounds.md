# Rustonomicon - Higher Ranked Trait Bounds(HRTBs)

## What Is That

## What's Problem It Solves

- How to express that a type must work for any possible borrow, not just one specific lifetime

```rust
fn run_command<F>(f: F, a: &u8, b: &u8) -> u8
where
    for<'a> F: Fn(&'a u8, &u8) -> &'a u8,
{
    let c = f(&a, &b);
    return *c;
}

fn command<'b>(p1: &'b u8, p2: &u8) -> &'b u8 {
    p1
}


// Add lifetime 'b to p2, it became unsuitable for run_command
fn unsuitable_command<'b>(p1: &'b u8, p2: &'b u8) -> &'b u8 {
    p1
}

pub fn func_entry_point() {
    let res_1 = run_command(command, &5, &10);
    let res_2 = run_command(unsuitable_command, &5, &10);  // error: implementation of `Fn` is not general enough
}
```

