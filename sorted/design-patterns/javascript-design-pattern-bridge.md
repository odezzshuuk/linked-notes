# Javascript Design Pattern - Bridge

## Feature

- kind of structural pattern

## VS Decorator VS Adapter

Bridge, [Decorator](javascript-design-pattern-decorator.md), [Adapter](javascript-design-pattern-adapter.md)

- Decorator is used to add new functionality to an existing object without changing its interface
- Bridge is used to decouple an abstraction from its implementation so that the two can vary independently
- Adapter is used to change the interface of an existing object

## Where to Use

- Database access
- Logging
- Error Handling
- Networking
- file system operation

## Structure of Bridge

- Abstraction
- Refined Abstraction
- implementation
- concrete implementations

## Abstraction

- methods declared is depending on what client need to use

## Refined Abstraction

- provide variants of control logic
- the closest structure to client in bridge pattern
- hold a reference to an object of type [Implementor](#implementor)
- use [implementor] method to implement abstraction method

why describe by "**Refined**"?

- refined of abstraction is still an abstraction
- provide high level interface

## Implementor

- methods declared depend on the functionality

## Concrete Implementor

- provide platform specific code here, like
  - System-specific operations
  - Data manipulation or access method relate to database
  - Algorithmic implementations

## Code

```ts
// abstraction
interface NetworkingOperation {
  sendRequest(): void;
}

// implementor
interface NetworkProtocol {
  connect(): void;
  disconnect(): void;
  send(data: string): void;
}

// concrete implementor
class TCPProtocol implements NetworkProtocol {
  connect(): void {
    console.log('TCPProtocol connect');
  }
  disconnect(): void {
    console.log('TCPProtocol disconnect');
  }
  send(data: string): void {
    console.log('TCPProtocol send');
  }

}
// concrete implementor
class UDPProtocol implements NetworkProtocol {

  connect(): void {
    console.log("Establishing UDP connection ...");
  }
  disconnect(): void {
    console.log("Closing UDP conection...");
  }
  send(data: string): void {
    console.log("Sending UDP data", data);
  }
}

// refined abstraction
class HTTPRequest implements NetworkingOperation {
  protected protocol: NetworkProtocol;
  constructor(protocol: NetworkProtocol) {
    this.protocol = protocol;
  }

  sendRequest() {
    this.protocol.connect();
    this.protocol.send("HTTP Request");
    this.protocol.disconnect();
  }
}

// refined abstraction
class FTPRequest implements NetworkingOperation {
  protected protocol: NetworkProtocol;

  constructor(protocol: NetworkProtocol) {
    this.protocol = protocol;
  }
  sendRequest() {
    this.protocol.connect();
    this.protocol.send("FTP Request");
    this.protocol.disconnect();
  }
}

const tcpProtocol = new TCPProtocol();
const udpProtocol = new UDPProtocol();

const httpRequest = new HTTPRequest(tcpProtocol);
httpRequest.sendRequest();

const ftpRequest = new FTPRequest(udpProtocol);
ftpRequest.sendRequest();
```