# code

## Method 1

```c++
void BR(size_t n) {  
  int a = n % 2;  
  n = n >> 1;  
  if (n != 0) {  
    BR(n);  
  }  
  std::cout << a;  
}
```
