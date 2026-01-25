# CSS - Property Visibility

## what is this

- css property shows or hides an element
- **without** changing the layout of the page

```css
.info{
  visibliity: visible;
}
```

## Available Values

- visible
- hidden: element is invisible, but **still affects layout** as normal, compare to [`display: none`](css-display.md)
- collapse: has different effects for different elements
  - element space will be occupied like `display: none`, for `<table>` rows, columns, column groups, and row groups
  - element space will be occupied, for flex items
  - element treated as hidden for other
