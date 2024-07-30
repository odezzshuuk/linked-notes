# std::result_of

- `std::result_of<T>::type`获得[[cpp-callable-type]]的返回类型, 用于声明变量类型
- `T`模板的类型参数, 包括:
  - R: 可调用类型的返回类型
  - Args: 可调用类型的参数类型
  
## 构造函数

```c++
template< class >  
class result_of;
  
template<class F, class... ArgTypes>  
class result_of<F(ArgTypes...)>;

template<class F, class... ArgTypes>  
class invoke_result;
```

- `F`必须是[[cpp-callable-type]], 函数的引用，或可调用表达式的引用

## 嵌套类型(辅助类型) 

- `std::result_of<F(ArgTypes)>::type`:  表示以 *参数类型ArgTypes* 调用 *可调用类型F* 的*返回类型*
  > F是可调用类型，不是函数名
