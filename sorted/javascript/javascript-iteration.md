# Iteration in JavaScript

* [Content](#content)
* [Generator Function](#generator-function)
* [Generator](#generator)
* [Iteration Protocols](#iteration-protocols)
* [keyword yield](#keyword-yield)

## Content

- keyword [yield](#keyword-yield)
- Generator Function
- Generator Object
- 2 protocols
  - Iterator protocol
  - Iterable protocol
- corresponding protocols for async iteration
  - Async Iterator protocol
  - Async Iterable protocol

## Generator Function

[Generator Function](javascript-generator-function.md)

## Generator

[Generator](javascript-generator.md)

## Iteration Protocols

[Iteration Protocols](javascript-iteration-protocols.md)

## keyword yield

> [yield in CSharp](csharp-yield.md)

syntax

`[rv] = yield [expression]`

- `rv`: the argument passed to the `next()` method of a generator object
- `expression`: the value to return from the generator function

```js
function* generator() {
    yield 10;
    x = yield 'foo';
    yield x;
}
var gen = generator();
console.log(gen.next()); // { value: 10, done: false }
console.log(gen.next()); // { value: 'foo', done: false }
console.log(gen.next(5)); // executes x=5, returns { value: 5, done: false }
```

how to understand yield

1. used to pause and resume the execution of a generator function
2. generator function will execute normally until it reaches the `yield` keyword
3. When a generator function encounters the yield keyword, it pauses execution and returns the value of the expression following the yield.
4. When the next next() method is called on a generator function, it continues execution from the paused position.
5. Execution stops upon encountering yield.
6. It can be used as a parameter in a function; yield will receive the first value passed to next().

example of used as parameter

```js
function* generatorFn(initial) {
    console.log(initial);
    console.log(yield);
    console.log(yield);
}
let generatorObject = generatorFn('foo');
generatorObject.next('bar');  // foo
generatorObject.next('baz');  // baz
generatorObject.next('qux');  // qux
```

keyword `yield*`

- pass the iteration behavior to another iterable object

```js
function* generatorFn() {
    yield* [1, 2, 3];
}
```


