# CSS Module File

## Introduction

- is a CSS file in which all class names and animation names are scoped locally by default
- compiled to Interoperable CSS

write like normal file

```css
.className {
  color: green;
}
```

import like js module

- import an Object with all mappings from local names to global names

```js
import styles from "./style.css"

function Button() {
  return (
    <button className={styles.className}>
      Click Me
    </button>
  )
}
```

## Class Naming

- for class name recommended camelCase
- kebab-casing may cause unexpected behavior

> no `style['class-name']`, but `style.className`

## Global Selectors

```css
:global(.className) {
  color: green;
}
```

## Composition

```css
.className {
  color: green;
  background: red;
}

.othreClassname {
  composes: className;
  color: blue;
}
```

- `composes` property must be before other properties
- when export the module, both `className` and `otherClassName` will be exported
- compose multiple classes: `composes: classNameA classNameB`;

compose from other CSS Modules

```css
.otherClassName {
  composes: classname from "./style.css";
}
```

- Compose from different files, the **order of appliance** is **undifined**
- So **avoid** to define **different values** for the **same property** in different files

## Preprocessor

define a global block

```css
:global {
  .global-class-name {
    color: green;
  }
}
```