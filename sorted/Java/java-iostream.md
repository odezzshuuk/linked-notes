## Java IOStream

InputStream

- Read data read(): Reads the next byte, **blocks** until input data is available

OutputStream

- public void write(int b): Writes a byte
- public void write(byte[] b): Writes a byte array

```java
byte[] data = new byte[1024];
//...
out.write(data);
out.write(13);  // If an IOException is thrown here
```

> Hypothesis: It is possible that when write(byte[] data) was called, the resource was already in an error state, so data was only written to the buffer and no exception was thrown. However, write(int b) flushes the buffer, so the exception is thrown here.
