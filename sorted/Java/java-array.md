# Array

- Is a [reference type].
- The element type must be the same.
- The number of elements must be specified.
- The length of the array cannot be changed.
- The initial values are 0, 0.0, false.

## Creating an Array

```java
int[] a1 = new int[5];               // Create an array of length 5, with element values of 0.
int[] a2 = {1, 2, 3, 4, 5};          // Create an array of length 5, with element values of 1, 2, 3, 4, 5.
int[] a3 = new int[]{1, 2, 3, 4, 5}; // Create an array of length 5, with element values of 1, 2, 3, 4, 5.
```

## Elements

- The value of an array element is an address, referencing an object instance.

## Array Copying

- Copies the specified array, truncating or padding it.

```java
Arrays.copyOf(T[] original, int newLength)
```
