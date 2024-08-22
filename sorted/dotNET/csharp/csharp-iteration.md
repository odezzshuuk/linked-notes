# CSharp - Iteration

* [Iterator](#iterator)
* [IEnumerator](#ienumerator)
* [IEnumerable](#ienumerable)
* [Generic Iteratable](#generic-iteratable)

## Iterator

[Iterator](csharp-iterator.md)

## IEnumerator

[IEnumerator](csharp-ienumerator.md)

## IEnumerable

[IEnumerable](csharp-ienumerable.md)


## Generic Iteratable

Method `GetEnumerator()` 

- return a [`IEnumerator<T>`](#ienumerable) instance
- There are two ways to create `IEnumerator<T>` instance
  - Define a new class `PeopleEnumerator` which implements `IEnumerator<T>` interface
  - Or use [`yield`](csharp-yield.md) keyword

Alternative of `class PeopleEnumerator`: yield ienumerator

```c
public IEnumerator<Person> GetEnumerator()
{
    foreach (Person p in _people)
    {
        yield return p;
    }
}
```



