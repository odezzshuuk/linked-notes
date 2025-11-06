# Extending Superclasses

- In Java, a subclass can only extend a single class
- Existing class: superclass, base class, parent class
- New class: subclass, derived class

## Defining Subclasses

extends keyword

- Define Manager class, a subclass inherited from Employee class

```java
public class Manager extends Employee {}
```

## Calling Superclass

Keyword super

- Call superclass method `super.method()`
- Call superclass constructor `super(arg1, arg2,....);`

## Constructing Subclasses

- If the derived class's constructor doesn't call the parent class's constructor, it defaults to calling the superclass constructor super() as the first statement

## Overriding Methods

- The [return type] of the subclass method is less than or equal to that of the superclass method

  > A method in the superclass that returns **a superclass in a certain derived hierarchy**, when overridden in a subclass, can return **a subclass in the same derived hierarchy**
  
- The [exceptions] thrown by the subclass method are less than or equal to (not throwing or throwing fewer) those of the superclass method
- The visibility of the subclass method cannot be lower than the superclass

  > If superclass is public, the subclass method must be public
  
- @Override annotation

[Refer to override in C++](c++-virtual-function.md#override关键字)

## Method Invocation

- Static binding: private methods, static methods, final methods or constructors
- Dynamic binding: 

Resolution process for calling `e.getSalary()`

1. Extract the method table of the **actual type** of e
2. Search for the getSalary() method signature

## Method Table

- Lists all method signatures and the methods actually invoked

## Preventing Inheritance

- Declare a class as final to prevent inheritance
  - Its methods are automatically declared as final
  - Fields are not declared as final
- Declare a method as final, and subclasses cannot override this method