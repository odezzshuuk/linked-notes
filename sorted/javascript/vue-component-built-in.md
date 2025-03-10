# Vue - Component Built-in

## What Are They

- component's members that exposed on the component instance

## Feature

- All Built-in members is readonly, except `$data`

## Catagory

Field

- $data
- $props
- $el
- $refs
- $slots
- $attrs
- $root

Method

- $watch()
- $emit()
- $forceUpdate()
- $nextTick()

## $refs

- object that contains all the [refs](vue-template-attributes.md#ref) in the component

```vue
<template>
  <input ref="inputElt" />
  <button ref="buttonElt">Click</button>
</template>
<script>
export default {
  mounted() {
    this.$refs.inputElt.focus() // access input element
    this.$refs.buttonElt.addEventListener('click', this.handleClick)  // access button element
  }
}
</script>
```

## $attrs

- Represent [html attribute](html-element-attribute.md) pass to the component, like `class`, `style`, `id`
- Which will further parse to root element
- [`props`](vue-script.md#props) and [`emits`](vue-script.md#emits) are not include

if parent component content looks like:

- Assume `propA` is a property defined in [`props`]

```vue
<div>
  <Component0 class="bg-red" propA="foo" />
</div>
```

then rendered html will be:

- `propA` will not appear on the root element

```html
<template class="bg-red">
  <!-- body -->
</template>
```




