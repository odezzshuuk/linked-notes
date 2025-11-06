# Eight Primitive Types Information

## byte

- 8bits, 1 byte
- Value range: -128~127
  - `-1`:   11111111
  - `-128`: 10000000
  - `127`:  01111111

## Integer Types

- Literals
  - Hexadecimal literals prefix 0x
  - Octal literals prefix 0
  - Binary prefix 0b

short

- 16bits, 2 bytes

int: Integer

- 32bits, 4 bytes
- Range: -2^31 ~ 2^31-1
  - `-2^31`:  10000000000000000000000000000000
  - `2^31-1`: 01111111111111111111111111111111
  - `-1`:     11111111111111111111111111111111
- int negative value formula: `-n = ~n + 1`

```java
int a = 5;  // 5 is an integer literal
double b = 5 / 2; // b = 2.0
```

long: Long Integer

- 64bits, 8 bytes
- Numeric suffix L

Mixed integer types, short type converts to long type

```java
long l1 = 1000000000 * 2 * 10L;  // 10000000000 * 2 int to long
long l2 = 1000000000 * 3 * 10L;  // 10000000000 * 3 int overflow
long l3 = 1000000000L * 3 * 10;  // Always long
```

> In C and C++, the size of types like int and long depends on the target platform, such as integer values occupying 2 bytes on 16-bit processors like 8086

## Floating Point Types

float

- 32bits, 4 bytes
- Decimal point plus suffix f, like `float f = 624.424f;`

double

- 64bits, 8 bytes
- `double d = 1.0;`
- Double precision format floating point number
- Has errors

```java
double c = 2.0, d = 1.9
System.out.println(c - d);
// Output 0.1000000000000009
```

## boolean

- Can only be assigned true or false
- Size is not precisely defined

> In C++, numerics and pointers can substitute for boolean, value 0 is equivalent to boolean value

## char : Character

- char in Java, 2 bytes, range 0~65535
- Enclosed in single quotes
- 16-bit [Unicode]() character
- min: \\u0000, max: \\uffff 
- Essentially an int
- ASCII code
  - a: 97
  - A: 65
  - 0: 48

```java
char a1 = 'A';
char a2 = 65;
// a1 equals a2;

// Unicode encoding to characters
int code = 0x41;  // Unicode encoding
char c = (int)code;  // c = 'A'
```

Code points

- 与编码表的某个字符对应的代码值
