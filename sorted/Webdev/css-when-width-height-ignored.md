# CSS - Situations When `width` and `height` Ignored

* [1. Inline Elements (Non-Replaced)](#1.-inline-elements-(non-replaced))
* [2. Table Elements with `table-layout: auto`](#2.-table-elements-with-`table-layout:-auto`)
* [3. Flexbox Items](#3.-flexbox-items)
* [4. Grid Items](#4.-grid-items)
* [5. Absolutely Positioned Elements with Constraints](#5.-absolutely-positioned-elements-with-constraints)
* [6. Elements with `box-sizing` Issues](#6.-elements-with-`box-sizing`-issues)
* [7. Images and Replaced Elements](#7.-images-and-replaced-elements)
* [8. Text Content Overflow](#8.-text-content-overflow)
* [9. Min/Max Constraints Override](#9.-min/max-constraints-override)
* [10. Percentage Heights Without Parent Height](#10.-percentage-heights-without-parent-height)
* [11. Float Elements](#11.-float-elements)
* [12. Transform Scale](#12.-transform-scale)
* [13. CSS Grid with `fit-content()`](#13.-css-grid-with-`fit-content()`)
* [14. Viewport Constraints](#14.-viewport-constraints)

## 1. Inline Elements (Non-Replaced)

Inline elements like `<span>`, `<a>`, `<em>`, `<strong>` ignore width and height:

```css
span {
  width: 200px;    /* Ignored */
  height: 100px;   /* Ignored */
}
```

**Solution:** Use `display: inline-block` or `display: block`

## 2. Table Elements with `table-layout: auto`

Table cells may ignore dimensions when content doesn't fit or table layout is auto:

```css
td {
  width: 50px;  /* May be ignored if content is wider */
}
```

**Solution:** Use `table-layout: fixed` on the table

## 3. Flexbox Items

Flex items can shrink/grow beyond their set dimensions:

```css
.flex-item {
  width: 200px;  /* Can be overridden by flex-grow/shrink */
}
```

**Solution:** Use `flex: none` or `flex-shrink: 0`

## 4. Grid Items

Grid items are constrained by their grid tracks:

```css
.grid-item {
  width: 500px;  /* Ignored if grid track is smaller */
}
```

## 5. Absolutely Positioned Elements with Constraints

When `left`, `right`, `top`, `bottom` conflict with width/height:

```css
.absolute {
  position: absolute;
  left: 0;
  right: 0;
  width: 100px;  /* Ignored - element stretches left to right */
}
```

## 6. Elements with `box-sizing` Issues

Content might overflow the set dimensions:

```css
.box {
  width: 200px;
  padding: 50px;  /* Total width becomes 300px */
  box-sizing: content-box;
}
```

## 7. Images and Replaced Elements

Images maintain aspect ratio by default:

```css
img {
  width: 200px;
  height: 50px;   /* Image will maintain aspect ratio */
}
```

**Solution:** Use `object-fit: fill` to force exact dimensions

## 8. Text Content Overflow

Long words or content can force expansion:

```css
.container {
  width: 100px;
  white-space: nowrap;  /* Long text forces width expansion */
}
```

**Solution:** Use `overflow: hidden` or `word-break: break-word`

## 9. Min/Max Constraints Override

When min/max values conflict:

```css
.element {
  width: 100px;
  min-width: 200px;  /* min-width wins, actual width is 200px */
}
```

## 10. Percentage Heights Without Parent Height

Percentage heights fail when parent has no explicit height:

```css
.parent {
  /* No height set */
}
.child {
  height: 50%;  /* Ignored - parent has no height reference */
}
```

## 11. Float Elements

Floated elements can affect dimensions of their containers:

```css
.container {
  width: 200px;
  /* If floated children extend beyond, container won't expand height */
}
```

## 12. Transform Scale

Visual scaling doesn't affect layout dimensions:

```css
.scaled {
  width: 100px;
  transform: scale(2);  /* Visually 200px but layout still uses 100px */
}
```

## 13. CSS Grid with `fit-content()`

Grid tracks with `fit-content()` can override item dimensions:

```css
.grid-container {
  grid-template-columns: fit-content(100px);  /* May be smaller than 100px */
}
```

## 14. Viewport Constraints

Elements can't exceed viewport dimensions without overflow:

```css
.huge {
  width: 5000px;  /* May cause horizontal scrolling */
}
```

The key is understanding the CSS layout context and using appropriate solutions for each situation.
