# data attribute

## what is this

- a attribute associate with a element
- can be used to **store** data on a element
- not have any effect on the element

## define in html

```html
<article
  id="electric-cars"
  data-columns="3"
  data-index-number="12314"
  data-parent="cars"
>
  ...
</article>
```

## access in js

```js
const article = document.querySelector("#electric-cars");

article.dataset.columns; // "3"
article.dataset.indexNumber; // "12314"
article.dataset.parent; // "cars"
```

## access in css

use [`attr()` function](css-function.md#attr)

```js
article::before {
  content: attr(data-parent)
}
```

use [attribute selector](css-selector.md#attribute-selector)

```css
article[data-parent="cars"] {
  /* ... */
}
```