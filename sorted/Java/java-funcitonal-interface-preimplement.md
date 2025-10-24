# Predefined Functional Interfaces

## Generic Functional Interface

| Functional Interface   | Parameter Type | Return Type | Abstract Method Name | Description                                 | Other Methods                   |
| ------------------- | -------------- | ---------- | -------------------- | ------------------------------------------- | ------------------------------- |
| `Runnable`          | None           | void       | run                  | Action with no parameters or return value    |                                 |
| `Supplier<T>`       | None           | T          | get                  | Provides a value of type T                  |                                 |
| `Consumer<T>`       | T              | void       | accept               | Processes a value of type T                 | andThen                         |
| `BiConsumer<T, U>`  | T, U           | void       | accept               | Processes values of type T and U            | andThen                         |
| `Function<T, R>`    | T              | R          | apply                | Function with a parameter of type T         | compose, andThen, identity      |
| `BiFunction<T, U, R>` | T, U         | R          | apply                | Function with parameters of type T and U    | andThen, identity               |

These functional interfaces have a method `apply()`, which means calling this function object with the parameters passed to apply.

example

- function type: `BiFunction<T, U, R>`
- method to use a function argument: `public String mergeString(String a, String b, BiFunction<T, U, R> func)`
- call the function argument with given parameter: `func.apply(a, b)`

```java
public class Demo {
    public String mergeString(String a, String b, BiFunction<T, U, R> func) {
        return func.apply(a, b);
    }

    public String fx(String a, String b) {
      return a + b;
    }

    public static void main(String[] args) {
        Demo demo = new Demo();
        String result = demo.mergeString("a", "b", demo::fx);
        System.out.println(result);
    }
}
```

## Primitive Type Functional Interfaces

| Functional Interface | Parameter Type | Return Type | Abstract Method Name |
| -------------------- | -------------- | ----------- | -------------------- |
| BooleanSupplier      | none           | boolean     | getAsBoolean         |
| PSupplier            | none           | p           | getAsP               |
| PConsumer            | p              | void        | accept               |
