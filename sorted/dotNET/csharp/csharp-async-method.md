# CSharp - Async Method

* [Features](#features)
* [await expression](#await-expression)
* [Return Type](#return-type)
* [Any type has a `GetAwaiter` method](#any-type-has-a-`getawaiter`-method)
* [`IAsyncEnumerable<T>`](#`iasyncenumerable<t>`)
* [Wait A Async Value In A Sync Method](#wait-a-async-value-in-a-sync-method)

## Features

- `async` modifier
- Contains await expression
- return `void`, `Task`,  `Task<T>`
- parameter can not be `out`, `ref`
- Name convention: `Async` suffix

## await expression

- await expression doesn't block the thread
- `await` operator suspends the enclosing async method
- **return the control to the caller** of the method
- `await` operator can only be used in an `async` method, function, or [lambda expression]()

> the enclosing method is `GetAnswerAsync()`

```c
public async Task<int> GetAnswerAsync()
{
    await Task.Delay(1000);
    return 42;
}
```

Take A Look

```cs
public class AwaitOperator
{
    public static async Task Main()
    {
        Task<int> downloading = DownloadDocsMainPageAsync();
        Console.WriteLine($"{nameof(Main)}: Launched downloading.");  // ② 

        int bytesLoaded = await downloading;
        Console.WriteLine($"{nameof(Main)}: Downloaded {bytesLoaded} bytes.");  // ④ 
    }

    private static async Task<int> DownloadDocsMainPageAsync()
    {
        Console.WriteLine($"{nameof(DownloadDocsMainPageAsync)}: About to start downloading.");  // ① 

        var client = new HttpClient();
        byte[] content = await client.GetByteArrayAsync("https://learn.microsoft.com/en-us/");  // return to main

        Console.WriteLine($"{nameof(DownloadDocsMainPageAsync)}: Finished downloading.");  // ③ 
        return content.Length;
    }
}
```

- Output looks like:

```
DownloadDocsMainPageAsync: About to start downloading.
Main: Launched downloading.
DownloadDocsMainPageAsync: Finished downloading.
Main: Downloaded 27700 bytes.
```

> the caller of `Main()` is [CLR](dotnet-glossary.md#CLR)

## Return Type

1. [`Task<T>`](csharp-task.md)
2. [Any type has a `GetAwaiter` method](#any-type-has-a-getawaiter-method)
3. [`IAsyncEnumerable<T>`](#iasyncenumerablet)

## Any type has a `GetAwaiter` method

- `GetAwaiter` method must return a type that implements `System.Runtime.CompilerServices.INotifyCompletion` interface

`ValueTask<T>` is a lightweight implementation of `Task<T>` provide by .NET

- In following code, replace `ValueTask<int>` with `Task<int>` is also correct
- But `Task<int>` is a [Reference type](csharp-value-reference.md), allocation in performance type

```c
class Program
{
    static readonly Random s_rnd = new Random();

    static async Task Main()
    {
        Console.WriteLine($"You rolled {await GetDiceRollAsync()}");
    }

    static async ValueTask<int> GetDiceRollAsync()
    {
        Console.WriteLine("Shaking dice...");

        int roll1 = await RollAsync();
        int roll2 = await RollAsync();

        return roll1 + roll2;
    }

    static async ValueTask<int> RollAsync()
    {
        await Task.Delay(500);

        int diceRoll = s_rnd.Next(1, 7);
        return diceRoll;
    }
}
// Example output:
//    Shaking dice...
//    You rolled 8
```

## `IAsyncEnumerable<T>`

Combine the features of [`IEnumerable<T>`](csharp-ienumerable.md) and `async` method

## Wait A Async Value In A Sync Method

- Blocking the execution: use `GetAwaiter().GetResult()` or `Result` property
- Fire and forget:





