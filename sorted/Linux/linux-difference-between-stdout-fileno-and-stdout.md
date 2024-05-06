# Linux - Difference between stdout and STDOUT_FILENO

- `stdout` is `FILE*`, called file pointer, refer to [IO Stream](linux-io-stream.md)
- `STDOUT_FILENO` is [file descriptor](linux-file-descriptor.md)
- `fprintf(stdout, "x=%d\n", x)`  corresponding to `printf("x=%d\n", x)
- `STDOUT_FILENO == fileno(stdout)`

