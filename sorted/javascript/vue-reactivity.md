# VUE - Reactivity Essential

## ref(): Declaring reactive value

```ts
import { ref } from 'vue'
const count = ref(0)
```


## reactive(): Declaring reactive object

```vue
<script setup lang="ts">
import { reactive } from 'vue'
const state = reactive({ count: 0 })
</script>
```

## computed(): Declaring computed value

- computed value is calculated from other reactive state 

```vue
<script setup lang="ts">
import { ref, computed } from 'vue';

const count = ref(0);
const isFive = computed(() => count.value === 5);

function increment() {
  count.value++;
}
</script>
```


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
