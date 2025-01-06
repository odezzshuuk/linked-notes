# Design Pattern - Event Listener

## Class

- `Event`: most simple event is a string, but can be any type
- `Listener/EventHandler`:
  - a function registered to be called when an event is emitted
- `Emitter`
  - emit events
  - also register listeners

nodejs provides built-in class [`EventEmitter`]

## Minimal Code 

```ts
type EventHandler = (...args: any[]) => void;

class EventEmitter {
  private events: Record<string, EventHandler[]> = {};

  on(event: string, listener: EventHandler): void {
    if (!this.events[event]) {
      this.events[event] = [];
    }
    this.events[event].push(listener);
  }

  emit(event: string, ...args: any[]): void {
    const listeners = this.events[event];
    if (listeners) {
      for (const listener of listeners) {
        listener(...args);
      }
    }
  }

  off(event: string, listener: EventHandler): void {
    const listeners = this.events[event];
    if (listeners) {
      this.events[event] = listeners.filter((l) => l !== listener);
    }
  }
}

// Example usage:
const eventEmitter = new EventEmitter();

// Listener 1
const listener1: EventHandler = (data: string) => {
  console.log(`Listener 1: ${data}`);
};

// Listener 2
const listener2: EventHandler = (data: string) => {
  console.log(`Listener 2: ${data}`);
};

// Register listeners
eventEmitter.on('exampleEvent', listener1);
eventEmitter.on('exampleEvent', listener2);

// Emit event
eventEmitter.emit('exampleEvent', 'Hello, world!');

// Unregister a listener
eventEmitter.off('exampleEvent', listener1);

// Emit event again, only listener2 should be triggered
eventEmitter.emit('exampleEvent', 'Hello, again!');
```
