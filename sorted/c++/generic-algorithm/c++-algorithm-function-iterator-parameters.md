# C++ - Algorithm Function Iterator Parameters

- Member functions in container types that return iterators.
- Insert iterators
  - You can add elements to a container through an insert iterator.
  - Accepts a container or a reference to a container as a parameter.
  - Often used as parameters for standard library algorithm functions.
  - There are three types: `back_inserter`, `front_inserter`, and `inserter`.
    - `back_inserter` creates a `push_back` iterator.
    - `front_inserter` creates a `push_front` iterator.
    - `inserter` accepts an iterator parameter for positioning and a value parameter as the element to insert, inserting the element **before the element pointed to by the iterator**.

  ```cpp
  vector<int> vec;
  auto it = back_inserter(vec);  // it is created as a push_back iterator
  *it = 42;  // Add an element to the container by dereferencing it in a push_back manner
  ```

  ```cpp
  list<int> lst = {1, 2, 3, 4};
  list<int> lst2, lst3;
  copy(lst.cbegin(), lst.cend(), front_inserter(lst2));
  // front_inserter inserts before the first element in each iteration
  copy(lst.cbegin(), lst.cend(), inserter(lst3, lst3.begin()));
  // Using inserter inserts before the first inserted element in each iteration
  ```

- iostream iterators
  - Use generic algorithms to write data through stream iterators.
  - When creating a stream iterator, you must specify the type of object the iterator will read from or write to.
  - A default-initialized iterator is an empty iterator and can be used as an end-of-stream iterator.
  - At the end of a file or in case of an I/O error, the value of the iterator becomes equal to the end-of-stream iterator.
