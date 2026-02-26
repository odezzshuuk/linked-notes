# Javascript - this

* [what It Is](#what-it-is)
* [this in function](#this-in-function)
* [This In Callback](#this-in-callback)
* [This In Closure](#this-in-closure)
* [This In Arrow Function](#this-in-arrow-function)
* [this in constructor](#this-in-constructor)
* [this in class](#this-in-class)
* [this in global context](#this-in-global-context)
* [how to check this bind to what](#how-to-check-this-bind-to-what)
* [globalThis](#globalthis)

## what It Is

- In a method, 'this' refers to the [object](javascript-object.md) to which the method belongs.
- In global functions
  - in non-strict mode, `this` represents the `window` object
  - in strict mode, `this` is `undefined`.
- Within an object property reference chain, only the previous or, in other words, the last level in the calling context is effective.

```javascript
function foo() {
  console.log(this.a);
}
var obj2 = {
  a:42,
  foo: foo
};
var obj1 = {
  a: 2,
  obj2: obj2
};
obj1.obj2.foo();  // 42
```

## this in function

this bind to the object that call the function

```js
function foo() {console.log(this.a);}
var obj = {a: 2, foo: foo};

obj.foo(); // this bind to obj
```

- this is bind to obj

use method `call()`, `bind()`, `apply()`, can set which object this bind to

use `null` to bind `this` can ignore `this`

```js
var bar = foo.bind(null, 2);
bar(3);
```

`object.create(null)` create a object without prototype

```js
var o0 = Object.create(null);
var bar = foo.bind(o0, 2);
```

## This In Callback

## This In Closure

[here is closeure](javascript-closure.md)

## This In Arrow Function

## this in constructor

- `this` represent the object create by [constructor](javascript-constructor.md)

```js
function C() {
  this.a = 42;
}

let obj = new C();
console.log(o.a); // 42
```

- `this` bind to `obj`

## this in class

example class

```js
class Foo {
  static fx() {
    console.log(this);
  }
}
const f = new Foo();
```

- in static method: this is `Foo`
- static field initialize: this is `Foo`
- in instance method: this is `f`

## this in global context

- in web browser: `this === window` is true
- in node module: `this === undifined` is true

## how to check this bind to what

1. new bind: `var bar = new foo();`
2. explicit bind: `var bar = foo.call(obj);`
3. implicit bind: `var bar = obj.foo();`
4. default bind: `var bar = foo();`

## globalThis

the reason why globalThis

- Historically, accessing the **global `this`** has required different syntax
  - in browser，global `this` is `window`
  - in [web worker]()，global `this` is `self`
  - in [nodejs](nodejs.md)，global `this` is `global`

`globalThis` provides a standard way of accessing the global `this` 

- guaranteed to work in window and non-window contexts 
- the global scope `this` is `globalThis`

Add Property to `globalThis`

```js
if (typeof globalThis.Intl === 'undefined') {
  // No Intl in this environment; define our own on the global scope
  Object.defineProperty(globalThis, 'Intl', {
    value: {
      // Our Intl implementation
    },
    enumerable: false,
    configurable: true,
    writable: true,
  });
}
```
