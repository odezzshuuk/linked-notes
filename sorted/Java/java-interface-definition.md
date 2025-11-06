# Defining Interfaces

- If the interface modifier doesn't specify public, it's considered that only the same package has access permission to the interface
- Interfaces can extend other interfaces, and an interface can extend any number of interfaces

Taking Comparable as an example

```java
public interface Comparable
{
    int compareTo(Object other);
}
```

> That is, any class that implements the Comparable interface needs to include the compareTo() method

## Method Declarations in Interfaces

- All methods are implicitly public
- Can contain [abstract methods](), [default methods](), [static methods]()
- Methods in interfaces ending with `;` are abstract methods
- Can contain [constant declarations], field declarations in interfaces default to `public static final`