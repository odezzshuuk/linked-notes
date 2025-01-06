# Javascript Design Patterns - Flyweight

## Feature

- A structural pattern
- Distinct with other patterns it's not about decouple things
  - it concerned with **memeory optimization**
  - reduce memory usage and improve performance

## When To Use

typically when there is a large number of objects with similar attributes

1. Text Editing
2. Game Development: such as managing particles or spirte

## Structure of Flyweight Pattern

- Flyweight
- Flyweight Factory
- [Context]()

## Flyweight

- contains the state that can be **shared** between objects

## Flyweight Factory

- manage an collection of existing flyweights.
- provide a way to get flyweight

```ts
class FlyWeightFactory {
  private flyweights: { [key: string]: FlyWeight } = {};
  getFlyweight(key: any) {
    if (!this.flyweights[key]) {
      this.flyweights[key] = new FlyWeight(key);
    }
    return this.flyweights[key];
  }
}
```

## Context

- this is optional in a simple flyweight structure
- contains the unique state

## Code

```ts
// flyweight
class Tenant {
  constructor(public name: string) {}
}

// flweweight factory
class Registry {
  private tenants: Map<string, Tenant>;

  constructor() {
    this.tenants = new Map<string, Tenant>();
  }

  findByName(name: string): Tenant {
    if (!this.tenants.has(name)) {
      this.tenants.set(name, new Tenant(name));
    }
    return this.tenants.get(name)!;
  }
}

// unique state in context
class Apartment {
  private occupants: Map<number, Tenant>;
  private registry: Registry;

  constructor() {
    this.occupants = new Map<number, Tenant>();
    this.registry = new Registry();
  }

  addOccupant(name: string, room: number): void {
    const tenant = this.registry.findByName(name);
    this.occupants.set(room, tenant);
  }

  getTenants(): void {
    for (const [room, tenant] of this.occupants.entries()) {
      console.log(`${tenant.name} occupies room ${room}`);
    }
  }
}

const apartment = new Apartment();
apartment.addOccupant("David", 1);
apartment.addOccupant("Sarah", 3);
apartment.addOccupant("George", 2);
apartment.addOccupant("Lisa", 12);
apartment.addOccupant("Michael", 10);
apartment.getTenants();
```
