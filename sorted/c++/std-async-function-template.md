# std_async function

```c++
template <class Fn, class... Args>
future<typename result_of<Fn(Args...)>::type> async (Fn&& fn, Args&&... args);
```    


```c++    
template <class Fn, class... Args>
future<typename result_of<Fn(Args...)>::type> async (launch policy, Fn&& fn, Args&&... args);
```    

## Parameters

- `fn` : [callback object](cpp-callable-type.md)
- `Args`: 
- `policy`: 
  - `std::launch::async`:
  - `std::launch::deferred`:
  - `std::launch::async | std::launch::deferred`:
    
## 返回值

- `std::future<fn>`
