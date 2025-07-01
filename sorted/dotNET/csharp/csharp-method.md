# CSharp - Method 

## Parameter

Arguments are passed by value by default

When a reference type is passed by value to a method, the method receives a copy of the reference to the class instance.

- Both variables refer to the same object. 
- The parameter is a copy of the reference. 

**The called method can't reassign the instance in the calling method** 

- this will only set the local reference to a new instance, not the original reference
- Or this only changes the local copy **points to**
- modifier `ref` or `out` can be used to change the original reference

```cs
public void Method1(Point point)
{
    // `point` is a local copy of the reference
    point = new Point(10, 10);  // This will not change the original instance
}
```


**However, the called method can use the copy of the reference to access the instance members**

```cs
public void Method2(Point point)
{
    point.X = 10;  // This will change the original instance
}
```

## Extension Method

[extend](csharp-extension-method.md)

## ref return

```cs
public class A {
  private int[] _array = new int[10];
  public ref int GetNumber(int index) {
    return ref _array[index];
  }
}
public class Program {
  public static void Main() {
    A a = new A();
    Console.WriteLine(a.GetNumber(5)); // Output: 0
    ref int temp = ref a.GetNumber(5);
    temp = 42; // Modify the value at index 5
    Console.WriteLine(a.GetNumber(5)); // Output: 42
  }
}
```

