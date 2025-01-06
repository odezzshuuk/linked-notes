# Javascript Design Patterns - Factory Method

## Feature

- A creational pattern
- For creating object according to different request

## When To Use

- object creation logic becomes too convoluted
- decouple the client code and the concrete class
- when application need to create different objects with common interface
- even if there only one type product, it is still recommended to use factory pattern for future extend requirement

## Structure of Factory Pattern

factory structure is normal, just factory and product

- Factory Interface And Concrete Factory
- Product Interface And Concrete Product

factory method

- always receive one or more parameters

## Code

```ts
// product interface
interface Car {
  start(): void;
  stop(): void;
}

// concrete product
class Sedan implements Car {
  start() {
    console.log('Starting Seda ...');
  }

  stop() {
    console.log('Stopping Sedan...')
  }
}
class SUV implements Car {
  start() {
    console.log('Starting SUV ...');
  }

  stop() {
    console.log('Stopping SUV ...');
  }
}

// base factory
class CarFactory {
  createCar(type: string): Car {
    if (type === 'Sedan') {
      return new Sedan();
    } else if (type === 'SUV') {
      return new SUV();
    } else {
      throw new Error('Invalid car type!');

    }
  }
}

// client
const factory = new CarFactory();

const mySedan = factory.createCar('Sedan');
mySedan.start();
mySedan.stop();

const mySUV = factory.createCar('SUV');
mySUV.start();
mySUV.stop();
```
