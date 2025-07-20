# Rule of Three/Five

- Three basic operations can control the copy operations of a class:
  - [[c++_Copy_Constructor]]
  - [[Copy Assignment Operator]]
  - [[c++_Destructor]]
- A class that needs a destructor also needs copy and assignment operations.
- A class that needs a copy operation also needs an assignment operation, and vice versa.

```c++
class HasPtr { /// A class with a pointer member
public:
    HasPtr(const std::string& s = std::string()) : ps(new std::string(s)), i(0) {}
    /// If no copy constructor is defined, a synthesized copy constructor will be used.
private:
    std::string* ps;
    int i;
};
HasPtr f(HasPtr hp)
{
    HasPtr ret = hp;  /// copy hp
    return ret;  /// ret and hp are destroyed
    /// This will cause the pointer member to be destroyed twice.
}
```
