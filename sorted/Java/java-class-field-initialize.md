# Field Initialization Methods

## Explicit Initialization

```java
class Employee {
    private String name = "";
}
```

## Initialization Block

- Static initialization block, add `static` before a normal block.

```java
class Employee {
    {
        id = nextId;
        nextId++;
    }

    static {
        Random rd = new Random();
        nextId = rd.nextInt(10000);
    }
}
```

## Instance Field Initialization

- When an instance of a class is constructed, the initialization block is executed.

## Static Initialization Block

- A code block marked with `static`: `static {...}`.
- When a [class is first loaded], the static block is executed.
- Can be used to load resources into variables, avoiding the I/O overhead of multiple loads.
