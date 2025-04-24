# CSharp - Cancel Task

* [Cooperation With CancellationToken](#cooperation-with-cancellationtoken)
* [TaskCanceledException](#taskcanceledexception)

## Cooperation With CancellationToken

Cancel need **Cooperation**: 

1. Call `CancellationTokenSource.Cancel()` to toggle `CancellationToken.IsCancellationRequested` to `true`
2. Check `CancellationToken.IsCancellationRequested` cancel flag in wrapped function

Check `CancellationToken.IsCancellationRequested` property

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

## Pass CancellationToken VS Not Pass CancellationToken 

What's the difference between `Task.Run(callback)` and `Task.Run(callback, token)`?

- `Task.Run(callback)`: the scheduled task will still execute before cancellation token cancel flag is checked
- `Task.Run(callback, token)`: the scheduled task will never execute

By pass a canceled `CancellationToken` as parameter [task](csharp-task.md) api, such as `Task()`, `Task.Run()`, to prevent the task from starting

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

- task won't start

## TaskCanceledException

- Inherits from [OperationCanceledException](csharp-cancellation#OperationCanceledException)

> OperationCanceledException is thrown instead when [await](csharp-task.md#wait-vs-await) a canceled task

Thrown wrapped in an `AggregateException` when:

- A `CancellationTokenSource.ThrowIfCancellationRequested()` is called
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

