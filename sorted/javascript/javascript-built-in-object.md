# Javascript Built-in Object

- [JSON](#json)
- [Function](#function)
- [setTimeout()](#settimeout)
- [setInterval()](#setinterval)
- [setImmediate()](#setimmediate)
- [clearTimeout()](#cleartimeout)
- [WeakMap](#weakmap)
- [Intl](#intl)
- [Performance](#performance)
- [uri decode and encode](#uri-decode-and-encode)

## Date

get ISO 8601 time

- **ISO 8601** time is standard time for worldwide exchange and communication

```js
console.log(new Date().toISOString());
```

get UTC time

- UTC time

```ts
console.log(new Date().toUTCString());
```

get local time

```ts
console.log(new Date().toLocaleString());
```

get time with time zone

```ts
console.log(new Date().toString());
```

## JSON

`JSON.stringify()`: Convert an [Object]() to a JSON string

```js
console.log(JSON.stringify({x: 5, y: 6}));
// {"x":5,"y":6}
```

## Function

- every function is a Function Object

> function(){}.constructor === Function

## setTimeout()

Set a timer which executes a function or specified piece of code once the timer expires

Syntax:

- `setTimeout(function, delay, param1, param2, ...) `

Parameters:

- `function`: the function to be executed
- `delay`: the number of milliseconds to wait before the function is executed
  - `delay` is not guaranteed time, it is minimum time because [event loop](nodejs-event-loop.md)
- `param1, param2, ...`: optional parameters to be passed to the function

return value

- a positive integer means timeoutID

## setInterval()

set a timer which executes a function or specified piece of code **repeatedly**, with a fixed time delay between each call to the function

Syntax:

- `setInterval(function, delay, param1, param2, ...)`

Parameters

- same to `setTimeout`

## setImmediate()

- Interrupt long-running operations
- Execute after the browser completes other operations
- In nodejs, [setImmediate()](nodejs-timers.md#setimmediate)

## clearTimeout()

`clearTimeout(timeoutID)`

- clear a timeout previously established by setTimeout()

## WeakMap

[WeakMap](javascript-built-in-object-weakmap.md)

## Intl

[Intl](javascript-built-in-object-intl.md)

## Performance

[Performance](javascript-built-in-object-performance.md)

## uri decode and encode

- `decodeURI()` for decode uri
- `encodeURI()` a string to uri format

```js
const uri = 'https://mozilla.org/?x=шеллы';
const encoded = encodeURI(uri);
console.log(encoded);
// Expected output: "https://mozilla.org/?x=%D1%88%D0%B5%D0%BB%D0%BB%D1%8B"

try {
  console.log(decodeURI(encoded));
  // Expected output: "https://mozilla.org/?x=шеллы"
} catch (e) { // Catches a malformed URI
  console.error(e);
}
```

- i didn't find difference between `encodeURI()` and `encodeURIComponent()`
- and `decodeURI()` and `decodeURIComponent()`

## TypedArray

- think about TypedArray as an abstract class

TypedArray Object

- Int8Array
- Uint8Array
- Uint8ClampedArray
- Int16Array
- Uint16Array
- Int32Array
- Uint32Array
- Float32Array
- Float64Array
- ...

