# ByteArrayInputStream/ByteArrayOutputStream

## ByteArrayOutputStream

- Data is written to an **auto-growing** buffer array.

Creating an object:

- `ByteArrayOutputStream()`
- `ByteArrayOutputStream(int size)`

Extracting data from the buffer:

- `byte[] toByteArray()`: Copies the data from the stream's buffer to a byte array.
- `String toString()`: Converts the contents of the buffer into a string by decoding the bytes using the default character set.

## ByteArrayInputStream

