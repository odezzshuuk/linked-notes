# Javascript Design Patterns - Facade

## Feature

- A Structural Pattern
- IN SUMMARY, provide simplified interface to a complex subsystem

> subsystem may have many class

- Act as a **middle layer** between the client and subsystems
- Not recommend to encapsulate multiple **unrelated** subsystems into a single class

## What problem to solve

- When a subsystem is complex, it is hard to use
- Managing complex subsystems by providing a simple and unified interface

## Real Case Of Facade Use Case

- Operation System
- Modern Car Dashboard

## Structure of Facade Pattern

- [Facade](#facade)
- [Subsystem Classes](#subsystem-classes)

## Facade

- Hold the fields reference to subsystem class that facade need to use
- Relationship between facade and subsystem class is [**has-a**](uml.md#line-association) relationship
- It is not necessary to receive subsystem class instance in facade constructor

## Subsystem Classes

- Classes used by facade

## Code

```ts
// Subsystem class
class Engine {
  start() {
    console.log('Engine started');
  }
  stop() { /*...*/ }
  increasePower() { /*...*/ }
  decreasePower() { /*...*/ }
}

// Subsystem class
class Headlights {
  turnOn() {
    console.log('Headlights turned on');
  }
  turnOff() { /*...*/ }
}

// Subsystem class
class FuelSystem {
  injectFuel() {
    console.log('Music player started playing');
  }
  ejectFuel() { /* ... */ }
}

// Subsystem class
class Battery {
  charge() {
    console.log('Charging battery ...');
  }
  getStatus() { /* ... */ }
  getChargeLevel() { /* ... */ }
}

// Facade
class CarFacade {
  private engine: Engine;
  private headlights: Headlights;
  private fuelSystem: FuelSystem;
  private battery: Battery;

  constructor() {
    this.engine = new Engine();
    this.headlights = new Headlights();
    this.fuelSystem = new FuelSystem();
    this.battery = new Battery();
  }

  start() {
    this.battery.charge();
    this.engine.start();
    this.headlights.turnOn();
    this.fuelSystem.injectFuel();
  }
  stop() {
    console.log('Stopping car ...');
    this.fuelSystem.ejectFuel();
    this.engine.stop();
  }
}

// Client code
const carFacade = new CarFacade();
carFacade.start();
carFacade.stop();
```
