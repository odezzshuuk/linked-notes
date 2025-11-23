# CSharp - IDisposable

* [What's For](#what's-for)
* [Unmanaged Resources](#unmanaged-resources)
* [Managed Resources](#managed-resources)
* [using Statment](#using-statment)
* [try-finally](#try-finally)

## What's For

- Clean up unmanaged resources or managed resources that wrap unmanaged resources
- Clean up event handlers to prevent memory leaks
  - The publisher will hold a reference to the subscriber, preventing the garbage collector from collecting the subscriber object

## Unmanaged Resources

- Resources automatically handled by the [CLR](dotnet-glossary.md#clr), such as memory allocated on the managed heap

## Managed Resources

- Such as file handles, network sockets, database connections, COM objects

## How To Implement Dispose()



## using Statment

```c
using System.IO;

class UsingDeclaration
{
    static void Main()
    {
        var buffer = new char[50];
        using StreamReader streamReader = new("file1.txt");

        int charsRead = 0;
        while (streamReader.Peek() != -1)
        {
            charsRead = streamReader.Read(buffer, 0, buffer.Length);
            //
            // Process characters read.
            //
        }
    }
}
```

- the using statement doesn't explicitly call the `Dispose()` method
- its equivalent to [try-finally](#try-finally) block, `Dispose()` method is called in the `finally` block

## try-finally

```c
using System.IO;

class TryFinallyGenerated
{
    static void Main()
    {
        var buffer = new char[50];
        StreamReader? streamReader = null;
        try
        {
            streamReader = new StreamReader("file1.txt");
            int charsRead = 0;
            while (streamReader.Peek() != -1)
            {
                charsRead = streamReader.Read(buffer, 0, buffer.Length);
                //
                // Process characters read.
                //
            }
        }
        finally
        {
            // If non-null, call the object's Dispose method.
            streamReader?.Dispose();
        }
    }
}
```
