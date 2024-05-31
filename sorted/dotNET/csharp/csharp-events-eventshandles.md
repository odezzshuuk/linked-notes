# CSharp - Standard Event

[code](csharp-standard-event-code.md)

## EventHandler

`public delegate void EventHandler(object sender, EventArgs e);`

- parameters
  - sender: object, event publisher
  - e: store information about the event

```c
using System;

class Program
{
    static void Main()
    {
        Incrementer incrementer = new Incrementer();
        Dozens dozensCounter = new Dozens(incrementer);

        incrementer.DoCount();
        Console.WriteLine("Number of dozens = {0}", dozensCounter.DozensCount);
    }
}
```

## Passing Data


```c#
public class IncrementerEventArgs: EvnetArgs
{
    public int InterrationCount{get;set;}
}
```

