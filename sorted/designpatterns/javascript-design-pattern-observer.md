# Javascript Design Pattern - Observer

* [Feature](#feature)
* [VS Mediator](#vs-mediator)
* [Components For This Pattern](#components-for-this-pattern)
* [Publisher/Observable](#publisher/observable)
* [Subscriber Interface](#subscriber-interface)
* [Concrete Subscriber](#concrete-subscriber)
* [Code](#code)

## Feature

- kind of behavioral pattern
- one-to-many communication between objects
- many is called observers
- one is called subject
- when publisher changes, all observer will be notified
- the subscribe operation is done by [publisher/observable](#publisher/observable)

## VS Mediator

VS [Mediator](javascript-design-pattern-mediator.md#vs-observer)

- inheritance relationship
  - subscribers typically inherit from a common interface or base class
  - components not required to implement a common interface
- dependency relationship
  - subscribers do not hold a reference to the publisher
  - in mediator, components and mediator depend on each other

## Components For This Pattern

- [publisher](#publisher), also called subject, event **emitter**, event **manager**
- [subscriber interface](#subscriber-interface), also **observer**, **listener**
- [concrete subscriber/observer](#concrete-subscriber)

## Publisher/Observable

- have a method like `notify()` to notify all [subscriber](#subscriber-interface)
  - execute when publisher state changes
  - this method should call its `update()` method for [each subscriber](#concrete-subscriber)
- hold a **list** of [subscriber](#subscriber-interface) in the publisher class
- provide a way to add or remove observer
- have method to manage subscribers
  - `subscribe()`: add subscriber
  - `unsubscribe()`: remove subscriber
  - `mainBusinessLogic()`: main business logic

## Subscriber Interface

- An interface in most case consists of a single method like `update()`
- observer or Concrete subscriber should implement the this interface
- So that publisher communicates with observer

```ts
interface subscriber {
  update(data?: any): any;
}
```

## Concrete Subscriber/Observer

- implement `update()` method to perform a action when notified by [publisher](#publisher)

## Code

publisher

- actually `EventEmitter` is a wrapper for publisher
- it holds a fields reference to `publisher`
- and finish busniess logic with method

```ts
class EventManager {
  private listeners: { [key: string]: Subscriber[] } = {};

  subscribe(eventType: string, listener: Subscriber): void {
    if (!this.listeners[eventType]) {
      this.listeners[eventType] = [];
    }
    this.listeners[eventType].push(listener);
  }

  unsubscribe(eventType: string, listener: Subscriber): void {
    const listeners = this.listeners[eventType];
    if (listeners) {
      this.listeners[eventType] = listeners.filter(l => l !== listener);
    }
  }

  notify(eventType: string, data: any): void {
    const listeners = this.listeners[eventType];
    if (listeners) {
      listeners.forEach(listener => listener.update(data));
    }
  }
}
class EventEmitter {
  public events: EventManager = new EventManager();
  private data: string;

  constructor(data: any) {
    this.data = data;
  }

  triggerLogBusniess(data: string): void {
    this.data = data
    this.events.notify("log", this.data);
  }
  triggerSendBusniess(data: string): void {
    this.data = data;
    this.events.notify("send", this.data);
  }
}
```

subscriber

```ts
interface Subscriber {
  update(message: string): void
}
class LoggingSubscriber implements Subscriber {
  update(message: string): void {
    console.log(`log message: ${message}`);
  }
}
class EmailSubscriber implements Subscriber {
  update(message: string): void {
    console.log(`send email: ${message}`);
  }
}
```

index.ts

```ts
const eventEmitter = new EventEmitter("message");

const logger = new LoggingSubscriber();
eventEmitter.events.subscribe("log", logger);

const email = new EmailAlertsSubscriber();
eventEmitter.events.subscribe("send", email);

// emit event to log subscriber
eventEmitter.triggerLogBusniess("time");
// emit event to email subscriber
eventEmitter.triggerSendBusniess("message")
```


