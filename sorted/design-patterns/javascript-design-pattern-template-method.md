# Javascript Design Patterns - Template Method

## What It Is

- A Behavioral Pattern

## What problem to solve

**Problem**

- this first version the app could work only with DOC file
- the following version, it was able to support CSV files
- A month later, it needs to support PDF files
- In summary
  - when you have a business with a series of steps
  - basic steps remain the same
  - some steps have variations depending on the context

**Solution**

- defining the basic steps of an algorithm in a place
- and allowing the individual steps have their own implementation in subclass

## Structure of Template Method Pattern

class for template method pattern is **simple**

- just base abstract class and its concrete class

## Methods in the Base class

how to implement the template method is the **critical part**

- usually one method to run the steps method in order, maybe name as
  - `run()`
  - `runSteps()`
  - `turn()`
- **abstract steps** must be implemented
- **optional steps** have default impletation
- **Empty body methods** called hooks

## code

base class

- `GameAI.ts`

```ts
abstract class GameAI {
  public turn() {
    this.collectResources();
    this.buildStructures();
    this.buildUnits();
    this.attack();
  }

  public collectResources() {
    console.log("collecting resources");
  }
  public buildUnit() {
    console.log('Building units')
  }
  public attact() {
    console.log('Attacking');
  }
  protected abstract buildStructures();
}
```

Concrete Class

```ts
class OrcsAI extends GameAI {
  public buildStructures() {
    console.log('Building Orc structures');
  }
}
class MonstersAI extends GameAI {
  public buildStructures() {
    console.log('Building monster structures');
  }

  public collectResources() {
    console.log('Monsters do not collect resources');
  }

  public buildUnits() {
    console.log('Monsters do not build units');
  }
}
```

Client

- `index.ts`

```ts
const orcAI = new OrcsAI();
orcAI.turn();

const monsterAI = new MonstersAI();
monsterAI.turn();
```
