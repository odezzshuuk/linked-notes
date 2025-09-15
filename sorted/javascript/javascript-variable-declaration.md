# JavaScript - Variable

## var statement

- Scope of variables declared with `var`: **Within a function** or **in the global scope**
- Variables declared with `var` are added as properties to the [variable object](javascript-context.md), and once set, their values cannot be changed, and the properties cannot be deleted.

The **declaration** of a variable is hoisted, but the **definition** is not hoisted.

Illustrate this with following code

```js
function foo() {
    console.log(age);
    var age = 26;
}
console.log(age);  // undifined
```

*ECMAScript will treat above code as:*

```js
function foo() {
    var age;
    console.log(age);
    age = 26;
}
```

- Scope of variable declared in [module]() is **within the module** not added as properties to the global object
- where ever it appears, it will be processed before any code is executed

- ~coresponding name is added to the global environment record's `[[varname]]`, `[[varname]]` can distinguish **global variable** and **variable object property**~

```javascript
console.log(x);  // undifined
var x = 1;
```

> In browsers, global variables and functions defined with var become properties and methods of the window object.

## let declaration

> Keyword introduced after ECMAScript 6

- let variables are scoped within blocks, i.e., between `{}`
- The biggest difference between let and var is scope
- let cannot be used alone as a block body

```javascript
if (true) let a = 1; // Syntax error
```

## const declaration

- const variables must be assigned a value at declaration
- Assigning a [primitive value](javascript-variable-copy-and-reference.md) to a const variable means the value cannot be changed
- You can change the properties of a const object, but cannot reassign the object itself
- A const array can be modified, but cannot be reassigned

## Non-identifier Names

- in non-strict mode, treated as a global object variable
- in strict mode, ReferenceError is thrown

## Statement And Declaration

Declaration keywords:

- let, const, function, function*, async function, async function*, class, export, import

Most control flow structure only accept statement, so:

```javascript
if (condition) {
    // statement1...
    let l = 0;  // error
} else {
    // statement2
    var i = 0; // a statement
}
```
