# GCC

* [What It Is](#what-it-is)
* [Feature](#feature)
* [Compilation process of gcc/g++](#compilation-process-of-gcc/g++)
* [What Is Link](#what-is-link)
* [How To Link](#how-to-link)
* [Practical Use](#practical-use)
* [Options](#options)

## What It Is

- gcc mean GNU Compiler Collection
- gcc/g++ respectly is GNU C/C++ Compiler

> mingw: Minimalist GNU for **Windows**

## Feature

- multi-language support
- multi-platform support

## Compilation process of gcc/g++

compile process

- source file ⮕  preprocess ⮕  compile ⮕  [link](#what-is-link) ⮕  executable file

corresponding file suffix

- .cpp ⮕ .i ⮕ .s(assemble) ⮕ .o([object file](c-object-file.md)) ⮕  binary file

## What Is Link

- link [static and dynamic libraries](c-library-file.md) to create an executable program.
- In the GNU environment, the [ld command](gnu-linker.md) is used to set linking options.
- The formats for linking library files are as follows:
  - Static Linking Library: `.a` (UNIX) / `.lib` (Windows)
  - Dynamic Linking Library: `.so` (UNIX) / `.dll` (Windows)

## How To Link

```sh
gcc -L/usr/local/lib -lmylib main.cpp
```

- `-L`: add library search path
- `-l`: link library

## Practical Use

## Options

[GCC Options](gcc-options.md)

