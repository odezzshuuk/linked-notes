# Java Modifier

## Introduction

- Modifier is reflected to int
- Modifier list
  - `public`
  - `protected`
  - `private`
  - `abstract`
  - `static`
  - `final`
  - `sealed`
  - `non-sealed`
  - `strictfp`

converts int to string represent the modifier

- use static Method `Modifier.toString()`

```java
public class Demo {
  private Date date;
  public static void main(String[] args) {
    Class<?> cls = Demo.class;
    Field[] fl = cls.getDeclaredFields();
    for (Field f : fl) {
      System.out.println(Modifier.toString(f.getModifiers()) + " " + f.getType().getName() + " " + f.getName());
    }
}
```

```java
private
```

## get Modifier

- foo.getModifiers(): Returns int, representing the modifier of the Class instance

> foo is instance of Class, Field, Method
> Static method: Modifier.toString() converts the integer representing Modifier to a string;
