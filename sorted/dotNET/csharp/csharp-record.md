# CSharp - Record

- To define a **Reference Type** that providers built-in functionality for **encapsulating data**

## vs class

1. **immutable** by default

```c
public record Person {
    public string FirstName { get; init; }
    public string LastName { get; init; }
}

Person person = new Person { FirstName = "John", LastName = "Doe" };
person.LastName = "Smith"; // Error
```

- Create new instance use `with` expression to change property value

```c
Person updatedPerson = person with { LastName = "Smith" };
```

2. **Value-based equality** by default

```
var person1 = new Person { FirstName = "John", LastName = "Doe" };
var person2 = new Person { FirstName = "John", LastName = "Doe" };
Console.WriteLine(person1 == person2); // True
```

3. **Deconstructor** by default

> class do not have built-in deconstructor

```c
var person = new Person("John", "Doe");
var (firstName, lastName) = person; // Deconstructing
```




