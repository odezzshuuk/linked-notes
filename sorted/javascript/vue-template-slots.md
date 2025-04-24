# Vue - Template Slots

## Slot Definition

```vue
<template>
  <div>
    <slot></slot> <!-- slot outlet -->
    <button class="fancy-btn" /> 
  </div>
</template>
```

## Slot Usage

```vue
<FancyButton>
  Press the button! <!-- slot content -->
</FancyButton>
```

This will rendered as

```html
<div>
  Press the button!
  <button class="fancy-btn" />
</div>
```

## Render A Slot Based On Slot Properties

Define a slot with [props(attributes)](vue-script.md#props)

- `ComponentA.vue`

```vue
<div>
  <slot :text="greetingMessage" :count="1"></slot>
</div>
```

Fill slot content based on slot properties

- `ComponentB.vue`
- use [`v-slot`](vue-directives.md#v-slot) directive to retrieve slot properties

```vue
<ComponentA v-slot="{ text, count }">
    <p>{{ text }} {{ count }}</p>
</ComponentA>
<!-- or -->
<ComponentA v-slot="slotData">
    <p>{{ slotData.text }} {{ slotData.count }}</p>
</ComponentA>
```

- `text` is value returned from `greetingMessage` in `ComponentA` 
- `count` is 1


