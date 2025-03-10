# Vue - Template Attributes

## Summary

- ref

## ref

Essential

- Provide a way to access the element in the template
- Related to [$refs](vue-component-built-in.md#$ref)

How to ref

```vue
<script>
export default {
  mounted() {
    this.$refs.refElt.focus()
  }
}
</script>

<template>
  <input ref="refElt" />
</template>
```

- with `<input ref="refElt" />`, the element can be accessed by `this.$refs.refElt`

`ref` inside `v-for`

```vue
<template>
  <ul>
    <li v-for="item in list" ref="items">
      {{ item }}
    </li>
  </ul>
</template>
```

- `this.$refs.items` will be an array of `li` elements

