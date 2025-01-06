# Javascript Design Patterns - Command

* [Feature](#feature)
* [Which Scenario to use](#which-scenario-to-use)
* [Receiver](#receiver)
* [Command](#command)
* [Invoker](#invoker)
* [Example Code](#example-code)

## Feature

- kind of behavioral design pattern
- Encapsulating a request as an object

three components in command pattern

- **Receiver**: the object that executes method on
- **Command**: holds a fields reference to receiver
- **Invoker**: holds a fields ralated to command object

## Which Scenario To Use

- undo/redo
- GUI component
- queuing: execute commands in order
- transactions: used to implement database transactions
- Remote procedure calls

## Receiver

- the target object that [command](#command) executes on
- usually the real object that does actually work
- passed to the command object via constructor

## Command

- sometimes is a **base class** or abstract class for concrete commands
- holds a field reference to the [receiver](#receiver)
- usually has a method called `execute()` to call the receiver's method
- responsible for command encapsulation

## Invoker

- also has a method called `execute()` to call all command's `execute()` method
- holds a fields reference to the [commands](#command) list
- In summary, Invoker is responsible for
  - command execution
  - command management
- optionally has methods
  - `undo()/redo()`
  - `getCommandHistory()`

## Example Code

Create Command Object

```js
class LightCommand {
  constructor(light) {
    this.light = light;
  }

  execute() {
    throw new Error('execute() must be implemented');
  }
}

class TurnOnCommand extends LightCommand {
  execute() {
    this.light.turnOn();
  }
}

class TurnOffCommand extends LightCommand {
  execute() {
    this.light.turnOff();
  }
}
```

- TurnOnCommand and TurnOffCommand are concrete commands

Receiver Object to receive command

```js
class Light {
  turnOn() {
    console.log('Light is on.');
  }

  turnOff() {
    console.log('Light is off.');
  }
}
```

Invoker

```js
// Invoker
class Switch {
  constructor() {
    this.history = [];
  }

  storeAndExecute(command) {
    this.history.push(command);
    command.execute();
  }

  undo() {
    const lastCommand = this.history.pop();
    if (lastCommand) {
      console.log('Undoing last command:');
      lastCommand.execute();
    }
  }
}
```

Programmming

```js
// Client
const light = new Light();
const turnOnCommand = new TurnOnCommand(light);
const turnOffCommand = new TurnOffCommand(light);

const lightSwitch = new Switch();
lightSwitch.storeAndExecute(turnOnCommand); // output: Light is on.
lightSwitch.storeAndExecute(turnOffCommand); // output: Light is off.

lightSwitch.undo(); // output: Undoing last command: Light is off.
lightSwitch.undo(); // output: Undoing last command: Light is on.
```
