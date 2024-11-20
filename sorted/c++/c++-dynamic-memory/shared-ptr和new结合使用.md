# Cpp - Combine shared_ptr and new

```c++
void process(shared_ptr<int> ptr)
{
    /// function_body
}
int *x(new int(1024));
process(x);  
process(shared_ptr<int>(x));  
int j = *x;
```
