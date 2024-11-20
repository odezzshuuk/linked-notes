# CSharp - Record

* [vs class](#vs-class)

## What's For

- To define a **Reference Type** that providers built-in functionality for **encapsulating data**

## vs class

1. **Value-based equality** by default

```c
public record Person {
    public string FirstName { get; init; }
    public string LastName { get; init; }
}

var person1 = new Person { FirstName = "John", LastName = "Doe" };
var person2 = new Person { FirstName = "John", LastName = "Doe" };
Console.WriteLine(person1 == person2); // True
```

2. **Deconstructor** by default

> class do not have built-in deconstructor

```c
var person = new Person("John", "Doe");
var (firstName, lastName) = person; // Deconstructing
```

