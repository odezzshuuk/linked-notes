# Concrete Implementations

| Interfaces   | Hash Table | Resizable Array | Tree    | Linked List | Hash table + Linked list |
|--------------|------------|-----------------|---------|-------------|--------------------------|
| Set          | HashSet    |                 | TreeSet |             | LinkedHashSet            |
| List         |            | ArrayList       |         | LinkedList  |                          |
| Queue, Deque |            | ArrayDeque      |         | LinkedList  |                          |
| Map          | HashMap    |                 | TreeMap |             | LinkedHashMap            |

- All implementations provide all optional operations contained in their interfaces.
- All elements allow null elements, keys, and values.
- Thread-safe.
- Can be serialized.
- Supports `clone()`.

## LinkedList

## ArrayList

## HashSet

- [Hash table] computes an integer for each object, called a hash code.

## TreeSet

- `TreeSet<T>`
- Inserts in any order, outputs in sorted order.
- Implemented with a red-black tree.

## Map

### API

- `HashMap<K, V>`
- Adding elements:
  - `V put(K key, V value)`
- Updating values:
  - `V put(K key, V newVal)`
  - `V merge(K key, V value, BiFunction<? super V, ? super V, ? extends V> remappingFunction)`

  ```java
  map.merge(key, msg, String::concat)
  ```

- Returning a collection of keys or values:
  - Key Set: `Set<K> keySet()`, the returned Set is not a `HashSet` or `TreeSet`.
  - Value Collection: `Collection<V> values()`
  - Key-Value Set: `Set<Map.Entry<K, V>> entrySet()`

### WeakHashMap

- For other Map objects, if an object is active, the garbage collector will not reclaim objects in the Map that are no longer referenced by values.
- Therefore, `WeakHashMap<K, V>` was designed. The existence of a mapping for a given key in a `WeakHashMap` does not prevent that key from being discarded by the garbage collector.

## LinkedHashSet and LinkedHashMap

- Used to remember the insertion order of elements.
- Elements affected by `get()` or `put()` calls will be removed from their current position and placed at the end of the linked list.
- Constructor: `LinkedHashMap<K, V>(initialCapacity, loadFactor, true)`
- Can keep frequently accessed elements in memory, while less frequently accessed elements are read from the database.

