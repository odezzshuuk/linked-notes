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

## defineModel(): Declaring Double Way Binding

```vue
<script setup>
const model = defineModel()
</script>

<template>
    <input type="text" v-model="model" />
    <!-- equivalent to -->
    <input
        :value="text"
        @input="event => text = event.target.value">
</template>
```

##  watch(): Watching reactive state changes

```vue
<script setup lang="ts">
const count = ref(0)
watch(count, (count, prevCount) => {
  /* ... */
})
</script>
```

