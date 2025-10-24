# std::packaged_task

- Wraps a [[cpp-callable-type]] object, allowing the wrapped object to be called asynchronously, with the return value stored in a [[std_future class template]] object.

```c++
template<class R, class ...Args>
class packaged_task<R(Args...)>
```
- `std::packaged_task<T> task(fn)`: Constructs a `std::packaged_task<T>` object with fn, where T corresponds to the type of fn.
- `T`: Template type parameter, including:
  - R: Return type of the callable type
  - Args: Parameter types of the callable type
  - A callable type that takes *parameter types Args* and returns *type R*

## Constructors

```c++
packaged_task() noexcept;

template <class Fn>
  explicit packaged_task (Fn&& fn);

template <class Fn, class Alloc>
  explicit packaged_task (allocator_arg_t aa, const Alloc& alloc, Fn&& fn);

packaged_task (packaged_task&) = delete;

packaged_task (packaged_task&& rhs) noexcept;
```

-  Function parameters:
   - fn: Callable object
   - a: Allocator
   - rhs: The packaged_task object to move

## Other Members

- `get_future`: Returns the asynchronous result to a [[std_future class template]] object
- `operator()`: Executes the function wrapped by the std::packaged_task object
- `valid`
- `swap`
- `make_ready_at_thread_exit`
