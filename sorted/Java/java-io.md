# IO

- [feature](#feature)
- [Practical Use](#practical-use)
- [File IO](#file-io)
- [Byte Stream](#byte-stream)
- [Reader/Writer](#readerwriter)
- [Why Buffer IO faster than unbuffered IO](#why-buffer-io-faster-than-unbuffered-io)
- [IO Class Hierarchy](#io-class-hierarchy)

## feature

- **Streams must be closed**
- Low-level stream (node stream): Actually connects the program to the other end, responsible for reading and writing byte data
- High-level stream (processing stream): Used to simplify read/write operations, cannot exist independently, must be built on other streams

[流的抽象理解](java-stream.md)

## Practical Use

## File IO

interact with file in java

[File Class](java-file-class.md)

File Byte IO Stream

[FileInputStream/FileOutputStream](java-fileiostream.md)

## Byte Stream

Base Class

- [InputStream/OutPutStream](java-iostream.md)

Low Level Stream

- [FileInputStream/FileOutputStream](java-fileiostream.md)
- [ByteArrayInputStream/ByteArrayOutputStream](java-bytearrayiostream.md)

High Level Stream

- [Buffer Stream](java-bufferediostream.md): Stream that reduces the number of IO operations through buffering
- [Object Stream](java-objectiostream.md): Stream for serializing and deserializing objects
- [Data Stream](java-dataiostream.md): Stream for reading and writing [primitive data types](java-primitives-type.md)

## Reader/Writer

Abstract base class

[Reader/Writer](java-io-character-stream.md)

> write to a stream need close() flush the buffer

**Convert** byte stream to character stream

[InputStreamReader/OutputStreamWriter](java-io-byte-to-charcter.md)

**Buffered** character stream

[BufferedReader/BufferedWriter](java-io-buffer-character.md)

Character output stream that supports **line operations**

[PrintWriter](java-printwriter.md)

## Why Buffer IO faster than unbuffered IO

- Hard disk access is not by byte, but by block
- Therefore, if writing 1 byte takes time t, it does not mean writing x bytes takes x*t

## IO Class Hierarchy

- `java.io.Console (implements java.io.Flushable)`
- `java.io.File (implements java.lang.Comparable<T>, java.io.Serializable)`
- java.io.FileDescriptor
- java.io.InputStream (implements java.io.Closeable)
  - java.io.ByteArrayInputStream
  - java.io.FileInputStream
  - java.io.FilterInputStream
    - java.io.BufferedInputStream
    - java.io.DataInputStream (implements java.io.DataInput)
    - java.io.LineNumberInputStream
    - java.io.PushbackInputStream
  - java.io.ObjectInputStream (implements java.io.ObjectInput, java.io.ObjectStreamConstants)
  - java.io.PipedInputStream
  - java.io.SequenceInputStream
  - java.io.StringBufferInputStream
- java.io.ObjectInputStream.GetField
- java.io.ObjectOutputStream.PutField
- java.io.ObjectStreamClass (implements java.io.Serializable)
- java.io.ObjectStreamField (implements java.lang.Comparable<T>)
- java.io.OutputStream (implements java.io.Closeable, java.io.Flushable)
  - java.io.ByteArrayOutputStream
  - java.io.FileOutputStream
  - java.io.FilterOutputStream
    - java.io.BufferedOutputStream
    - java.io.DataOutputStream (implements java.io.DataOutput)
    - java.io.PrintStream (implements java.lang.Appendable, java.io.Closeable)
  - java.io.ObjectOutputStream (implements java.io.ObjectOutput, java.io.ObjectStreamConstants)
  - java.io.PipedOutputStream
- java.security.Permission (implements java.security.Guard, java.io.Serializable)
  - java.security.BasicPermission (implements java.io.Serializable)
    - java.io.SerializablePermission
  - java.io.FilePermission (implements java.io.Serializable)
- java.io.RandomAccessFile (implements java.io.Closeable, java.io.DataInput, java.io.DataOutput)
- java.io.Reader (implements java.io.Closeable, java.lang.Readable)
  - java.io.BufferedReader
    - java.io.LineNumberReader
  - java.io.CharArrayReader
  - java.io.FilterReader
    - java.io.PushbackReader
  - java.io.InputStreamReader
    - java.io.FileReader
  - java.io.PipedReader
  - java.io.StringReader
- java.io.Writer (implements java.lang.Appendable, java.io.Closeable, java.io.Flushable)
  - java.io.BufferedWriter
  - java.io.CharArrayWriter
  - java.io.FilterWriter
  - java.io.OutputStreamWriter
    - java.io.FileWriter
  - java.io.PipedWriter
  - java.io.PrintWriter
  - java.io.StringWriter
