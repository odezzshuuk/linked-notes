# Rust - Fundamental

## Variable Binding

[Variable](rust-variable-binding.md)

## Data Type

[Type](rust-data-type.md)

## Function

Features

- Arguments number must match parameters number
- Use [`Option<T>`](rust-enum#option) to represent optional parameters, must explicitly pass into

> Design choice: Explicit and Predictability

```rust
fn func(a: i32, b: i32, c: i32 = 0) {  // default parameter is not supported in Rust
    // ...
}
```

- No function overloading

return value

```rust
fn add(x: i32, y: i32) -> i32 {
    return x + y;
}
fn only_one_number() -> i32 {
    5
}
fn add(x: i32, y: i32) -> i32 {
    x + y
    // x + y;  // return type is `()`, unit type
}
```

> [unit type definition here](rust-data-type#unit)

## `if let` statement

- A way to handle `match` statement when you only care about one pattern

```rust
let some_value = Some(5);
fn func() -> Option<i32> {
  Some(5)
}

if let Some(x) = some_value { 
  println!("The value is: {}", x);
}

if let Some(x) = func() {
  println!("The value is: {}", x);
}
```

- equivalent to `match` statement:

```rust
let some_value = Some(5);
match some_value {
  Some(x) => println!("The value is: {}", x),
  None => (),
}
```

- Analogous to null check in other languages

```ts
// typescript
let someValue: number | null = 5;
if (someValue !== null) {
  console.log(`The value is: ${someValue}`);
}
```

## Flow Control

```rust
enum Color {
  Red(u8, u8, u8),
  Green(u8, u8, u8),
  Blue(u8, u8, u8),
}


fn get_green_1(color: Color) -> Option<u8> {
  let res_g = if let Color::Green(_, g, _) = color {
    g
  } else {
    return None;
  };

  return Some(res_g);
}

fn get_green_2(color: Color) -> Option<u8> {
  let Color::Green(r, g, b) = color else {
    return None;
  };
  Some(g)
}
// both get_green_1 and get_green_2 are ok
// get_green_2 is more concise and easier to read

let color = Color::Green(45, 218, 45);
let green = get_green_1(color);
let green_2 = get_green_2(color);
println!("Green color: {:?}", green);
```

## Dereference operator `*`

[* Operator](rust-deref-operator.md)

## Deref Trait

[`Deref` trait](rust-deref-trait.md)

## `loop` keyword

- a loop

```rust
fn func() {
  loop {
    println!("loop last forever until ctrl+c");
  }
}
```

- break a loop with `break`

```rust
fn func() {
  let mut count = 0;
  loop {
    count += 1;
    if count == 5 {
      break;
    }
  }
}
```

- break a loop with value

```rust
fn main() {
    let mut counter = 0;
    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2;
        }
    };
    println!("The result is {result}");  // The result is 20
}
```

- break in nest loop, use label to specify which loop to break
  - `break` apply to the current loop
  - `break 'label` apply to the loop with the specified label

```rust
fn func() {
  let mut count = 0;
  'outer: loop {
    let mut remaining = 10;
    loop {
       println!("remaining = {}", remaining);
      if remaining == 9 {
        break; 
      }

      if count == 2 {
        break 'outer; // break outer loop
      } 
      remaining -= 1;
    }
    count += 1;
  }
}
```

