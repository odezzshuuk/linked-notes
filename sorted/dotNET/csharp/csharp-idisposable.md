# CSharp - IDisposable

## What's For

## Unmanaged Resources

## Managed Resources

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
