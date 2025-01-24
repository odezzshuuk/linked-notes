# CSharp - Task

## What It Is

> like [`Promise`](javascript-promise.md) in JavaScript

`Task` for Asynchronous operation return nothing

- Doesn't have a `Result` property
- No value is produced when an `async` method is called

`Task<T>` for Asynchronous operation return T

- Contains a `Result` property of type `T`
- `Result` is a blocking property, try to access `Result` before the `Task` is completed will block the thread

## Task And Task<T>

- `Task` is an asynchronous operation that doesn't return a value
- `Task` is also provider of helper methods for asynchronous operations, such as `Wait()`, `WaitAll()`, `WaitAny()`, `Run()`, `WhenAll()`, `WhenAny()`, `FromResult()`, `FromCanceled()`, `FromException()`
_ `Task<T>` is a asynchronous operation that returns a value of type `T`

## Task Status

- Created
- WaitingForActivation
- WaitingToRun
- Running
- WaitingForChildrenToComplete
- RanToCompletion
- Canceled
- Faulted

## TaskFactory

Provides a way to create and start multiple tasks with the same configuration

```cs
var factory = new TaskFactory(cts.Token, TaskCreationOptions.LongRunning, TaskContinuationOptions.None, TaskScheduler.Default);
List<Task> tasks = [];
for (int i = 0; i < 10; i++)
{
  tasks.Add(factory.StartNew(() => { Console.WriteLine("Task is running"); }));
}
```

- tasks created by the factory will use the same `CancellationToken`

## Wait Api Vs Await

Blocking vs Non-blocking

- `Wait()` is a blocking method
- `await` do not block current thread

Exception Handling When Task Is Canceled

- Wait api throw exception, such as `TaskCanceledException`, by wrapping it in an `AggregateException`
- throw actual exception, such as `OperationCanceledException`

## Take A Look

create a task

```c
Task t = new Task(() => { Console.WriteLine("Task is running"); });
```

execute a task

```c
t.Start();
```

wait for a task

```c
t.Wait();
```

complete example

```c
public class Programm
{
  public static void Main()
  {
    Task t = new Task(() => { Console.WriteLine("Task is running"); });
    t.Start();
    t.Wait();  // without this line, the program will exit before the task is completed
  }
}
```
