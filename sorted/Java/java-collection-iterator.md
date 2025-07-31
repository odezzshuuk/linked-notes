# Iterator

## Get Iterator

```java
Iterator it = coll.iterator();
```

- The initial position of the iterator is before the first element of the collection.

## Traversing Elements

- `it.next()`: Returns the next element in the collection `coll`.
- `it.hasNext()`: Checks if there are more elements in the collection `coll`.

## `remove()` Method

- If the underlying collection is modified in any way during iteration, other than by calling this method, the behavior of the iterator is unspecified, unless an overriding class specifies a concurrent modification policy.
- After calling the `forEachRemaining` method, the behavior of the iterator is unspecified.
