# Stream Util Collectors

- prefined collectors for most common operations

## toSet()

```java
List<Integer> numbers = List.of(1, 2, 3, 4, 5, 6 );
Set<integer> oddNumbers = numbers.parallelStream()
  .filter(x -> x % 2 ! = 0)
  .collect(Collectors.toSet());
```

## toMap()

```java
List<Integer> numbers = List.of(1, 2, 3, 4, 5, 6);

Map<Integer, String> mapOddNumbers = numbers.parallelStream()
  .filter(x -> x % 2 != 0)
  .collect(Collectors.toMap(Function.identity(), x -> String.valueOf(x)));
```

## joining()

`joining()`

`joining(CharSequence delimiter)`

`joining(CharSequence delimiter, CharSequence prefix, CharSequence suffix)`

```java
String[] list = {"a", "b", "c"};
String l = list.stream().collect(Collectors.joining(", ", "[", "]"));
System.out.println(l);  // [a, b, c]
```
