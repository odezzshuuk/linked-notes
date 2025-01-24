# CSharp - Async

## Async Programming

What's For?

- Let blocking operation unblocking

Typical Cases

- Web Access
- Working with Files
- Working with images
- ...

## Async Method

[Async Method](csharp-async-method.md)

## Task

[Task](csharp-task.md)

## Cancellation

[Cancellation](csharp-cancellation.md)

## Async Operation VS Thread

| Aspect            | Asynchronous Operations                                      | Threads                                               |
| ----------------- | ------------------------------------------------------------ | ----------------------------------------------------- |
| Execution Model   | Non-blocking, event-driven.                                  | Dedicated execution unit for running code.            |
| Resource Usage    | Lightweight; managed by the runtime.                         | Expensive; consumes more system resources.            |
| Context Switching | Less frequent; relies on task continuations.                 | Requires context switching between threads.           |
| State Persistence | Execution pauses and resumes within the same logical thread. | Execution remains bound to a specific thread.         |
| Primary Use Cases | Managing I/O, waiting on network calls, timers, etc.         | Parallel processing, computationally intensive tasks. |
| Concurrency Type  | I/O-bound or task-based concurrency.                         | CPU-bound concurrency.                                |
| Thread Usage      | Does not necessarily use a new thread.                       | Always runs on a specific thread.                     |

- Async Operation is managed by the [runtime]()

## Lock Can Not Work With await

Explanation

- Deadlock Scenario: 
  - When an async method holds onto a lock and yields control to its caller with [`await`](/sorted/dotNET/csharp/csharp-async-method.md#await-expression)
  - The caller try to acquire the same lock before the async method completes


