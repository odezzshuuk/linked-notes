# Linux - File Descriptor

## What It Is

- Is a non-negative integer
- Is created with process
- Is created by process
- Different process's file descriptor **may not equal for same file**
- A file descriptor is corresponding to a **opened** file
- [Process](linux-process.md) access file by file descriptor

## 3 Standard File Descriptors

**Every** process create three standard file descriptors

- `STDIN_FILENO`(standard input, like keyboard), `/proc/<pid>/fd/0`
- `STDOUT_FILENO`(standard output, like screen), `/proc/<pid>/fd/1`
- `STDERR_FILENO`(standard error, like screen), `/proc/<pid>/fd/2`

## Take A Look

eg: use vim open a file `vim test`, `ls -l /proc/pid/fd` output as below

> pid in `ls -l /proc/pid/fd` is the process id of `vim test`

```sh
lrwx------ 1 user user 0 Sep  9 10:48 0 -> /dev/tty1
lrwx------ 1 user user 0 Sep  9 10:48 1 -> /dev/tty1
lrwx------ 1 user user 0 Sep  9 10:48 2 -> /dev/tty1
lrwx------ 1 user user 0 Sep  9 10:48 4 -> /home/user/code/.test.swp
```

except system auto create file descriptor, there is a file descriptor 4, vim will write all modify to this file

- `0` is STDIN_FILENO
- `1` is STDOUT_FILENO
- `2` is STDERR_FILENO
- `4` is ...

## Three standard file descriptors

- `STDIN_FILENO` is standard input, like keyboard
-

## Process Table

every process has a process table, which contains a set of file descriptors

- key-value pairs is file descriptor flag and a pointer to a file table item
- default size limit is 1024
- file table item has those members
  - file status flag
  - current file offset
  - pointer to a [i-node] table item

v-node

- file type and pointer to function that operate this file
- most of them also contains a pointer to file's i-node

i-node

- contains file owner, file length, disk location and so on

## Command To Operate File Descriptor


- `exec num<file` create a file descriptor that only can be used for input
- `exec num>file` create a file descriptor that only can be used for output
- `&file_descriptor`
- `exec file_descriptor<&-`
- `exec file_descriptor>&-`
