# Linux Programming - Buffer

## Buffer Type

[A Simple Demonstrate](output-order-of-function-write()-and-printf().md)

- full buffer : buffer is full, then send content and flush buffer, usually in file input
- line buffer : flush buffer when newline appears, like keyboard input, printf function
- no buffer : output directly after input, like `write()` function

Some Buffer Type Of Common Stream

- printf() is line buffer
- write() is no buffer
- std error is no buffer

## Set Buffer

```c
#include <stdio.h>
void setbuf(FILE *stream, char *buf);
void setbuffer(FILE *stream, char *buf, size_t size);
void setlinebuf(FILE *stream);
int setvbuf(FILE *stream, char *buf, int mode, size_t size);
```

