# CSharp - Extension Method

- static class
- static method
- paramter format: `this typename arg`

```cs
public class Point
{
    public int X { get; set; }
    public int Y { get; set; }

    public Point(int x, int y)
    {
        X = x;
        Y = y;
    }

    public int Distance()
    {
        return X * X + Y * Y;
    }
}

public static class PointPlus
{
    public static void Plus(this Point p)
    {
        Console.WriteLine(p.X + p.Y);
    }
}

public class Program
{
    public static void Main()
    {
        Point p = new(3, 5);
        p.Plus();
    }
}
```
