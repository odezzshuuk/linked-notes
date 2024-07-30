# C++ - Std Function Template

```c++
template<class R, class ... Args>
class function<R(Args...)>
```

- 对于一个`std::function<T>`的实例`f`作为条件时: 含有可调用对象为真，否则为假
- 在头文件`<functional>`中
- 可复制构造
- 模板的类型参数
  - R： 可调用的返回类型
  - Args: 可调用类型的参数类型

## 构造函数

```c++
function() noexcept;
function (nullptr_t fn) noexcept;

function (const function& x);  // 复制构造
function (function&& x);  // 

template <class Fn> function (Fn&& f);

template <class Alloc>
  function (allocator_arg_t aa, const Alloc& alloc) noexcept;
template <class Alloc>
  function (allocator_arg_t aa, const Alloc& alloc, nullptr_t fn) noexcept;
template <class Fn, class Alloc>
  function (allocator_arg_t aa, const Alloc& alloc, Fn fn);
template <class Alloc>
  function (allocator_arg_t aa, const Alloc& alloc, const function& x);
template <class Alloc>
  function (allocator_arg_t aa, const Alloc& alloc, function&& x);
```

- parameter
  - x : 用于初始化`*this`的函数
  - Fn: [[cpp-callable-type]]对象
  - alloc:
- `std::function<T> f;`： 用来存储可调用对象的空function
- `std::function<T> f(nullptr);`: 显式构造一个空function
- `std::function<T> f(obj);` :  f中存储可调用对象obj的副本
- `f(args)`: 调用f中的对象, 参数args
- 不能将重载函数的名字存入function对象，使用[函数指针](c++-function-pointer.md)解决二义性问题 

## Member

- result_type
- argument_type
- first_argument_type
- second_argument_type
