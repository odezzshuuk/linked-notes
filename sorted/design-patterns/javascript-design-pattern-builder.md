# Javascript Design Pattern - Builder

* [What It Is](#what-it-is)
* [What kind of Problem to Solve](#what-kind-of-problem-to-solve)
* [Components of this pattern](#components-of-this-pattern)
* [Product](#product)
* [Builder](#builder)
* [ConcreteBuilder](#concretebuilder)
* [Director](#director)
* [Code](#code)

## What It Is

- kind of creational pattern
- **In summary, extract the construction to a separate object**

## What kind of Problem to Solve

**Problem**: for build plenty kinds of houses

```java
class Pizza {
    Pizza(int size) { /* ... */ }
    Pizza(int size, boolean cheese) { /* ... */ }
    Pizza(int size, boolean cheese, boolean pepperoni) { /* ... */ }
    // ...
}
```

- you can create plenty of subclasses for `House` class
- or create a gaint constructor, like `House(windows, doors, rooms, hasGarage, hasSwimPool, hasStatues, hasGarden,...)`
  - in most cases most of the parameters are not used

**Solution**: extract the construction to a separate object

## Components of this pattern

basic components

- [Product](#product)
- [Builder](#builder)

further need component

- [ConcreteBuilder](#Concretebuilder)
- [Director](#director)

## Product

- the object to be created
- usually represent something from the real world

## Builder

- interface for creating products
- or builder class if no [concreteBuilder](#concretebuilder) is needed
- with methods like
  - `reset()`
  - `setSeats(num: number)`
  - `setEngine(name: string)`
  - `setTripComputer(flag: boolean)`
  - `setGPS(flag: boolean)`
  - ...
- if no [concreteBuilder](#concretebuilder), a method like `getProduct()` to return the product

## ConcreteBuilder

- hold a fields reference to the [product](#product)
- implement the [builder](#builder) interface
- with a method like `getProduct()` return the [product](#product)

## Director

- not strictly necessary
- can be use to
  - provide some predefined configuration
  - sometimes define the order of construction

## Code

[product](#product)

- car.ts

```js
class car {
  seats: number;
  engine: string;
  tripComputer: boolean;
  GPS: boolean;
  //...
}
```

[builder](#builder): builder interface

- `builder.ts`

```ts
interface Builder {
  reset(): void;
  setSeats(num: number): void;
  setEngine(name: string): void;
  setTripComputer(flag: boolean): void;
  setGPS(flag: boolean): void;
}
```

[concrete builder](#concretebuilder)

- `carBuilder.ts`

```ts
class CarBuilder implements Builder {
  private car: Car;
  constructor() {
    this.reset();
  }
  reset(): void { this.car = new Car(); }
  setSeats(num: number): void { this.car.seats = num; }
  setGPS(flag: boolean): void { this.car.GPS = true; }
}
```

- `carManualBuilder.ts`

```ts
class CarManualBuilder implements Builder {
  private manual: Manual;
  CarManulaNuilder() {
    this.reset();
  }

  reset(): void { this.manual = new Manual(); }
  setSeats(num: number): void { /* ... */ }
  setEngine(name: string): void { /* ... */ }
  setTripComputer(flag: boolean) { /* ... */  }
  setGPS(flag: true): void { /* ... */  }
  getProduct(): Manual { return this.manual; }
}
```

or use [director](#director)

- `director.ts`

```ts
class Director {
  constructSportCar(builder: Builder): void {
    builder.reset();
    builder.setSeats(2);
    builder.setEngine('sport');
    builder.setTripComputer(true);
    builder.setGPS(true);
  }

  constructSUV(builder: Builder): void {
    builder.reset();
    builder.setSeats(4);
    builder.setEngine('suv');
    builder.setTripComputer(true);
    builder.setGPS(true);
  }
}
```

client: code to use pattern

- `index.ts`

```ts
// director
const director = new Director();

// builder to product
const carBuilder = new CarBuilder();
director.constructSportsCar(carBuilder);
const car = carBuilder.getProduct();

// builder to product
const carManualBuilder = new CarManualBuilder();
director.constructSportsCar(carManualBuilder);
const manual = carManualBuilder.getProduct();
```
