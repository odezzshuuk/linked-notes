# Javascript Design Patterns - Proxy

* [What It Is](#what-it-is)
* [Appropriate scenario](#appropriate-scenario)
* [code](#code)

## What It Is

- kind of structural pattern
- acts as an intermediary between client and the target object
- proxy object used to add additional functionality without modifying the real object, such as
  - security checks
  - caching

two component

- **real object**
- **proxy object**

## Appropriate scenario

Protection Proxy

- control access to the real object by checking credentials

Virtual proxy

remote proxy

- provide a local representation of a remote object
- reduce network traffic and latency

caching

- caching result of operation perform on real object
- reduce expensive calculation

Logging proxy

- log the request and response of the real object
- useful for debugging and analysis

## code

```js
const target = {
  name: 'john',
  age: 30
}

const handler = {
  get: function(target, prop) {
    console.log(`Getting ${prop} property`);
    return target[prop]
  },
  set: function(target, prop,value) {
    console.log(`Setting ${prop} property`);
    target[prop] = value;
  },
  deleteProperty: function(target, prop) {
    console.log(`Deleting ${prop} property`);
    delete target[prop];
  }
};
const proxy =  new Proxy(target, handler);
console.log(proxy.name);
proxy.age = 35;
delete proxy.name;
console.log(target); // {age: 35}
```
