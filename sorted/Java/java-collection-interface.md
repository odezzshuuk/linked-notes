# Collection Interface

- Represents a group of objects.

## Interface `Collection`

- `Iterable<E>`, is the superinterface of all `Collection`-related interfaces, where `E` defaults to `Object`.
- The root interface for implementing classes that contain a group of elements.

Classes that implement `Collection<T>` provide two constructors:

- To create an empty collection.
- To copy a collection.

```java
new HashSet<>();
new HashSet<>(Collection<? extends E> c);
```

The `for(element e : IterableInstance)` statement can only be used with classes that implement the `Iterable<E>` interface.

## Subinterfaces of `Collection`

### Interface `Set`

- A collection that does not contain duplicate elements.

> In other words, there will not be two elements `e1` and `e2` such that `e1.equals(e2)` is true.

- Interface `SortedSet`

### Interface `List`

- Can contain duplicate elements.
- Elements can be accessed by index.
- Elements can be inserted at any position.

### Interface `Queue`

- A queue collection.

### Interface `Deque`

- A double-ended queue collection.
