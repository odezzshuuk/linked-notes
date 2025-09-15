# NodeJS Process - process.nextTick()

## Features

- callback pass to `process.nextTick()` going to executed on the **current iteration of event loop**
- callback pass to `process.nextTick()` will be resolved before the event loop continue
- or rather, `process.nextTick()` will be executed after [every event phase](nodejs-event.md#phase-detail) queue finishing
- recursive `process.nextTick()` will block the event loop

## Why would that be allowed

- A design philosophy: An API should be asynchronous where it doesn't have to be
- This philosophy can lead to some potentially problematic situations

```js
let bar;
function someAsyncApiCall(callback) {
  callback();
}
someAsyncApiCall(() => {
    // since someAsyncApiCall hasn't completed, bar hasn't been assigned any value
    console.log('bar', bar); // undefined
})

bar = 1
```

- in this code: `someAsyncApiCall()` is actually operate an synchronous operation
- the callback tries to reference a variable that is not yet defined in the scope
- placing callback in `process.nextTick()` will solve this problem

## Take A Look

defining an asynchronous function, does not actually perform asynchronous operation, but try to reference a variable that is not yet defined in the scope

> undefined variable `bar`

```js
let bar;
// this has an asynchronous signature, but calls callback synchronously
function someAsyncApiCall(callback) {
  // callback();
  process.nextTick(callback);  // use process.nextTick() instead of callback()
}

// the callback is called before `someAsyncApiCall` completes.
someAsyncApiCall(() => {
  // since someAsyncApiCall hasn't completed, bar hasn't been assigned any value
  console.log('bar', bar); // undefined
});

bar = 1;
```

- if `callback` is passed to `process.nextTick(callback)`
  - callback will be executed **after** all the definition of variable, function, etc.
  - meanwhile, callback will be executed [**before entering event loop continue**](nodejs-event.md)

## process.nextTick() vs setImmediate()

[`setImmediate()`](nodejs-timers.md#setimmediate)

- `process.nextTick()` is more immediate `setImmediate()`
- 互换名称会更符合函数的功能
- However, swapping the names would affect most npm packages
- it is recommended to use `setImmediate()` instead of `process.nextTick()`

[and setTimeout()](nexttick-setimmediate-settimeout.md)

## why use `process.nextTick()`

- run a callback run **after the call stack** but **before the event loop continue**

```js
const server = net.createServer();
server.on('connection', (conn) => {})

server.listen(8080);
server.on('listen', () => {});
```

`listen()` is run at beginning of the event loop
- It is possible that the `connection` event is triggered before `listen()`

emitting an event from constructor immediately

```js
const EventEmitter = require('events');

class MyEmitter extends EventEmitter {
  constructor() {
    super();
    process.nextTick(() => {
      this.emit('evnet');
    });
  }
}

const myEmitter = new MyEmitter();
myEmitter.on('event', () => {
  console.log('an event occurred!');
});
```
