# Javascript Design Pattern - Decorator

## Feature

- kind of structural pattern
- add behavior or functionality to object **dynamically**

dynamically create like this

```ts
const coffee = new Coffee();
coffee = new Milk(coffee);
coffee = new Whip(coffee);
```

## What Problem to Solve

- create different type of coffee like "espresso", "latte", "cappuccino", etc
- then add different condiments like "milk", "soy", "mocha", "whip", etc
- if we use subclass we have to create subclasses for each combination

## Structure of Decorator Pattern

- [Component](#component)
- [Concrete Component](#concrete-component)
- [Base Decorator](#base-decorator)
- [Concrete Decorator](#concrete-decorator)

## Component

- abstract class or interface defined common methods

## Concrete Component

- implements the component and define base behavior
- object to be wrapped

## Base Decorator

- hold a field reference to [concrete component](#concrete-component)
- always [aggregate](/sorted/UML/uml.md#clear-diamond-aggregation) a [concrete component](#concrete-component)
- inherit from [component](#component)
- not necessary, but recommend

## Concrete Decorator

- define extra behavior that can be added to [concrete component](#concrete-component) dynamically

## Code

```ts
// base component
interface Coffee {
  getCost(): number;
  getDescription(): string;
}

// concrete component
class SimpleCoffee implements Coffee {
  getCost() {
    return 1;
  }

  getDescription() {
    return "Simple coffee";
  }
}

// base decorator
abstract class CoffeeDecorator implements Coffee {
  coffee: Coffee;

  constructor(coffee: Coffee) {
    this.coffee = coffee;
  }

  getCost(): number {
    return this.coffee.getCost();
  };

  getDescription(): string {
    return this.coffee.getDescription();
  };
}

// Concrete decorator
class MilkDecorator implements CoffeeDecorator {
  coffee: Coffee;

  constructor(coffee: Coffee) {
    this.coffee = coffee;
  }

  getCost() {
    return this.coffee.getCost() + 0.5;
  }

  getDescription() {
    return `${this.coffee.getDescription()}, milk`;
  }
}

// concrete decorator
class SugarDecorator implements CoffeeDecorator {
  coffee: Coffee;

  constructor(coffee: Coffee) {
    this.coffee = coffee;
  }

  getCost() {
    return this.coffee.getCost() + 0.3;
  }

  getDescription() {
    return `${this.coffee.getDescription()}, sugar`;
  }
}

// Create a simple coffee and wrap it with decorators
let myCoffee: Coffee = new SimpleCoffee();
myCoffee = new MilkDecorator(myCoffee);
myCoffee = new SugarDecorator(myCoffee);

// Print the description and cost of the decorated coffee
console.log(myCoffee.getDescription()); // Simple coffee, milk, sugar
console.log(myCoffee.getCost()); // 1.8
```