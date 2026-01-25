# @ Rules

- [`@import`](#import)
- [`@layer`](#layer)
- [`@media`](#media)

## `@import`

- import styles from another css file

Syntax:

```css
@import url list-of-media-queries;
@import url layer
```

- url: resource location

import from css file

```css
/* styles.css */
@import url("reset.css");
@import url("typography.css");
```

## `@layer`

Syntax

```css
@layer layer-name
```

create layer

```css
@layer utilities {
  .padding-sm {
    padding: 0.5rem;
  }
}

@layer type {
  .box p {
    font-weight: bold;
    font-size: 1.3em;
    color: green;
  }
}
```

- create two layer: `utilities` and `type`

anonymous layer

- any style not in a layer is in an anonymous layer
- anonymous layer gather all the styles that are not in a layer
- anonymous comes after all the named layers
- that means will override styles declared in named layers, cause by [order of cascade](css-understanding-the-cascade.md)


```css
@layer {
  p {
    margin-block: 1rem;
  }
}
```

## `@media`

[@media](css-at-media.md)

