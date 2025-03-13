# JavaScript Object Generator

* [what is this](#what-is-this)
* [next()](#next())
* [return()](#return())
* [throw()](#throw())
* [Built-in Generator Object](#built-in-generator-object)

## what is this

- the Object return by a [generator function](javascript-generator-function.md)
- have three method: `next()`, `return()`, `throw()`

> [Analogy to IEnumerator in C#](csharp-ienumerator.md)

## next()

return value

- An [`IteratorResult`](javascript-iteration-protocols.md#iteratorresult-interface) Object
  - `value`: the value of `yield` expression in [generator function]()
  - `done`: boolean
    - `true`: if the generator is past the end of its control, the generator is exited by `return`(which may by undefined)
    - `false`: if the generator is exited by `yield`

if pass argument to `next(value)` method

- the value of `yield*` expression is that argument

## return()

- method that terminates the generator function prematurely

return 

- An [`IteratorResult`](javascript-iteration-protocols.md#iteratorresult-interface) Object
  - `value`
    - the value given as argument to `return(value)`
    - or the value from [yield expression](javascript-iteration.md#keyword-yield) which is wrapped in [try...finally]()
  - `done`: boolean
    - `true`: 
    - `false`:

## throw()

- `g.throw(exception)` as if a throw statement is inserted in the generator at current suspended position
- if generator function doesn't handle the exception, the generator will be closed
- if generator function handle the exception, the execution will skip current yield and continue

function body doesn't handle the exception

```js
function* generatorFn() {
    for (const x of [1, 2, 3]) {
        yield x;
    }
}
const g = generatorFn();  // suspended
console.log(g);
try {
    g.throw('foo');
} catch (e) {
    console.log(e);
}
console.log(g);  // closed
```

function body handle the exception

```js
function* generatorFn() {
    try {
        for (const x of [1, 2, 3]) {
            yield x;
        }
    } catch (e) {
        console.log(e);
    }
}
const g = generatorFn();  // suspended
console.log(g.next());   // {value: 1, done: false}
g.throw('foo');
console.log(g.next());   // {value: 3, done: false}
```

## Built-in Generator Object

[Similar concept in CSharp: IEnumerator](csharp-ienumerator.md)

`Generator` Object

- Satisfied [Iterator protocol](javascript-iteration.md#iterator-protocol) and [Iterable protocol](javascript-iteration.md#iterable-protocol)

3 methods, `next`, `return`, `throw`

- `Generator.prototype.next()`: return value of yield expression
- `Generator.prototype.return()`: return specified value and end the iteration of Generator Object
- `Generator.prototype.throw()`: throw an error
