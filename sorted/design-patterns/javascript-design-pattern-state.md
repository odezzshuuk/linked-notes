# TypeScript Design Patterns - State

* [Feature](#feature)
* [What Problem To Solve](#what-problem-to-solve)
* [Class Consist of State Pattern](#class-consist-of-state-pattern)
* [Context](#context)
* [state interface](#state-interface)
* [concrete states](#concrete-states)
* [code](#code)

## Feature

- kind of behavioral pattern
- similar structure
  - [strategy](javascript-design-pattern-strategy.md)

## What Problem To Solve

- More and more state make the code hard to maintain
- Most method will contain monstrous conditions

## Class Consist of State Pattern

- [context](#context)
- [state interface](#state-interface)
- [concrete states](#concrete-states)

## Context

1. Holding a fields reference to the [state object](#concrete-states)
2. One or more methods that change the state

```js
class Context {
  // 1. state field
  private state: State;
  // 2. changing state method
  methodToChangeState() {
    this.state = new ConcreteState();
  }
}
```

## State Interface

- declare all the methods that the context can call to change state

```ts
interface State {
  changeToA(): void;
  changeToB(): void;
}
```

## Concrete States

- Providing their own implementations for the state-specific method

> may provide intermediate abstract class for duplicate code

- State object store a backreference to the [context object](#context)
- For fetch required info from [context object](#context)

## Code

state interface

```ts
abstract class State {
  abstract pullUp(wrapper?: Chain): void;
  abstract pullDown(wrapper?: Chain): void;
}
```

concrete state

```ts
class Off extends State {
  pullUp(wrapper?: Chain) {
    wrapper?.setState(new Low());
    console.log(' low speed');
  }
  pullDown() {
    console.log(' already off');
  }
}

class Low extends State {
  pullUp(wrapper?: Chain) {
    wrapper?.setState(new Medium());
    console.log(' medium speed');
  }
  pullDown(wrapper?: Chain) {
    wrapper?.setState(new Off());
    console.log(' turning off');
  }
}

class Medium extends State {
  pullUp(wrapper?: Chain) {
    wrapper?.setState(new High());
    console.log(' high speed');
  }
  pullDown(wrapper?: Chain) {
    wrapper?.setState(new Low());
    console.log(' low speed');
  }
}

class High extends State {
  pullUp(wrapper?: Chain) {
    console.log(' already the highest');
  }
  pullDown(wrapper?: Chain) {
    wrapper?.setState(new Medium());
    console.log(' medium speed');
  }
}
```

context

- `Chain.ts`

```ts
class Chain {
  private current: State;
  constuctor() {
    this.current = new Off();
  }
  setState(state: State) {
    this.current = state;
  }
  pullUp() {
    this.current.pullUp(this);
  }
  pullDown() {
    this.current.pullDown(this);
  }
}
```

index.ts

```ts
const chain = new Chain();
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})
function switchState() {
  rl.question('any key to continue(\'q\' to exit)', (input) => {
    if (input === 'q') {
      rl.close();
    } else if (input === 'up') {
      chain.pullUp();
      switchState();
    } else if (input === 'down') {
      chain.pullDown();
      switchState();
    } else {
      console.error('invalid input')
      switchState();
    }
  })
}
switchState();
```
