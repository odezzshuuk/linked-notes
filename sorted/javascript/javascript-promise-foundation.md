# Javascript - Promise Foundation

* [States Of Promise](#states-of-promise)
* [Create Promise](#create-promise)
* [resolve](#resolve)
* [reject](#reject)
* [When error thrown from promise](#when-error-thrown-from-promise)
* [Await a promise](#await-a-promise)
* [Static Method](#static-method)
* [Promise Instance method](#promise-instance-method)
* [chained promise](#chained-promise)
* [Promise reject event](#promise-reject-event)

## States Of Promise

- there are three states of promise object: pending, fulfilled, rejected
  - `pending`: initial state, pending state
  - `fulfilled`: represent operation completed successfully
  - `rejected`: represent operation failed
- `fulfilled` and `rejected` are both `settled` state
- promise is always one of the three states

**pending promise**

```js
(async () => {
  const promise = new Promise(() => {
    setTimeout(() => {
    }, 1000);
  }).then(() => {
    console.log('nothing')
  });
})();
```

- If i don't call `resolve` or `reject` in promise, promise will be **pending**
- And there will be **no output**
- Because the promise is **still pending**, function in then will never be called

**settled promise**

```js
const success = true;
(async () => {
  const promise = new Promise((resolve, reject) => {
    if(success) {
      resolve(value);
    } else if(fail) {
      reject(reason);
    } else {
      throw error;
    }
  }).then(
    () => console.log('success'),
    () => console.log('fail'),
  )
})()
```

- when `success` is `true`, there will be **success** output
- when `success` is `false`, there will be **fail** output

## Create Promise

Syntax: `new Promise((resolve, reject) => { ... }))`

```js
const success = true;
const fail = false;
const promise = new Promise((resolve, reject) => {
  // do something
  if (success) {
    resolve(value);
  } else if(fail) {
    reject(reject);
  } else {
    throw error;
  }
});
```

## resolve

`resolve: (value: T) => void`

- when `resolve(value)` execute: wrapping `value` into a Promise Object
- the `value` can be parsed by `then(onFullfilled, onRejected)` method as [`onFullfilled`](javascript-promise-then.md#parameters) callback function argument
- in ts, type of `value` can be restricted by generic type `T`

## reject

`reject: (message: any) => void`

- `reject(message: any)`: wrapping `reason` into a Promise Object
- the `message` can be parsed by `then(onFullfilled, onRejected)` method as [`onRejected`](javascript-promise-then.md#parameters) callback function argument

## Example

```ts
type Point = {
  x: number;
  y: number;
}
const p = { x: 3, y: 5 }
const flag = 1
const promise = new Promise<Point>((resolve, reject) => {
  if (flag === 1) {
    resolve(p);  // resolve value must be type of Point
  } else {
    reject('reject message can be any type');
  }
}).then((point) => {
  console.log(point.x, point.y);
}, (reason) => {
  console.log(reason);
});
```

## When error thrown from promise

- `error` will be wrapped into a Promise Object
- `error` will be passed to `onRejected` callback function
- or parsed by `catch()` method

## Await a promise

- **unwrap** a promise

[await](javascript-async-await.md)

```js
let value = await promise;
console.log(value);
```

value from `resolve(value)` or `reject(reason)`

## Static Method

`Promise.all(iteratable_promise)`

- takes an iterable [promise]() as argument 
- returns a single promise
  - when all input promises fulfilled, return an array of fulfillment values
  - when any of input promises rejected, return the first rejection reason

`Promise.settled(iteratable_promise)`

- takes an iterable [promise]() as argument 
- returns a single promise with an array of object that describe the outcome of **each promise**

[Promise.resolve()](javaScript-promise-resolve.md)

Promise.reject()

## Promise Instance method

[then()](javascript-promise-then.md)

[catch()](javascript-promise-catch.md)

[finally()](javascript-promise-finally.md)

- with method `then(), catch(), finally()`, Promise Object can be chained together

## chained promise

```js
myPromise
  .then(value => {value + ' and bar'})
  .then(value => {value + ' and bar again'})
  .catch(err => console.log(err));
```

similar process with [await/async](javascript-async-await.md)

```js
async function foo() {
    try {
        const result = await syncDosomething();
        const newResult = await syncDoSomethingElse(result);
        const finalResult = await syncDoThirdThing(newResult);
        console.log(`Got the final result: ${finalResult}`);
    } catch {
        failureCallback(err);
    }
}
```

## Promise reject event

- `unhandledrejection`: when a Promise object is rejected, and there is no reject handler, `unhandledrejection` event will be triggered
- `rejectionhandled`: when a Promise object is rejected, and there is a reject handler, `rejectionhandled` event will be triggered

```js
const myPromise = new Promise((resolve, reject) => {
    if (success) {
        resolve(value);
    } else {
        reject(error);
    }
});
```

- `reject(error)`: this is the reject handler

