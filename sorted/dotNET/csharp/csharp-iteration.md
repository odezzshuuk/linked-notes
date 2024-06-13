# CSharp - Iteration

## IEnumerator

[IEnumerator](csharp-ienumerator-interface.md)

has 3 method: Current, MoveNext, Reset

- Current
- MoveNext
- Reset

## IEnumerable

- used in `foreach(Type VarName in EnumerableObject)`, `EnumerableObject` must be an instance of a class that implements `IEnumerable` interface
- [IEnumerable](#IEnumerable) call its GetEnumerator method return instance of [IEnumerator interface](#IEnumerator)

## Generic Iteratable

```c
using System;
using System.Collections;
using System.Collections.Generic;

// Simple business object.
public readonly struct Person(string firstName, string lastName)
{
    public string FirstName { get; } = firstName;
    public string LastName { get; } = lastName;
}

// Collection of Person objects. This class
// implements IEnumerable so that it can be used
// with ForEach syntax.
public class PeopleCollection : IEnumerable<Person>
{
    private readonly Person[] _people;
    public PeopleCollection(Person[] pArray)
    {
        _people = new Person[pArray.Length];

        for (int i = 0; i < pArray.Length; i++)
        {
            _people[i] = pArray[i];
        }
    }

    // Implementation for the GetEnumerator method.
    IEnumerator<Person> IEnumerable<Person>.GetEnumerator()
    {
        return GetEnumerator();
    }

    public PeopleEnumerator GetEnumerator()
    {
        return new PeopleEnumerator(_people);
    }

    // Must also implement IEnumerable.GetEnumerator
    IEnumerator IEnumerable.GetEnumerator()
    {
        return GetEnumerator();
    }

}

// When you implement IEnumerable, you must also implement IEnumerator.
public struct PeopleEnumerator() : IEnumerator<Person>
{
    private readonly Person[] People { get; }

    // Enumerators are positioned before the first element
    // until the first MoveNext() call.
    private int position = -1;

    public PeopleEnumerator(Person[] people) : this()
    {
        People = people;
    }

    public bool MoveNext()
    {
        position++;
        return position < People.Length;
    }

    public void Reset()
    {
        position = -1;
    }

    readonly object IEnumerator.Current => Current;

    public readonly Person Current
    {
        get
        {
            try
            {
                return People[position];
            }
            catch (IndexOutOfRangeException)
            {
                throw new InvalidOperationException();
            }
        }
    }

    public readonly void Dispose() { }
}

public class App
{
    public static void Main()
    {
        Person[] peopleArray =
        [
            new("John", "Smith"),
            new("Jim", "Johnson"),
            new("Sue", "Rabon")
        ];

        PeopleCollection peopleList = new(peopleArray);
        foreach (Person p in peopleList)
        {
            Console.WriteLine(p.FirstName + " " + p.LastName);
        }
    }
}

/* This code produces output similar to the following:
 *
 * John Smith
 * Jim Johnson
 * Sue Rabon
 */

```

Method `GetEnumerator()` 

- return a [`IEnumerator<T>`](#ienumerable) instance
- There are two ways to create `IEnumerator<T>` instance
  - Define a new class `PeopleEnumerator` which implements `IEnumerator<T>` interface
  - Or use [`yield`](#csharp-yield.md) keyword

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


## Iterator

[Iterator](csharp-iterator.md)

- Iterator: A method return [`IEnumrator<T>`](csharp-ienumerator-interface.md) interface
- [yield](csharp-yield.md)

