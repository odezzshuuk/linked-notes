# Javascript Design Patterns - Iterator

## What It Is

- kind of behavioral pattern

## What problem to solve

- To separate the **data structure** from the traverse **algorithm**

## Structure of Iterator Pattern

- [Iterator interface](#iterator-interface)
- [Concrete Iterator](#concrete-iterator)
- [Aggregate Interface](#aggregate-interface)
- [Concrete Aggregate](#concrete-aggregate), also called **collection**

## Iterator Interface

- declare the traverse methods, name like:
  - `current()`
  - `next()`
  - `key()`

## Concrete Iterator

- hold a field reference to the [aggregate object](#concrete-aggregate)
- hold a field to store the current traversal position
- implement the methods in [iterator interface](#iterator-interface)
- how to implement the Iterator is depending on the which **data structure** about to traverse

## Aggregate Ineterface

- one or multiple methods for getting iterators

## Concrete Aggregate

- always hold a field to store the data
- iterator getting method should return the [corresponding iterator](#concrete-iterator)

## Code

```ts
// Iterator interface
interface IIterator<T> {
  current(): T;
  next(): T;
  key(): number;
  valid(): boolean;
  rewind(): void;
}

// Aggregator interface
interface Aggregator {
  getIterator(): IIterator<string>;
}

class AlphabeticalOrderIterator implements IIterator<string> {
  private collection: WordsCollection;
  private position: number = 0;
  private reverse: boolean = false;
  constructor(collection: WordsCollection, reverse: boolean = false) {
    this.collection = collection;
    this.reverse = reverse;
    if (reverse) {
      this.position = collection.getCount() - 1;
    }
  }
  public rewind() {
    this.position = this.reverse ? this.collection.getCount() - 1 : 0;
  }
  public current(): string {
    return this.collection.getItems()[this.position];
  }
  public key(): number {
    return this.position;
  }
  public next(): string {
    const item = this.collection.getItems()[this.position];
    this.position += this.reverse ? -1 : 1;
    return item;
  }
  public valid(): boolean {
    if (this.reverse) {
      return this.position >= 0;
    }
    return this.position < this.collection.getCount();
  }
}
class WordsCollection implements Aggregator {
  private items: string[] = [];
  public getItems(): string[] {
    return this.items;
  }
  public pgetCount() : number {
    return this.items.length;
  }
  public addItem(item: string) {
    this.items.push(item);
  }
  public getIterator(): IIterator<string> {
    return new AlphabeticalOrderIterator(this);
  }
  public getReverseIterator(): IIterator<string> {
    return new AlphabeticalOrderIterator(this, true);
  }
}

const collection = new WordsCollection();
collection.additem('First');
collection.additem('Second');
collection.addItem('Third');

const IItreator = collection.getIterator();
console.log('Straight traversal: ');
while (IIiterator.valid()) {
  console.log(IITreator.next());
}
console.log('');
console.log('Reverse traversal: ');
const reverseiterator = collection.getReverseIterator();
while (reverseIterator.valid()) {
  console.log(reverseIterator.next());
}
```




