# C++ - Preprocess


* [What It Is](#what-it-is)
* [`#include`](#`#include`)
* [`#define`](#`#define`)
* [`#if`](#`#if`)

## What It Is

- Inherited from language C
- Preprocessor directives start with `#.`

For example, `#define macro-name replacement-text`

- when this line of code appears in a file
- all `macros-name` will be replaced with `replacement-text` before the program is compiled.

## `#include`

- Typically used to include header files.
- It can also include source files
  - If a source file is included, you don't need to include it again when using C++ project build tools
  - otherwise, it will result in errors due to duplicate definitions.

`#include <func.h>`

- search for system header files, search directory is determined by compiler and system
- common search directory is `/usr/inlcude`, `usr/local/include`

`#include "func.h"` 

- search same directory as the file containing `#include "func.h"`
- search directory specified by [`-I` option](gcc-options.md#-i-dir)

`#include "directory/func.h"` 

- search `func.h` from the subdirectory `directory`

`#include "../func.h"` 

- includes `func.h` from the parent directory. `..` is used to go up to the parent directory before referencing.

## `#define`

Define a text replacement

- ...

Define a macro

- Syntax:

1. `#define identifier replace_list(optional)`
2. `#define identifier(parameters) replace_list(optional)`
3. `#define identifier(parameters, ...) replace_list(optional)`
  - `...` represents a mutable number of parameters

```c++
#define PI 3.1415926
```

## `#if`

- `#ifdef` 
- `#ifndef` 

```c++
#ifndef SALES_DATA_H
#define SALES_DATA_H
#include <string>

struct Sales_data{
    std::string bookNo;
    unsigned units_sold = 0;
    double revenue = 0.0;
};
#endif
```

[Pramga](c++-preprocessor-pragma.md)
