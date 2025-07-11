# Design Patterns - Composite

## Feature

- kind of structural pattern

## When To Use

- GUI framework

## Structure of Composite Pattern

- [Component](#component)
- [Leaf](#leaf)
- [Composite](#composite)

## Component

- Common **interface** or **abstract class** for **[Leaf](#leaf) and [Composite](#composite)**
- Define the behavior that **BOTH [leaf](#leaf) AND [composite](#composite)** should implement

## Leaf

- Object represent an individual object
- Do not have any child

## Composite

- Hold a collection of child components
- implement the behavior defined by [component](#component) by delegating the operations to its child objects
  - usually contains a **traverse** and **recursive** operation

## Code

significant difference between composite and leaf

- ① : collection of child
- ② : method to aggregate the net price of all child

```ts
// component
interface Equipment {
  getName(): string;
  setName(name: string): void;
  getNetPrice(): number;
  setNetPrice(netPrice: number): void;
  add(equipment: Equipment): void
  remove(equipment: Equipment): void;
}

// Composite
class CompositeEquipment implements Equipment {
  private name: string;
  private netPrice: number;
  private equipment: Equipment[]; // ①

  constructor(name: string) {
    this.name = name;
    this.netPrice = 0;
    this.equipment = [];
  }
  getName(): string{
    return this.name;
  }

  setName(name: string): void {
    this.name = name;
  }
  // ②
  getNetPrice(): number {
    let total = this.netPrice;
    for (const equipment of this.equipment) {
      total += equipment.getNetPrice();
    }
    return total;
  }
  setNetPrice(netPrice: number): void{
    this.netPrice = netPrice;
  }
  add(equipment: Equipment): void {
    this.equipment.push(equipment);
  }
  remove(equipment: Equipment): void {
    const index = this.equipment.indexOf(equipment);
    if (index !== -1) {
      this.equipment.splice(index, 1);
    }
  }
}

// leaf
class FloppyDisk implements Equipment {
  private name: string;
  private netPrice: number;
  constructor(name: string) {
    this.name = name;
    this.netPrice = 0;
  }
  getName(): string {
    return this.name;
  }
  setName(name: string): void  {
    this.name = name;
  }
  getNetPrice(): number {
    return this.netPrice;
  }
  setNetPrice(netPrice: number): void {
    this.netPrice = netPrice;

  }

  add(equipment: Equipment): void {
    throw new Error("FloppyDist does not support add operation.");
  }

  remove(equipment: Equipment): void {
    throw new Error("FloppyDisk does not support remove operation");
  }

}

class Chassis extends CompositeEquipment {
  constructor(name: string) {
    super(name);
  }
}

const fd1: Equipment = new FloppyDisk("3.5 in Floppy");
fd1.setNetPrice(19.99);
console.log(`${fd1.getName()}: netPrice=${fd1.getNetPrice()}`);

const fd2: Equipment = new FloppyDisk("5.25 in Floppy");
fd2.setNetPrice(29.99);
console.log(`${fd2.getName()}: netPrice=${fd2.getNetPrice()}`);

const ch: Equipment = new Chassis("PC Chassis");
ch.setNetPrice(39.99);
ch.add(fd1);
ch.add(fd2);
console.log(`${ch.getName()}: netPrice=${ch.getNetPrice()}`);
```

## Code II

```ts
abstract class FileSystemComponent {
    protected name: string;
 
    constructor(name: string) {
        this.name = name;
    }
 
    abstract print(): void;
}

class File extends FileSystemComponent {
    constructor(name: string) {
        super(name);
    }
 
    print(): void {
        console.log(`File: ${this.name}`);
    }
}

class Folder extends FileSystemComponent {
    private components: FileSystemComponent[] = [];
  
    constructor(name: string) {
        super(name);
    }
 
    add(component: FileSystemComponent): void {
        this.components.push(component);
    }
 
    print(): void {
        console.log(`Folder: ${this.name}`);
        this.components.forEach((component) => {
            component.print();
        });
    }
}

let folder = new Folder('folder');
let file1 = new File('File1');
let file2 = new File('File2');

folder.add(file1);
folder.add(file2);

let subfolder = new Folder('subfolder');
let file3 = new File('File3');

subfolder.add(file3);
folder.add(subfolder);
folder.print();
```

result

```sh
Folder: folder
File: File1
File: File2
Folder: subfolder
File: File3
```
