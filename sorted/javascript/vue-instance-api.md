# Vue - Instance API

## data

- When a Vue instance is **created**, all [properties](javascript-property.md) in data are added to Vue's reactivity system
- When a property in data changes, the view will update
- Properties added to a Vue instance **after creation** will not be added to Vue's reactivity system
- The data of a component instance must be a function that returns an object
- You can access data via `vm.$data`, where vm is the Vue instance

```js
var data = {a: 1};

var vm = new Vue({
    data: data 
})

vm.a == data.a // true
```
- object.freeze() prevents modification of existing properties

## methods


## mount element: el

- el: 'target'
  - target refers to the mount target
  - target is a DOM element, which can be an HTML element or a CSS selector
  - target is an element that already exists on the page
- 只能用在new创建的Vue实例中

> For example, `el: '#app'` mounts to the element with id 'app'

## props

- Array or object
- Used for passing data from parent [component](vue-register-component.md#通过props传递组件数据) to child component

```html
<child-component prop_name="val" />
```

- Syntax:

```js
props: [
    'prop_name_1':{options}, 
    'prop_name_2':{options}
]
```

- The `options` for a prop can use the following attributes:
  - type: Used to check if `prop_name` is a specific type; can be String, Number, Boolean, Array, Object, Date, Function, Symbol, [custom constructor], or an array of multiple types
  - default: Used to specify the default value of `prop_name`
  - required: Used to specify whether `prop_name` is required
  - validator: Used to specify whether the value of `prop_name` is valid

## Life Circle of Vue Instance

[Vue Instance's Life Circle](vue-lifecycle.md)
