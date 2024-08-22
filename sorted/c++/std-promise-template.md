# C++ - std::promise

- Template Declaration

```c++
template< class R > class promise;
template< class R > class promise<R&>;
template<>          class promise<void>;
```
  
## Constructor

```c++
promise();

template< class Alloc >  
promise(std::allocator_arg_t, const Alloc& alloc);

promise( promise&& other ) noexcept;  // move constructor

promise( const promise& other ) = delete;  // copy constructor unavailable
```

- parameters
  - alloc: allocator
  - other: other std::promise object

## get_value()   

```c++
std::future<T> get_future()
```
- no parameter， 返回与`*this`共享状态的[future](std-future-template.md)  

## set_value()

```c++
void set_value( const R& value );
void set_value( R&& value );
void set_value( R& value );
void set_value();
```
   
- value: 要存储与共享状态的值
   
## set_value_at_thread_exit

- 线程结束后，共享的value处于可用状态
- value: 要存储与共享状态的值

   
