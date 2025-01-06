# Javascript Design Patterns - Mediator

## Feature

- kind of behavioral pattern

## VS Observer

vs [Observer](javascript-design-pattern-observer.md#vs-mediator)

- mediator: many to many
- observer: one to many

## What Problem To Solve

- useful when objects need to interact with many other object

## Structure of Mediator

- [mediator interface](#mediator)
- [concrete mediator](#concrete-mediator)
- [components ](#components), also called colleague

## mediator

- typically declare a single  `notify()` method to notify [component]
  - methods should receive component andt event type as arguments

```ts
interface Mediator {
  notify(sender: object, event: string): void;
}
```

## Concrete Mediator

- usually hold reference to **all** related component
- usually pass components through constructor

```ts
class MediatorA {
  constructor(c1: Component1, c2: Component2) { }
}
```

## Components

- **not required to inherit** from a common interface or base class
- must have a reference to a [mediator](#mediator) object
- use the mediator `notify()` method to communicate with other components

## Code

```ts
// mediator interface
interface Mediator {
  notify(sender: object, event: string): void;
}

// components
class ConcreteMediator implements Mediator {
  private component1: Component1;

  private component2: Component2;

  constructor(c1: Component1, c2: Component2) {
    this.component1 = c1;
    this.component1.setMediator(this);
    this.component2 = c2;
    this.component2.setMediator(this);
  }

  public notify(sender: object, event: string): void {
    if (event === 'A') {
      console.log('Mediator reacts on A and triggers following operations:');
      this.component2.doC();
    }

    if (event === 'D') {
      console.log('Mediator reacts on D and triggers following operations:');
      this.component1.doB();
      this.component2.doC();
    }
  }
}

// base component but not required
class BaseComponent {
  protected mediator: Mediator;

  constructor(mediator?: Mediator) {
    this.mediator = mediator!;
  }

  public setMediator(mediator: Mediator): void {
    this.mediator = mediator;
  }
}

// concrete components
class Component1 extends BaseComponent {
  public doA(): void {
    console.log('Component 1 does A.');
    this.mediator.notify(this, 'A');
  }

  public doB(): void {
    console.log('Component 1 does B.');
    this.mediator.notify(this, 'B');
  }
}

// concrete components
class Component2 extends BaseComponent {
  public doC(): void {
    console.log('Component 2 does C.');
    this.mediator.notify(this, 'C');
  }

  public doD(): void {
    console.log('Component 2 does D.');
    this.mediator.notify(this, 'D');
  }
}

// client code
const c1 = new Component1();
const c2 = new Component2();
const mediator = new ConcreteMediator(c1, c2);

console.log('Client triggers operation A.');
c1.doA();

console.log('');
console.log('Client triggers operation D.');
c2.doD();
```


