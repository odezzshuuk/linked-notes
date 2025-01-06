# Factory Method

## Feature

## Interface

Creator.java

- Creator Interface, contains an abstract method, used to create Product object

```java
public interface Creator {
    public Product factory();
}
```

Product.java

- Product Interface

```java
public interface Product {

    public void method1();
    public void method2();
}
```

## Example

Factory

- `ConcreteCreator.java`

```java
public class ConcreteCreator implements Creator {

    @Override
    public Product factory() {
        return new ConcreteProduct();
    }
}
```

Product

- `ConcreteProduct.java`

```java
public class ConcreteProduct implements Product {

    @Override
    public void method1() {
        // method body
    }

    @Override
    public void method2() {
        // method body
    }
}
```

Application Code

```java
public class FactoryMethodDemo {
    public static void main(String[] args) {
        Creator creator = new ConcreteCreator();
        Product product = creator.factory();
        product.method1();
        product.method2();
    }
}
```

