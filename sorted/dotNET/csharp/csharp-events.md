# CSharp - Event

* [What is Event](#what-is-event)
* [Features](#features)
* [With vs Without event keyword](#with-vs-without-event-keyword)
* [EventHandler vs Action](#eventhandler-vs-action)
* [3 Parts of An Event System](#3-parts-of-an-event-system)
* [Publish Event](#publish-event)
* [Subscribe Event](#subscribe-event)
* [Trigger Event](#trigger-event)
* [Standard Events](#standard-events)
* [Event Accessor](#event-accessor)
* [Sample Code](#sample-code)

## What is Event

- A special kind of multicast [delegate](csharp-delegate.md)

## Features

## With vs Without event keyword

- Use to Declare a delegate that can **only** be invoked from **within** the class that declared it

```cs
class Example {
    public event EventHandler<EventArgs> onUpdate0;
    public EventHandler<EventArgs> onUpdate1;
}
```

- With `event` keyword, 
  - Ensure that `onUpdate0` can be listened by other classes.
  - Meanwhile `onUpdate0` can only be invoked within `Example` class

## EventHandler vs Action

Purpose

- [`Action`](csharp-delegate.md#action): General for [callback]
- `EventHandler`: Designed for [event pattern]

Parameters

- `Action`: flexible parameters, based on generic format
- `EventHandler`: Has standard parameters, `object sender` and [`EventArgs e`]()
  - `object sender`: the sender of the event, generally pass `this`
  - `EventArgs e`: the event data

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

