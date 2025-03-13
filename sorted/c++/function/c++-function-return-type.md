# 返回类型

## 返回数组指针

- 返回的是指向[数组](c++-array.md)的指针
- 因为**数组不能被拷贝**，所以函数不能返回数组, 可以返回数组的指针或引用
- 函数形式: `Type (*function(parameter)) [dimension]`
  - Type:表示**元素**类型
  - dimension: 表示数组维度大小
- 函数声明分解
  - `func (int i)`  &nbsp  函数名，形参类型和名称
  - `(*func (int i))`&nbsp  对调用函数的**返回值**解引用
  - `(*func(int i))[10]`&nbsp 得到一个大小是10的数组
  - `int (*func(int i))[10]` &nbsp 声明元素类型
  
## 尾置返回类型
- `auto func(int i) -> int(*)[10];`返回一个指针指向含有10个元素数组
- 任何函数都可以定义成尾置返回, 但尤其适用于复杂返回类型
