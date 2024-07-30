#  C++ Callbale Type

[function pointer](c++-function-pointer.md)

[data member pointer](cpp-data-member-pointer.md): can be used as a parameter, although it is not called

[lambda expression](c++-lambda.md)

[overload call operator](cpp-overload-call-operator.md)

[std function template](cpp-std-function-template.md)

[std built-in callable object](cpp-std-define-callable-object.md)

- A map of various callable objects

```c++
map<string, function<int(int, int)>>binops = {
  {"+", add},                                  // function pointer
  {"-", std::minus<int>()},                    // std built-in callable object
  {"/", divide()},                             // user-defined callable object
  {"*", [](int i, int j) {return i * j;}},     // unnamed lambda
  {"%", mod}                                   // named lambda
};
```

## Std Library Of Callable Object

[std::result_of](c++-std-result-of.md)

[std::bind](标准库bind函数.md)
