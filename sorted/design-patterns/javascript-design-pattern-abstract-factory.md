# Javascript Design Pattern - Abstract Factory

## Feature

- A creational pattern
- Use to Create **object family**

## VS Factory Design Pattern

- Factory Design Pattern: focus on creating single type product

## Structure of Abstract Factory Pattern

- Abstract Factory
- Concrete Factory
- Abstract Product
- Concrete Product

## Code

```ts
interface CarModel {
  assemble(): void;
}

class Sedan implements CarModel {
  assemble(): void {
    console.log("Assembling Sedan car model");
  }
}

class SUV implements CarModel {
  assemble(): void {
    console.log("Assembling SUV car model");
  }
}

interface CarPart {
  install(): void;
}

class Tires implements CarPart {
  install(): void {
    console.log("Installing car tires");
  }
}

class Engine implements CarPart {
  install(): void {
    console.log("Installing car engine");
  }
}
interface CarFactory {
  createCarModel(): CarModel;
  createCarPart(): CarPart;
}

class SedanFactory implements CarFactory {
  createCarModel(): CarModel {
    return new Sedan();
  }
  createCarPart(): CarPart {
    return new Engine();
  }
}

class SUVFactory implements CarFactory {
  createCarModel(): CarModel {
    return new SUV();
  }
  createCarPart(): CarPart {
    return new Tires();
  }
}

function assembleCar(factory: CarFactory): void {
  const carModel = factory.createCarModel();
  const carPart = factory.createCarPart();

  carModel.assemble();
  carPart.install();
}

console.log("Client orders Sedan car: ");
const sedanFactory = new SedanFactory();
assembleCar(sedanFactory);
console.log("Client orders SUV car: ");
const suvFactory = new SUVFactory();
assembleCar(suvFactory);
```
