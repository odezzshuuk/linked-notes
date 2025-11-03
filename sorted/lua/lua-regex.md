# Lua - Regex

> unlike other script language, lua does not use [posix regex](regex.md)

## Unique Magic Character `%`

- `%` works as an escape `\` for magic characters
- for example `%%` is `%` itself

## Other Magic Characters

- `()`: capture
- `.`: any character
- `[]`: characters set
- `^`: line start, in `[]` represents not
- `$`

Repitition

- `+`
- `-`
- `*`
- `?`

## Character Classes

- `%a`: letters
- `%c`: control characters, e.g. `\n`
- `%d`: digits
- `%l`: lowercase letters
- `%p`: punctuation characters, e.g. `!`
- `$s`: whitespace characters
- `%u`: upper case letters
- `%w`: alphanumeric characters, e.g. `a-z`, `A-Z`, `0-9`
- `%x`: hexadecimal digits, e.g. `0-9`, `a-f`, `A-F`
- `%z`: the character with representation 0, e.g. `\0`

An upper case version of above lable represents reverse class

- for example: `%A` is non-letters

## Repitition

- `*`: 0 or more, e.g. `[0-9]*` matches any number
- `+`: 1 or more
- `?`: 0 or 1
- `-`: same as `*` 

