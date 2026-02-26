# Javascript - Closure

## what is a closure

- Nest function is a closure
- Closure: A function that has access to the parent scope, even after the scope has closed

## Features

- Variable or property in closure only can be accessed by the function in the closure, no other way to access it
- Closure will occupy more memory
- There is no difference between a closure and an object, in terms of data storage, but a closure is more hidden when accessing data

Closure will cause memory leak if not handled properly

- this code will cause a memory leak

```ts
class LeakyClass {
    private counter = 0;

    constructor() {
        setInterval(() => {
            this.counter++;
            console.log(this.counter);
        }, 1000);
    }
}

const leakyInstance = new LeakyClass();
```

- fix it

```ts
class LeakyClass {
    private counter = 0;

    constructor() {
        setInterval(() => {
            this.counter++;
            console.log(this.counter);
        }, 1000);
    }

    public destroy() {
        if (this.counter) {
            clearInterval(this.counter);
        }
    }
}

const leakyInstance = new LeakyClass();
leakyInstance.destroy();
```

## Nest function

```js
function addSquares(a, b) {
    function square(x) {
        return x * x;
    }
    return square(a) + square(b);
}
```

## Create Closure


```javascript
function outside(x) {
    function inside(y) {
        return x + y;
    }
    return inside;
}
const fnIside = outside(3);  // return inside function
const result = fnInside(5);  // return 8, whenever you call fnInside, it will always use 3 as the value of x
fnInside = null;  // release the reference to fnInside
```

**inner function** add the **outer** scope to its own scope chain, which means

- arguments `x` will not be destroyed after outside function is executed
- `x` will be saved in `fnInside` until `fnInside` is destroyed
- `fnInside = null` will release the memory

Create a closure with anonymous function

```js
const getCode = (function () {
  const apiCode = '0]Eal(eh&2';    // A code we do not want outsiders to be able to modify…

  return function () {
    return apiCode;
  };
})();

getCode();    // Returns the apiCode
```

