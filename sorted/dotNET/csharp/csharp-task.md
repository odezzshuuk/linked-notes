# CSharp - Task

## Task

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

## TaskFactory
