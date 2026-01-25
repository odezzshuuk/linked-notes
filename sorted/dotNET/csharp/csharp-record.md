# CSharp - Record

* [vs class](#vs-class)

## What's For

- To define a **Reference Type** that providers built-in functionality for **encapsulating data**

## VS class

1. **Value-based equality** by default

```cs
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

```cs
var person = new Person("John", "Doe");
var (firstName, lastName) = person; // Deconstructing
```

## VS struct

```cs
public struct Point {
    public int X = 5
    public int Y = 10;
}
```
