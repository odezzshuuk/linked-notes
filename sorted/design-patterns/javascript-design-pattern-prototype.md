# Javascript Design Pattern - Prototype

## Feature

- kind of creational pattern

## When To Use

- create complex object conveniently
- create object dynamically

## Structure of Prototype Pattern

- prototype

## Prototype

- declares the cloning methods, mostly `clone()`
- in `clone()` method, you should
  - create a new object
  - perform a [deep copy](javascript-deep-copy.md)

## Code

```ts
// prototype
class Shape {
  protected type: string;
  constructor() {
    this.type = '';
  }
  getDescription(): string {
    return this.type;
  }
  clone(): Shape {
    const clone = Object.create(Object.getPrototypeOf(this));
    Object.assign(clone, this);
    return clone;
  }
}
class Circle extends Shape {
  constructor() {
    super();
    this.type = 'Circle'
  }
}
class Square extends Shape {
  constructor() {
    super();
    this.type = 'Square';
  }
}

const originalCircle = new Circle();
const clonedCircle = originalCircle.clone();

const originalSquare = new Square();
const cloneSquare = originalSquare.clone();

console.log(originalCircle.getDescription());
console.log(clonedCircle.getDescription());

console.log(originalSquare.getDescription());
console.log(cloneSquare.getDescription());
```