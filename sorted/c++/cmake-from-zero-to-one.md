# CMake - 0 to 1

`CMakeLists.txt`

```c++
CMAKE_MINIMUM_REQUIRED(VERSION 3.15)

PROJECT(app)

add_executable(app main.cpp) 
```

Generate Build System Directory

```sh
cmake -S . -B build
```

- this command will use `CMakeLists.txt` in current directory to generate build system, and place it in `build` directory

To execute executable file

```sh
cmake --build build
```

- or use [`make`](makefile.md)

```sh
cd build
make
```

