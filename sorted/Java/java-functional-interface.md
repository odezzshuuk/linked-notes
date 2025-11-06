# Functional Interface

## Definition

[Definition](java-functional-interface-definition.md)

## Instances of Functional Interfaces

1. [Lambda Expression](java-lambda.md)

2. Method Reference

- `ClassName::MethodName` Called via class name
- `this::instanceMethod`
- `super::instanceMethod`

```java
public class MethodReference {
    public static void main(String[] args) {
    }

    public void takeMethodFunc(String a, String b, Function<T> func) {
        func.apply(a, b);
    }

    public void fx()

}
```

3.contructor reference

- `ClassName::new`

## Predefined Functional Interfaces

[Predefined Functional Interfaces](java-funcitonal-interface-preimplement.md)
