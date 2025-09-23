# Java Command Line Tools - Argument File Of Command Java

## What It Is

- Simplify the java command by specifying an argument file,
- Use the @ symbol prefix to indicate an argument file containing java options and class names
- When the --disable-@files option is encountered, stop expanding argument files
  - 可以在命令行的任何地方使用--disable-@files选项
  - Including in the argument file itself, to stop @file expansion.

## Argument File Syntax

- Argument files must contain only ASCII characters or ASCII-friendly characters in the system's default encoding, such as UTF-8.
- The size must not exceed 2,147,483,647 bytes
- Whitespace characters include a null character `\t, \n, \r, and \f`

> For example, `c:\Program Files` can be specified as `"c:\\Program Files"` or `c:\Program" "Files`

- Filenames containing spaces should be enclosed in double quotes
- Filenames in the argument file are relative to the current directory, not the location of the argument file
- Use `#` for comments
- Use a trailing `\` to join two lines; spaces before `\` are trimmed
- Place a `\` in the first column to prevent spaces before `\` from being trimmed
- Wildcards `*` are not allowed

## Example

参数文件

```
-cp "lib/
cool/
app/
jars
```

Interpreted as:

```
-cp lib/cool/app/jars
```

To output:

```shell
-cp c:\Program Files(x86)\Java\jre\lib\ext;c:\Program Files\Java\jre9\lib\ext
```

Argument file written as: 

```
-cp "c:\\Program Files (x86)\\Java\\jre\\lib\\ext;c:\\Program Files\\Java\\jre9\\lib\\ext"
```



