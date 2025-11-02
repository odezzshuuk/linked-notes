# Java - PrintWriter

Automatic line **flush buffer** **character** output stream

- If autoFlush is enabled:
  - Flushing only occurs when calling println(), printf(), or format() methods
  - It does not flush when outputting a newline character
- Does not have its own buffer array
- Does not provide append mode

## Creating a PrintWriter Object

Constructed via the [File](java-file-class.md) class

- Character set can be specified

Constructed via **OutputStream**: PrintWriter(OutputStream out, boolean autoFlush, Charset charset)

- Allows specifying character set
- Allows specifying auto flush

Constructed via Writer

- Can specify auto flush parameter

Constructed via file path

- Character set can be specified

## Methods for Writing Characters to a File

- println()
- print()

## Scanner

- Scanner class
- File class or file name string can be used as constructor parameter
- Includes various next methods
  - next() reads a string ending with whitespace characters, including `' ', '\t', '\f', '\r', '\n'`
  - nextLine() reads an entire line
