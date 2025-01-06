# Javascript Design Patterns - Adapter

* [Feature](#feature)
* [What problem to Solve](#what-problem-to-solve)
* [structure of adapter pattern](#structure-of-adapter-pattern)
* [Target](#target)
* [Adaptee](#adaptee)
* [Adapter](#adapter)
* [Client](#client)
* [Code](#code)

## Features

- kind of structural pattern
- Allows object with different interfaces to collaborate

## What problem to Solve

IN SUMMARY, Solve the problem of **incompatible** problem, for example

- Here is an example shows the incompatible **method name** between client and target
- While other incompatible problems also reference to
  - method parameter
  - method return type
  - ...

```ts
class Adaptee{
  getFoo(): number {
    // ...
  }
}
class Target{
  getBar(): number {

  }
}
class Adapter extends Target {
  private adaptee: Adaptee;
  constructor(adaptee: Adaptee) {
    this.adaptee = adaptee;
  }
  getBar(): number {
    // re-implement getBar() logic
    return getFoo();
  }
}
// client code
// ...
```

In above code demo

- CLIENT try to call `getBar()` method in ADAPTEE
- But CLIENT can't call directly
- Use ADAPTER wrap the Adaptee And inherit the TARGET
- Re-implement the client-compatible method use TARGET
- CLIENT use ADAPTER's method to run business logic

## structure of adapter pattern

basic structure

- [Target](#target)
- [Client](#client)
- [Adaptee](#adaptee)
- [Adapter](#adapter)

## Target

- An object that [Client](#client) work with
- An object that [Adapter](#adapter) need to inherit from it

## Adaptee

- An object that wrapped by [adapter](#adapter)
- have method that [client](#client) want to use but not compatible

## Adapter

- Client use [Adapter](#adapter) instead of [Target](#target)
- hold a fields reference to [adaptee](#adaptee)

how to implement a Aapter

1. Inherit [target](#target) class or interface
2. re-implement the [target](#target) method that [client] want work with use [adaptee] method

- IN SUMMARY, [Adapter](#adapter) should
    - inherit [target](#target) class
    - wrap a [adaptee](#adaptee) instance
    - re-implement target's method use adaptee's method

## Client

- have business logic that
  - Work with [target](#target)
  - But not compatible with [adaptee](#target)

## Code

```ts
// client have business logic
class RoundHole {
  private radius: number;
  constructor(radius: number) {
    this.radius = radius;
  }
  public getRadius(): number {
    return this.radius;
  }
  public fits(peg: RoundPeg) {
    return this.getRadius() >= peg.getRadius();
  }
}

// target that client work with
class RoundPeg {
  private radius: number;
  constructor(radius: number) {
    this.radius = radius;
  }
  public getRadius(): number {
    return this.radius;
  }
}

// adaptee with incompatible interface
class SquarePeg {
  private width: number;
  constructor(width: number) {
    this.width = width;
  }
  public getWidth(): number {
    return this.width;
  }
}

// adapter
class SquarePegAdapter extends RoundPeg {
  private peg: SquarePeg;

  constructor(peg: SquarePeg) {
    super(0);
    this.peg = peg;
  }
  public getRadius(): number {
    return this.peg.getWidth() * Math.sqrt(2) / 2;
  }
}

// client code
const hole = new RoundHole(5);
const rpeg = new RoundPeg(5);
console.log(hole.fits(rpeg));

const smallSqpeg = new SquarePeg(5);
const largeSqpeg = new SquarePeg(10);
console.log(hole.fits(smallSqpeg));  // use target directly, incompatible error

const smallSqpegAdapter = new SquarePegAdapter(smallSqpeg);
const largeSqpegAdapter = new SquarePegAdapter(largeSqpeg);
console.log(hole.fits(smallSqpegAdapter))
console.log(hole.fits(largeSqpegAdapter));
```
