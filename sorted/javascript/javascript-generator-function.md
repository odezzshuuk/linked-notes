# JavaScript - Generator Function

* [Declare Generator Function](#declare-generator-function)
* [Features](#features)

## Features

- **Calling** a generator function, will return a [Generator](javascript-generator.md) Object

## Declare Generator Function

- use `function*` to declare a generator function
- `*methodName()` to declare a generator method

generator function

```js
function* generator(i) {
    yield i + 1;
    yield i + 2;
    yield i + 3;
}
const gen = generator(2);
console.log(gen.next().value); // 3
console.log(gen.next().value); // 4
console.log(gen.next().value); // 5
```

generator method

```js
class Foo {
    *generatorMethod(i) {
        yield i + 1;
        yield i + 2;
        yield i + 3;
    }
}
```

## When Generator Function be Executed

For Code

```js
function* foo(i) {
    console.log("foo called")
    yield i + 1;
    yield i + 2;
    yield i + 3;
}
const gen = foo(2);  // ①
console.log(gen.next().value); // ②
```

At the beginning, [generator function](javascript-generator-function.md) at paused state

- that is to say, the code in function body **has not been executed**
- ① : will output nothing

Generator function will execute at the first time when [`next()` method of returned generator](javascript-generator.md#next) is called

- ② : will output `foo called` and `3`

