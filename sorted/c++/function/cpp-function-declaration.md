# Cpp - Function Declaration

- The **return type, function name, and parameter types** describe the function interface
- During preprocessing, function declarations are processed; do function declarations occur before linking?
- In a function declaration, parameter names are not required
- It is recommended to declare in the **header file** and define in the **source file**
- Declaration without definition is called **forward declaration**, and it is allowed
- Declaration can be simplified by [typedef](c++-handle-type.md#typedef) and [decltype](c++-handle-type.md#decltype)

```c++
// func0, func1, func2 are the same function type
bool func0(const string&, const string&);
typedef bool func1(const string&, const string&);
typedef decltype(func1) func2;
```
