# JavaScript - Variable

## Declaration

[Declaration](javascript-variable-declaration.md)

## Assignment

[Assignment](javascript-variable-assignment.md)

## check type

- `typeof a;` return type of a

## NULL

- represent an empty object pointer
- can be assigned to a variable as a representation of no value

## Array

```javascript
let myNameArray = ['Chris', 'Bob','Jim',]
```

## Object

```javascript
let dog = {name: 'Spot', breed: 'Dalmatian'};
```

## LHS and RHS

```javascript
function foo(a) {
    var b = a;
    return a + b;
}
var c = foo(2);
```

LHS

- `c=`
- `a=2`
- `b=` 

RHS

- `=a`
- `return a + b`,
- `foo(2)`
