# C++ Data Member Pointer

```cpp
struct Base { int m; };
struct Derived : Base {};
 
int main()
{
    int Base::*bp = &Base::m;
    int Derived::*dp = bp;
    Derived d;
    d.m = 1;
    std::cout << d.*dp << ' ' << d.*bp << '\n';
}
```

```cpp
struct Base {};
struct Derived : Base { int m; };
 
int main()
{
    int Derived::* dp = &Derived::m;
    int Base::* bp = static_cast<int Base::*>(dp);
 
    Derived d;
    d.m = 7;
    std::cout << d.*bp << '\n';
 
    Base b;
    std::cout << b.*bp << '\n';
}
```

