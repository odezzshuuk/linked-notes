# VUE - Single File Component (SFC)

## defineProps()

## defineEmits()

## defineModel()

ComponentA.vue

```vue
<script setup>
const defaultModel = defineModel()
const input = defineModel('input')
</script>

<template>
    <input type="text" v-model="defaultModel" />
    <input type="number" v-model="input" />
</template>
```

App.vue

```vue
<script setup>
const text = ref('hello')
const count = ref(0)
</script>
<template>
    <ComponentA v-model="text" v-model:input="count" />
</template>
```

- `v-model="text"` will pass `text` value to `defaultModel` in `ComponentA.vue`
- `v-model:input="count"` will pass `count` value to `input`

## Exposing Reactive State To Template

By `setup()` or `<script setup>`

- `<script setup>`

> `<script setup>` is more common

```vue
<script setup lang="ts">
import { ref } from 'vue'
const count = ref(0)
function increment() {
    count.value++
}
}
</script>
    
<template>
  <button @click="increment">Count is: {{ count }}</button>
</template>
```

- `setup()`

```vue
<script lang="ts">
let count = 0;
function increment() {
  count++;
}
export default {
  name: 'App',
  setup() {
    return { count, increment };
  }
}
</script>

<template>
  <button @click="increment">Count is: {{ count }}</button>
</template>
```
