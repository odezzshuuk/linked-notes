# Linux - File Permission

* [File ID](#file-id)
* [File Permission Properties](#file-permission-properties)
* [File Permission related File](#file-permission-related-file)
* [File Permission Mask](#file-permission-mask)

## File ID

[File ID](linux-file-id.md)

## File Permission Properties

- `ls -al`

> `-al` option: list all files add details

| drwxrwxrwx      | 9    | root       | root       | 4096      | Jul 11 14:24       | .         |
| --------------- | ---- | ---------- | ---------- | --------- | ------------------ | --------- |
| file properties | link | file owner | file group | file size | last modified time | file name |

File Permission Properties

| d         | rwx                   | rwx              | rwx                   |
| --------- | --------------------- | ---------------- | --------------------- |
| file type | file owner permission | group permission | other user permission |

- File Type
  - `d`: directory
  - `-`: File
  - `l`: link file
  - `b`:
  - `c`:
- permission properties
  - `r`: readable
  - `w`: writable
    - but you can delete the file even if you don't have write permission on the file, but have write permission on the parent directory
  - `x`: executable
  - `s`: when executable ????, only can be [executable file](executable-file.md)， /usr/bin/passwd
  - `t`: use on directory, make a directory can be written file, and the file can only be deleted by the writer
-  File name

## File Permission related File

[File Permission Related File](linux-account-manage-related-file.md)

## File Permission Mask

- [linux-system-function-umask](linux-system-function-umask.md)



