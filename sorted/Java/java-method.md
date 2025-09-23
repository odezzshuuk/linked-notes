# Method

## Abstract Method

- keyword `abstract`
- provide **signature** ，**return type**，**throw exception type**
- no implement

## Default Method

- add keyword `default` before method
- Mainly used for interfaces
- 隐式声明为public, 因此public关键字可省略
- Default methods can add new functionality to library interfaces and ensure binary compatibility with code written for older versions of those interfaces

## Static Method

- 隐式声明为public, 因此public关键字可省略
- Associated with the **class**, not with any **instance**
- Accessed directly by class name

## Method Signature

- method name and parameter list

## Method Overloading

- same method name, different parameter list

> unrelated to the return type


## inline method

- In Java, whether a method is inlined is determined by the JVM
- 简洁，经常被调用，没有被重载以及可优化的方法

## Method Parameters

- Cannot modify a parameter of a primitive type.
- Can change the state (content) of an object parameter.
- Cannot make an object reference a new object.
- Passing method: It is passed by value.

An example to demonstrate function parameter passing method

```java
public static void swap(Employee x, Employee y)
{
    Employee temp = x;
    x = y;
    y = temp;
}
Employee a = new Employee("Alice",1000);
Employee b = new Employee("Bob",2000);
swap(a, b);
```

## mutable parameters  

- declare by `foo(type... args)` syntax
- access by `args[i]` in method body

```java
public static double max(double... values) {
    double largest = Double.NEGATIVE_INFINITY;
    for (double v : values) {
        if (v > largest) largest = v;
    }
    return largest;
}
```
