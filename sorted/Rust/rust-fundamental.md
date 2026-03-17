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


## Statement

Not value

```rust
let x = 5;
```

## Expression

- evaluate to a value
- remove last semicolon `;` to represent a expression with `{}` block, 

```rust
let x = {
    let y = 6;
    y + 1
}
```

`if let` statement

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


