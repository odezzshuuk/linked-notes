# Constructor

- Same name as the class.
- A class can have multiple constructors.
- No return value.
- Always accompanied by `new` (unlike C++).

## Calling Another Constructor Using `this`

```java
public Employee(double s)
{
    this("Employee #" + nextId, s);  // Will call another constructor
    nextId++;
}
```

