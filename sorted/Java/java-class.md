# Class

## Initialization

[Initialization](java-class-initialize.md)

## `this`

- In a constructor, `this(param list)` should be called before other executable statements and after the `super` constructor statement.

## Abstract Class

```java
public abstract class AbstractClass {
    public abstract void abstractMethod();
}
```

- A class **containing an abstract method** must be declared as an abstract class.
- An abstract class **may contain** abstract methods.
- Can be used for declaration: `Foo a;`.
- **Cannot** be instantiated: `Foo a = new Foo();` is illegal.
- Subtypes must override abstract methods.
- Used for inheritance.

## Nested Class

[Nested Class](java-nested-class.md)
