# Vue - Script

* [Catagories](#catagories)
* [data](#data)
* [computed](#computed)
* [props](#props)
* [methods](#methods)
* [watch](#watch)
* [emits](#emits)

## Catagories

state

- [data](#data)
- [computed](#computed)
- [props](#props)
- [methods](#methods)
- watch
- emits
- expose

lifecycle

- beforeCreate
- created
- beforeMount
- updated
- beforeUnmount
- beforeUpdate
- updated
- beforeUnmount
- unmounted
- errorCaptured
- renderTracked
- renderTriggered
- activated
- deactivated
- serverPrefetch

## data

Essential

- View updates when value changes

How to Define

```js
export default {
    data() {
        return { a : 1  }
    }
}
```

How to use

```js
<template>
  <div>
    <p>{{a}}</p>
  </div>
</template>
```

## computed

Essential

- value is calculated from [data](#data), [props](props)

How to Define

```vue
<p>Has published books:</p>
<span>{{author.books.length > 0 ? 'Yes': 'No'}}</span>
<script>
export default {
  data() {
    return {
      author: {
        name: 'John Doe',
        books: [
          'Vue.js',
          'React.js',
          'Angular.js'
        ]
      }
    }
  }
}
</script>
```

Usage same as [data](#data)

```vue
<p>Has published books:</p>
<span>{{publishedBooksMessage}}</span>
<script>
export default {
  data() {
    return {
      // ...
    }
  },
  computed: {
    publishedBooksMessage() {
      return this.author.books.length > 0 ? 'Yes': 'No'
    }
  }
}
</script>
```

## props

Essential

- Component external interface, `<Component0 prop1="value1" prop2="value2" />`

How to Define

```js
<script>
export default {
  props: {
    height: Number,
    message: {
      type: String,
      default: 'Hello World'
      validator: (value) => {

      }
    }
  }
}
</script>
```

How to use

```vue
<template>
  <Demo message="Hello World" />
</template>
<script>
import ComponentA from './ComponentA.vue'
export default {
  components: {
    ComponentA
  }
}
</script>
```

[`:`](vue-directives.md#v-bind) Syntax: Assign **Javascript Expression** to props

```vue
<BlogPost :message="post.title + ' by ' + post.author.name"></BlogPost>
```

## methods

Essential

- Pass as event handler to interactable elements

How to define

```js
export default {
  methods: {
    greet() {
      return 'Hello World'
    }
  }
}
```

How to use

```vue
<template>
  <button @click="greet">Greet</button>
</template>
```

## watch

Essential

- Event listener for [data](#data), [props](#props)

How to define

- In [option API]: watcher's name should be same as the variable it watches

```js
export default {
  data() {
    return {
      searchQuery: ''
    }
  },
  watch: {
    searchQuery(newQuery, oldQuery) {
      this.fetchData(newQuery)
    }
  }
}
```

How to use

- Triggered when `searchQuery` changes

Deep watcher

- Triggered when watched value assgined to a new object
- Won't trigger if watched object's property changes
- `deep: true` option

```js
watch: {
  searchQuery: {
    handler(newQuery, oldQuery) {
      this.fetchData(newQuery)
    },
    deep: true
  }
}
```

## emits

Essential

**How to define**

- Array syntax

```js
export default {
  emits: ['check']
  created() {
    this.$emit('check', 'Hello World')
  }
}
```

- Object Syntax
  - emit event is the object key
  - key's value is a validator function which returns a boolean

```js
export default {
  emits: {
    check: (value) => {
      return value === 'Hello World'
    }
  }
}
```

**How to Trigger**

```vue
<template>
  <button @click="$emit('check', 'Hello World')">Check</button>
</template>
```


