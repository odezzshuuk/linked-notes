# Template std::future

- Provides a std::future object to the creator of an asynchronous operation via [[std_async function template]], [[std_promise class template]], or [[std_packaged_task class template]].
- The template type parameter `T` represents the type of the return value of the asynchronous operation.
- Template declaration:
```c++
template<class T> class future;
template<class T> class future<T&>;
template<> class future<void>;
```

## Constructors

- Default constructor: `future() noexcept;`
- Move constructor: `future(future && x) noexcept;`
- Copy constructor: `future (const future&) = delete;` (not available)

## Member Functions

- `get`: Retrieve the result
  - Blocks until a result is available
  - Returns the value stored in the shared state, equivalent to std::move(val)
  - Returns a reference to the value stored in the shared state, equivalent to std::move(val)
- `wait`: Wait for the result to become available
  - Blocks until a result is available
  - No return value
- `wait_for`: Wait for the result, returns after a specified time interval
- `wait_until`: Wait for the result, returns if the result is not available by a specified time point
- `valid`: Checks whether the future has a shared state
