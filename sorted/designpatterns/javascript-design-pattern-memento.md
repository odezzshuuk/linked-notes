# Javascript Design Pattern - Memento

## Feature

- kind of behavioral pattern

## What problem to solve

- undo/redo
- checkpoint

## Structure of memento pattern

- Originator
- Memento
- Caretaker

## Originator

- An object that going to do some action
- Holding a reference to the [memento](#memento) object represent current state

> for minimal memento pattern structure, Originator only nedd to have one field reference to [memento](#memento) object

- provide methods to
  - create [memento](#memento) object as current state
  - restore given from [memento](#memento) set to state

## Memento

- Holding the state that want to be remembered
- Provide methods for states, like:
  - `getState()`
  - `setState()`

## Caretaker


- hold a list or stack of memento objects, managing [memento](#memento) object
- hold a reference to the [originator](#originator) object
- provide methods for storing and retrieving object

> ~~Is optional, this task can be replace by client code~~

## Code

```ts
class Memento  {
  private state: string;
  private date: string;

  constructor(state: string) {
    this.state = state;
    this.date = new Date().toISOString().slice(0, 19).replace('T', ' ');
  }

  public getState(): string {
    return this.state;
  }

  public getName(): string {
    return `${this.date} / (${this.state.substr(0, 9)}...)`
  }

  public getDate(): string {
    return this.date;
  }

};

class Originator {
  private state: string;

  constructor(state: string) {
    this.state = state;
  }

  public doSomething(): void {
    this.state = this.generateRandomString(30);
  }

  private generateRandomString(length: number = 10): string {
    const charSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    return Array(length)
      .fill(null)
      .map(() => charSet.charAt(Math.floor(Math.random() * charSet.length)))
      .join('');
  }

  public save(): Memento {
    return new Memento(this.state);
  }

  public restore(memento: Memento): void {
    this.state = memento.getState();
    console.log(`Originator: My state has changed to: ${this.state}`);
  }
};

class Caretaker {
  private mementos: Memento[] = [];
  private originator: Originator;

  constructor(originator: Originator) {
    this.originator = originator;
  }

  public backup(): void {
    console.log('\nCaretaker: Saving Originator\'s state...')
    this.mementos.push(this.originator.save());
  }

  public undo(): void {
    if (!this.mementos.length) {
      return;
    }
    const memento = this.mementos.pop();
    console.log(`Caretaker: Restoring state to: ${memento?.getName()}`);
    if (memento) {
      this.originator.restore(memento);
    }
  }

  public showHistory(): void {
    console.log('Caretaker: Here\'s the list of mementos: ');
    for (const memento of this.mementos) {
      console.log(memento.getName());
    }
  }
};

const originator = new Originator('Super-duper-super-puper-super.')
const caretaker = new Caretaker(originator);

caretaker.backup();
originator.doSomething();

caretaker.backup();
originator.doSomething();

caretaker.backup();
originator.doSomething();

console.log('');
caretaker.showHistory();

console.log('\nClient: Now, let\'s rollback!\n');
caretaker.undo();

console.log('\nClient: Undo Once more!\n');
caretaker.undo();
```

