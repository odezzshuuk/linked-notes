# CSharp - CancellationTokenSource

## What It Is

- To cancel asynchronous operation or thread
- Source of `CancellationToken`
- Signal to cancellation by calling `Cancel()`

## Cancel()

## Take A Look

```cs
CancellationTokenSource source = new();
CancellationToken token = source.Token;
Task.Run(() =>
{
    for (int i = 0; i < 100; i++)
    {
        if (token.IsCancellationRequested)
        {
            Console.WriteLine("Task canceled.");
            return;
        }
    }
}, token);
```


