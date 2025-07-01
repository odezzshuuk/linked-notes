# CSharp - Keywords

## yield

[yield](csharp-yield.md)

## using

## new

declared modifier

- Represent a member that is **hidden** by a similar named member in a base class

## out

parameter modifier

- pass a reference parameter to a method
  - the arugment need not be initialized before calling the method
  - but must assign a value before returning

## params

- Declare a mutable number of parameters
- The type of the parameter must be a single-dimensional array
- No other parameter is allowed after params
- Only one `params` is allowed

```cs
public void UseParams(params int[] list)
{
    for (int i = 0; i < list.Length; i++)
    {
        Console.Write(list[i] + " ");
    }
    Console.WriteLine();
}
```


## base

## event

[with or without event keyword](csharp-events.md#with-vs-without-event-keyword)

