# CSS Selector

* [Element Selector](#element-selector)
* [id Selector "\#"](#id-selector-"\#")
* [class selector](#class-selector)
* [Descendant Selector](#descendant-selector)
* [children selector](#children-selector)
* [group selector](#group-selector)
* [attribute selector](#attribute-selector)
* [adjacent sibling combinator](#adjacent-sibling-combinator)
* [pseudo-class selector](#pseudo-class-selector)
* [pseudo element selector](#pseudo-element-selector)
* [General Sibling Combinator](#general-sibling-combinator)
* [Exclude A Selector](#exclude-a-selector)
* [Pure Css Selector](#pure-css-selector)

## Element Selector

- select html element

```css
element {
  width: 100px;
  height: 100px;
}
```

div, p, h1, h2 are all element

## id Selector "\#"

```css
#id {
  text-align: center;
  color: red;
}
```

select element `id="value"`, id is unique

## class selector

- use prefix `.`

```css
.classvalue {
  width: 100px;
  height: 100px;
}
```

select all elements with `class="value"`

## Descendant Selector

use space to separete ancestor and descendant

- select tag `div` with descendant tag `p`

```css
div p {
  width: 100px;
  height: 100px;
}
```

## children selector

use `>` to select children

- select tag `div` with children tag `p`

```css
div > p {
  width: 100px;
  height: 100px;
}
```

## group selector

select multiple elements, separate selectors by `,`

- select `h3` and `p` element at the same time

```css
h3,
p {
  width: 100px;
  height: 100px;
}
```

## attribute selector

```css
input[type='submit'] {
  width: 100px;
}
```

- select input element with attribute type="submit"

## adjacent sibling combinator

the second element is immediately preceded by the first, the second element will be selected

```css
img + p {
  font-weight: bold;
}
```

- for above example `<p>` after `<img>` will be selected

**owl selector**: select all sibling element after first element

```css
body * + * {
  margin-top: 1.5em;
}
```

## pseudo-class selector

- use to capture special state of element

> [pseudo-class list](css-pseudo-class.md)

- start with `:`, select special state of element

`selector:hover`

- select element when mouse hover

`selector:nth-child(an + b)`

- select numeric position in a series of siblings matches the pattern $an + b$(a, b are integers)
  - n is start from 0, until $an + b$ bigger than number of siblings
- sibling element: a set of **matching elements** with the same **parent** element

> `:nth-child(2)`: select second sibling element

example

```css
li:nth-child(-n + 3) {
  color: red;
}
```

- select first three li element at same parent element

pseudo-class can be used with CSS class

```html
<style>
  a.red:visited {
    color: #ff0000;
  }
</style>
<a class="red" href="####">CSS</a>
```

## pseudo element selector

> element that doesn't exist in the HTML markup

- `::before`: represent the first child of an element
- `::after`: represent the last child of an element
- often used with `content` property

```html
<p class="boring-text">Here is some plain old boring text.</p>
<p>Here is some normal text that is neither boring nor exciting.</p>
<p class="exciting-text">Contributing to MDN is easy and fun.</p>
```

```css
.exciting-text::after {
  content: ' <- EXCITING!';
  color: green;
}

.boring-text::after {
  content: ' <- BORING';
  color: red;
}
```

## General Sibling Combinator

- A ~ B: select all B element that follow A element, immediately or not

```css
p ~ span {
  color: red;
}
```

## Exclude A Selector

select p element except with class fancy

```css
p:not(.fancy) {
}
```

select element not div and span

```css
body :not(div):not(span) {
  /* ... */
}
```

## Pure Css Selector

- contain at least one local **class or id**

