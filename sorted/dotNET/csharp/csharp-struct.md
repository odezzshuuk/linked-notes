# CSharp - Struct

## What It Is

- Struct is a [value type](csharp-value-reference.md#value)
- Struct **Cannot** inherit from other [class]() or [struct]()
- Struct **CAN** contain data members and **function members**
- Struct **CAN** implement interface

## VS Class

```cs
public struct Point(int x, int y)
{
    public int X
    {
        get => x;
        set => x = value;
    }
    public int Y
    {
        get => y;
        set => y = value;
    }

}

public class Program
{
    public static void Main()
    {
        Point a = new(10, 10);
        Point b = a;
        a.X = 100;
        Console.WriteLine(b.X);
    }
}
```

- output: 10
- if `Point` is a class, the output will be 100
