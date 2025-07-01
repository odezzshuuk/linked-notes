# CSharp - Task

* [What It Is](#what-it-is)
* [Task And Task<T>](#task-and-task<t>)
* [Task Status](#task-status)
* [TaskFactory](#taskfactory)
* [Wait A Task](#wait-a-task)
* [Handle Non-cancel Exception In Task In Calling Method](#handle-non-cancel-exception-in-task-in-calling-method)
* [Method task.Wait() Vs Keyword Await](#method-task.wait()-vs-keyword-await)
* [Take A Look](#take-a-look)

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
  \_ `Task<T>` is a asynchronous operation that returns a value of type `T`

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

what's the difference between declare async method return `Task` and `void`?

public async Task ExampleMethod();
public async void ExampleMethod();

## Wait A Task

3 ways to wait a task

1. `Task.Wait()`
2. `Task.GetAwaiter().GetResult()`
3. `await Task`

| Feature               | Task.Wait()                             | Task.GetAwaiter().GetResult()          | await Task                               |
| --------------------- | --------------------------------------- | -------------------------------------- | ---------------------------------------- |
| Blocking              | Synchronous (blocks thread)             | Synchronous (blocks thread)            | Asynchronous (non-blocking)              |
| Returns               | Nothing (access Task.Result separately) | Task’s result directly                 | Task’s result directly                   |
| Exception Handling    | Throws AggregateException               | Throws inner exception                 | Throws inner exception                   |
| Thread Safety (Unity) | Risks deadlock on main thread           | Risks deadlock on main thread          | Safe, respects Unity’s sync context      |
| Performance (Unity)   | Freezes game if on main thread          | Freezes game if on main thread         | Keeps game responsive                    |
| Use Case              | Rare; non-main-thread sync calls        | Rare; forced sync calls in legacy code | Preferred for async operations in Unity  |
| Unity Friendliness    | Poor (avoid on main thread)             | Poor (avoid on main thread)            | Excellent (designed for async workflows) |

## Handle Non-cancel Exception In Task In Calling Method

1. when `Task.Wait()`

- Exception is wrapped in an `AggregateException.InnerExceptions`
- Catch the `AggregateException` to get the Non-cancel exception

```cs
public static void ExampleMethod() {
  var task = Task.Run(static () => throw new CustomException("Inside Task Exception"));

  try {
    task.Wait();
  } catch (AggregateException e) {
    foreach (var ex in e.InnerExceptions) {
      if (ex is CustomException customEx) {
        Console.WriteLine(customEx.Message);
      } else {
        Console.WriteLine("Other exception: " + ex.Message);
      }
    }
  }
}
```

2. when `await` the task

- Handle Exception Like a normal exception

```cs
public static async Task ExampleMethod() {
  var task = Task.Run(static () => throw new CustomException("Inside Task Exception"));

  try {
    await task;
  } catch (Exception e) {
    Console.WriteLine(e.Message);
  }
}
```

## Method task.Wait() Vs Keyword Await

Blocking vs Non-blocking

- `Wait()` is a blocking method
- `await` do not block current thread

Exception Handling When Task Is Canceled

- Method `task.Wait()` throw exception, such as `TaskCanceledException`, by wrapping it in an `AggregateException`
- `Await` throw actual exception, such as `OperationCanceledException`

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
