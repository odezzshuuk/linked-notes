# CSharp - Event

## What is Event

- A special kind of multicast [delegate](csharp-delegate.md)

## Features

## 3 Parts of An Event System

- [Publish]()
- Subscribe
- Trigger

> [Subscriber]() registers a method to an event member of a [publisher]()

## Publish Event

What's Publisher Do

- Define Event: `public event Handler CountedADozen;`
  - event keyword
  - delegate type
- Trigger Event: When triggered, the all the methods registered to the event are executed

```c
delegate void Handler();

class Incrementer
{
    // declare event
    public event Handler? CountedADozen;

    // trigger event
    public void DoCount()
    {
        for (int i = 1; i < 100; i++) {
            if (i % 12 == 0 && CountedADozen != null)
                CountedADozen();
        }
    }
}
```

## Subscribe Event

- `incrementer.CountedADozen += IncrementDozenCount;`

```c
class Dozens
{
    public int DozensCount {get; private set;}

    public Dozens(Incrementer incrementer)
    {
        DozensCount = 0;
        
        // register event
        incrementer.CountedADozen += IncrementDozensCount;
    }

    void IncrementDozensCount()
    {
        DozensCount++;
    }
}
```

## Trigger Event

```c
class Program
{
    static void Main()
    {
        Incrementer incrementer = new Incrementer();
        Dozens dozensCounter = new Dozens(incrementer);
    
        incrementer.DoCount();
        Console.WriteLine("Number of dozens = {0}",     
            dozensCounter.DozensCount); 
    }
}
```

## Standard Events

[Standard Events](csharp-events-eventshandles.md)

## Event Accessor

```c#
public event EventHandler CountADozen
{
    add
    {
        ...
    }
    remove
    {
        ...
    }
}
```

## Sample Code

[code](csharp-event-code.md)

