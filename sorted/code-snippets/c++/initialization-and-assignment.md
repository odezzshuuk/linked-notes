# Initialization and Assignment

> effective-c++ Initialize Class Members

```c++
#include <list>
#include <memory>
#include <vector>

class PhoneNumber {
};
class ABEntry {
public:
    ABEntry(const std::string& name, const std::string& address,
            const std::list<PhoneNumber>& phones);

private:
    std::string theName;
    std::string theAddress;
    std::list<PhoneNumber> thePhones;
    int numTimesConsulted;
};
ABEntry::ABEntry(const std::string& name, const std::string& address,
                 const std::list<PhoneNumber>& phones)
{
    /// This is assignment, not initialization
    theName = name;
    theAddress = address;
    thePhones = phones;
    numTimesConsulted = 0;
}

ABEntry::ABEntry(const std::string& name, const std::string& address,
                 const std::list<PhoneNumber>& phones)
    : theName(name), theAddress(address), thePhones(phones), numTimesConsulted(0)  
/// This is initialization, the result is the same as the previous constructor, but more efficient
{
}

```
