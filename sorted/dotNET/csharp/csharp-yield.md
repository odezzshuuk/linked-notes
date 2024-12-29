# CSharp - Keyword yield

## What's For

- Make a method [Iterator](csharp-iterator.md)
- Most common way to create an [Iterator](csharp-iterator.md)

## Features

- C# compiler will transform the method into a class that implements [`IEnumerator`](csharp-ienumerator.md) interface

## Execution

```cs
public class Program {
    public static void Main()
    {
        IEnumerable<int> numbers = GetNumbers();
        var enumerator = GetNumbers().GetEnumerator();
        Console.WriteLine("GetNumbers() called");

        enumerator.MoveNext();
        int value2 = enumerator.Current;
        Console.WriteLine(value2);

        enumerator.MoveNext();
        int value3 = enumerator.Current;
        Console.WriteLine(value3);

        enumerator.MoveNext();
        int value4 = enumerator.Current;
        Console.WriteLine(value4);
    }

    public static IEnumerable<int> GetNumbers()
    {
        Console.WriteLine("GetNumbers() Executed");
        yield return 1;
        yield return 2;
        yield return 3;
    }
}
```

Output:

```sh
GetNumbers() called
GetNumbers() Executed
1
2
3
```

Explanation:

1. when the iterator method is first called, it doesn't execute any code
2. When iterate with `foreach`, the method will execute until it reaches a `yield` statement and return the value
3. When `MoveNext()` is called, the method will start from where it left off(just after yield return), until it reaches another `yield` statement
4. End of the collection, `MoveNext()` return false

