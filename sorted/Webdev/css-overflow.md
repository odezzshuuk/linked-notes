# Overflow

- [What's for](#whats-for)
- [overflow Property](#overflow-property)

## What's for

- When content is too large cause it larger than box size, In order to prevent content loss, CSS will cause overflow

> but will make content look messy

overflow property can prevent content look messy

```css
.box {
    border: 1px solid #333333;
    width: 200px;
    height: 100px;
    overflow: scroll
}
```

## overflow Property

- `overflow: visible;`
  - Content is not Clipped
  - May be rendered outside the content box
  - Won't create new [BFC](css-block-formatting-context.md)
- `overflow: hidden;`: content will be clipped to fit the padding box, and hide scroll bar
  - `overflow-x: hidden;`
  - `overflow-y: hidden;`
- `overflow: scroll`: add scroll bar for overflow content
- `overflow: clip`
  - Similar to hidden
  - Forbid scroll, its box model is not a scrollable container
  - Won't create new [BFC](css-block-formatting-context.md)
- `overflow: auto`
  - If content is not larger than padding box, it looks like `overflow: visible`
  - Establishes a new [BFC](css-block-formatting-context.md)
  - On desktop browser, **provide scroll bar** if content overflows 
- `overflow: overlay`
  - add scrollbar for overflow content
