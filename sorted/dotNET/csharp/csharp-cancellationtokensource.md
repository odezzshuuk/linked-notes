# CSharp - CancellationTokenSource

## What It Is

- To cancel asynchronous operation or thread
- Source of [`CancellationToken`](csharp-cancel-task.md)
- Signal to cancel a task by calling `CancellationTokenSource.Cancel()`

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


