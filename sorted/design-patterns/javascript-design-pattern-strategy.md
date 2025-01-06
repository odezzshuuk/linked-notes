# Javascript Design Patterns - Strategy

## Feature

- A behavioral pattern
- Define a series of algorithms
- have the similar structures with
  - [state](javascript-design-pattern-state.md)
  - [bridge]

VS [state](javascript-design-pattern-state.md)

## When To Use Strategy Pattern

- when there are multiple algorithms for a specific task
- In behavior-interchangeable system

## Consist of Strategy Pattern

- [context](#context)
- [strategy inteface](#strategy-interface)
- [concrete strategy](#concrete-strategy)

## Context

1. Hold a fields reference to the [strategy object](#concrete-strategy)
2. A method to set the strategy
3. A method to use the strategy

```ts
class Context {
  private strategy: Strategy;
  constructor() {
    this.strategy = new Strategy();
  }
  setStrategy(strategy: Strategy) {
    this.strategy = strategy;
  }
  executeStrategy() {
    this.strategy.execute();
  }
}
```

## Strategy Interface

- declare the method of execute the algorithm

```ts
interface Strategy {
  execute(): void;
}
```

## Concrete Strategy

- implement their own algorithm

## Code

```ts
// context
class Context {
  private strategy: Strategy;
  constructor() {
    this.strategy = new Add();
  }
  setStrategy(strategy: Strategy) {
    this.strategy = strategy;
  }
  executeStrategy(a: number, b: number) {
    return this.strategy.execute(a, b);
  }
}

// strategy interface
interface Strategy {
  execute(a: number, b: number): number;
}
// concrete strategy
class Add implements Strategy {
  execute(a: number, b: number): number {
    return a + b;
  }
}

class Sub implements Strategy {
  execute(a: number, b: number): number {
    return a - b;
  }
}

class Mul implements Strategy {
  execute(a: number, b: number): number {
    return a * b;
  }
}
```

`index.ts`

```ts
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

const context = new Context();

function InputStrategy() {
  rl.question(
    'a=3, b=5 1: +, 2: -, 3: *, q: quit',
    (input: string) => {
      if (input === '1') {
        context.setStrategy(new Add())
      } else if (input === '2') {
        context.setStrategy(new Sub());
      } else if (input === '3') {
        context.setStrategy(new Mul());
      } else if (input === 'q') {
        rl.close();
        return;
      } else {
        console.log('input error')
      }
      const result = context.executeStrategy(3, 5);
      console.log(result);
      InputStrategy();
    })
}

InputStrategy();
```
