# JavaScript - Operator

* [Logic Operator](#logic-operator)
* [Math Operator](#math-operator)
* [Compare Operator](#compare-operator)
* [delete](#delete)
* [bit operator](#bits-operator)
* [typeof](#typeof)
* [in](#in)

## Logic Operator

Logic Operator is about `&&`, `||`, `!`

```js
function createArray(array) {
  array || (array = new Array(5));
  return array;
}
```

expression `array || (array = new Array(5))` means

- if `array` is [falsy](), then `array = new Array(5)` will be executed
- else do nothing

`!!` is not a special operator, it is just `!` twice

- Why `!!`? `!!` will convert any value to boolean

```js
console.log(!!null)       // false
console.log(!!undefined)  // false
console.log(!!0)          // false
console.log(!!"abc")      // true
```

> similar to [not not](lua-operator.md#logical-operator) in lua

`??` operator

- if left-hand value is `null` or `undefined`, then return right-hand value
- else keeps left-hand what it is

## Math Operator

- `+`, `-`, `*`, `/`, `%`, `**`
- `++`, `--`
- `+=`, `-=`, `*=`, `/=`

## Compare Operator

`==`: loose equality

- when compare，two operands will first convert to same type, then compare use `===`

```js
"1" == 1 // true
0 == false // true
0 == null // false
null == undefined // true
```

`===`:

- do not convert type before compare

```js
"hello" === "hello"; // true
"hello" === "hola"; // false

3 === 3; // true
3 === 4; // false

true === true; // true
true === false; // false

null === null; // true
[] === [];  // false
```

`Object.is(val1, val2)`

```js
Object.is([], [])
```

## delete

- remove **property** from object

```js
const Employee = {
  firstname: 'John',
  lastname: 'Doe',
}

delete Employee.firstname
console.log(Employee.firstname) // undefined
```

## Bits Operator

`<<`: left shift

- excess bits are discarded
- for positive number, 0 bits are added to the right 
- for negative number, 1 bits are added to the right

```js
const a = 5  // 00000000000000000000000000000101
const b = a << 2  // 00000000000000000000000000010100
console.log(b)  // 20
```

- equal to `a * 2^2`

`>>`: right shift

- excess bits are discarded
- zero bits are added to the left

```js
const a = 100  // 00000000000000000000000001100100
const b = a >> 2  // 00000000000000000000000000011001
console.log(b)  // 25
```

- equal to `a / 2^2`

`>>>` unsigned right shift

- always add zero bits to the left

## typeof

`typeof operand`

- operand 
- return value is a string, and is one of following values
  - string
  - number
  - bigint
  - boolean
  - symbol
  - undefined
  - object
  - function

```js
typeof 3 // "number"
```

## in

`prop in object`

- return `true` if `object` has `prop` property or `prop` is on [prototype chain](javascript-prototype.md#prototype-chain)

> check direct property use [`Object.hasOwn()`](javascript-global-object.md#objecthasown) instead

## Optional Chaining(?.)

syntax

```js
obj.val?.prop
obj.val?.[expr]
obj.func?.(args)
```

on property accessing

```js
const value = obj.first?.second 
```

- javascript will check `obj.first` before access to `obj.first.second`

on function calls

```js
const result = obj.Foo?.()
```

- `undefined` will be return if method `Foo` does not exist, instead of throwing an exception


