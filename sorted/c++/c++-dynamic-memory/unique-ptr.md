# unique_ptr

```cpp
unique_ptr<int> clone(int p) {
    return unique_ptr<int>(new int(p));
}
unique_ptr<int> clone(int p) {
    unique_ptr<int> ret(new int (p));
    return ret;
}
```

## Member

- `u.release()`
- `u.reset()`
- `u.reset(q)`

```c++
p1.reset(p2.release());
```
