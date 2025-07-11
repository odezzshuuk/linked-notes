# Modern CMake

## 1. variable and cache

- Cache: A text file named CMakeCache.txt
- created at build directory when run CMake

### 1.1 normal variable

local

```cmake
set(MY_VARIABLE "value")
```

### 1.2 Cache Variable

```cmake
set(MY_CACHE_VARIABLE "VALUE" CACHE STRING "Description")
```

won't modify already existed variable

- STRING: type of variable

```cmake
set(MY_CACHE_VARIABLE "VALUE" CACHE STRING "" FORCE)
mark_as_advanced(MY_CACHE_VARIABLE)
```

### 1.3 Set Environment Variable


```cmake
set(ENV{variable_name} value)
```

### 1.4 Property

```cmake
set_property(TARGET TargetName PROPERTY CXX_STANDARD 11)
```

###  BOOL

```cmake
option(MY_OPTION "this is settable form the command line" OFF)
```

## How to structure your project

```yml
- project
    - .gitignore
    - README.md
    - LICENCE.md
    - CMakeLists.txt
    - cmake
        - FindSomeLib.cmake
        - something_else.cmake
    - include
        - project
        - lib.hpp
    - src
        - CMakeLists.txt
        - lib.cpp
    - apps
        - CMakeLists.txt
        - app.cpp
    - tests
        - CMakeLists.txt
        - testlib.cpp
    - docs
        - CMakeLists.txt
    - extern
        - googletest
    - scripts
        - helper.py
```

