# Understanding Standard Library Algorithm Functions

- Understanding standard library algorithm functions lies in knowing whether they **read elements, change elements, or reorder elements**.
- Algorithms do not perform container operations.
  - This means they do not change the size of the container.
  - The only way for algorithms to access data is through [iterators](c++-iterator.md).
- Algorithm functions that read elements from two sequences can have the two sequences be from different containers.
- Two important types of parameters for algorithms are **iterator parameters** and **callable objects as parameters**.
  - Callable object parameters have requirements on the number of predicates[^predicate].

[^predicate]: A callable object that returns a bool type. A unary predicate accepts only one parameter, while a binary predicate accepts two parameters.
