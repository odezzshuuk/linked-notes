# CSharp - Cancel Task

## Cooperation With CancellationToken

Check `CancellationToken`'s `IsCancellationRequested` property

- **Optional(not recommend)**: When cancellation is requested, Replace `token.ThrowIfCancellationRequested()` with `return`

```cs
Task.Run(() => {
    for (int i = 0; i < 100; i++) {
        if (token.IsCancellationRequested) {
            Console.WriteLine("Task canceled.");
            token.ThrowIfCancellationRequested();
        }
    }
})
```

Cancel a async operation before it starts by pass a `CancellationToken` as parameter [task](csharp-task.md) api, such as `Task()`, `Task.Run()`

```cs
CancellationTokenSource source = new();
CancellationToken token = source.Token;
source.Cancel();
Task.Run(() => {
    for (int i = 0; i < 100; i++) {
        if (token.IsCancellationRequested) {
            Console.WriteLine("Task canceled.");
            token.ThrowIfCancellationRequested();
        }
    }
}, token);
```

- task will not start

## TaskCanceledException

- Inherits from [OperationCanceledException](csharp-cancellation#OperationCanceledException)

> OperationCanceledException is thrown instead when [await](csharp-task.md#wait-vs-await) a canceled task

Thrown wrapped in an `AggregateException` when:

- A CancellationTokenSource.ThrowIfCancellationRequested() is called
- And the task is waited by wait api is called, such as `Task.Wait()`

```cs
Task task = Task.Run(() => {
    for (int i = 0; i < 100; i++) {
        if (token.IsCancellationRequested) {
            Console.WriteLine("Task canceled.");
            token.ThrowIfCancellationRequested();
        }
    }
}, token);

try {
    task.Wait();
} catch (AggregateException ae) {
    foreach (Exception e in ae.InnerExceptions) {
        if (e is TaskCanceledException) {
            Console.WriteLine("Task was cancelled");
        }
    }
}
```

