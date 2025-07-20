# Dynamic Memory Management

- #variable_memory #simplified_vector #object_moving #StrVec #allocate_class

  [[allocator class]]

```c++
#include "string"
#include <algorithm>
#include <memory>

class StrVec {
public:
    StrVec() : elements(nullptr), first_free(nullptr), cap(nullptr) {}
    StrVec(const StrVec&);                                    /// Copy constructor
    StrVec& operator=(const StrVec&);                         /// Copy assignment
    StrVec& operator=(std::initializer_list<std::string> il); /// Overload assignment operator
    ~StrVec();
    void push_back(const std::string&);                   /// Insert element
    size_t size() const { return first_free - elements; } /// Number of current elements
    size_t capacity() const { return cap - elements; }    /// Number of remaining elements that can be saved
    void reserve(size_t n);                               /// Accommodate n elements space
    std::string* begin() const { return elements; }       /// Returns a pointer to the first element
    std::string* end() const { return first_free; }       /// Returns a pointer to the end

private:
    static std::allocator<std::string> alloc; /// Create an allocator class
    void chk_n_alloc()
    {
        if (size() == capacity()) reallocate();
    }
    std::pair<std::string*, std::string*>
    alloc_n_copy(const std::string*, const std::string*); /// Allocate memory and copy elements in a given range
    void free();                                          /// Destroy constructed elements and release memory
    void reallocate();                                    /// Reallocate memory
    void reallocate(size_t);
    std::string* elements; /// Points to the first element of the allocated elements
    std::string* first_free; /// The first unallocated space pointer, that is, the next position of the last element
    std::string* cap;        /// Points to the position after the end of the memory
};
void StrVec::push_back(const std::string& s)
{
    chk_n_alloc();
    alloc.construct(first_free++, s); // Increment first_free
}
std::pair<std::string*, std::string*>
StrVec::alloc_n_copy(const std::string* e,
                     const std::string* b) /// Allocate memory and copy elements in a given range, return pair type
{
    auto data = alloc.allocate(e - b); /// data is a pointer to the first element of the unconstructed array
    return {data, uninitialized_copy(b, e, data)}; /// first: a pointer to the first element named data;
    /// second: a pointer to the end after copying the elements between b and e to the unconstructed space with data as the first element
}
void StrVec::free()
{
    if (elements) {
        for (auto p = first_free; p != elements;)   /// Traverse from the last element to the front
            alloc.destroy(--p);                     ///  Decrement and destroy the element before decrementing
        alloc.deallocate(elements, cap - elements); /// Release memory
    }
}
StrVec::StrVec(const StrVec& s) /// Copy constructor
{
    auto newdata = alloc_n_copy(s.begin(), s.end()); ///
    elements = newdata.first;                        /// Assign the value of the first element to the data member
    first_free = cap = newdata.second;               /// Assign the value of the tail element
}
StrVec::~StrVec()
{
    free();
}
StrVec& StrVec::operator=(const StrVec& rhs) /// Assignment operator, accepts a StrVec object
{
    auto data = alloc_n_copy(rhs.begin(), rhs.end());
    free();                /// Destroy elements and release memory
    elements = data.first; /// Update data members
    first_free = cap = data.second;
    return *this;
}
StrVec& StrVec::operator=(
    std::initializer_list<std::string> il) /// Overload assignment operator, accepts an initializer_list<string> object
{
    auto data = alloc_n_copy(il.begin(), il.end()); /// Returns the head and tail pointers to data
    free();                                         /// Destroy the current element and release the memory
    elements = data.first;
    first_free = cap = data.second;
    return *this;
}
void StrVec::reallocate() /// Reallocate space
{
    auto newcapacity = size() ? 2 * size() : 1; /// If it is not empty, it will be expanded to twice the original size, and if it is empty, a space for one element will be allocated.
    auto newdata = alloc.allocate(newcapacity); /// Allocate space for newcapacity elements
    auto dest = newdata;
    auto elem = elements;
    for (size_t i = 0; i != size(); ++i)
        alloc.construct(
            dest++,
            std::move(
                *elem++)); /// Traverse the elements, the elements in the container are constructed by the moved string object, and the move constructor of the string is used
    free();
    elements = newdata;           /// Update pointer
    first_free = dest;            /// Update pointer
    cap = elements + newcapacity; /// Update pointer
}
void StrVec::reallocate(size_t newcapacity)
{
    auto newdata = alloc.allocate(newcapacity);
    auto dest = newdata;
    auto elem = elements;
    for (size_t i = 0; i != size(); ++i) alloc.construct(dest++, std::move(*elem++));
    free();
    elements = newdata;
    first_free = dest;
    cap = elements + newcapacity;
}

void StrVec::reserve(size_t n) /// Accommodate n elements space
{
    if (capacity() < n) reallocate(n);
}
#endif // CPPPRIMER_STRVEC_H
```