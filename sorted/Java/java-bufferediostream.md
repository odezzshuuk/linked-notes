# Buffered Stream: BufferInputStream/BufferOutputStream

- Extends from `FilterInputStream`/`FilterOutputStream`.
- Creates an internal buffer array (`byte[] buf`) upon creation.
- Improves efficiency by reducing the number of I/O operations.

***

- Creating `BufferInputStream`/`BufferOutputStream` objects:
  - `BufferedInputStream(InputStream in)`: Converts the `in` stream to a buffered stream.
  - `BufferedInputStream(InputStream in, int size)`: Converts the `in` stream to a buffered stream with a buffer size of `size`.

## Fields

### Input

- `buf`: Internal buffer array for storing data.
- `count`: Index of the last valid byte in the buffer + 1.
  - Range: `[0, buf.length]`.
- `pos`: Current position in the buffer, index of the next character to be read from the `buf` array.
  - Range: `[0, count]`.
- `markpos`: Value of the `pos` field when the last `mark()` method was called.
  - Range: `[-1, pos]`.
- `marklimit`:

### Output

- `buf`: Internal buffer array for storing data.
- `count`: Index of the last valid byte in the buffer + 1.
  - Range: `[0, buf.length]`.

## Methods

### Output

- `flush()`: Flushes the contents of the buffer.

### Input

- `read()`: Reads one byte.
  - Returns the byte read, or -1 if the end of the file is reached.
  - When `read()` is called, data is obtained from the buffer (`byte[] buf`).
