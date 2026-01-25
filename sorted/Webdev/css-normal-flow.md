# CSS - Normal Flow

## How elements are laid out in Normal Flow

1. Add a [box model](css-box-model.md) around each element
2. [Block level element](html-element-sort.md) vertical layout, [Inline Element](html-element-sort.md)
3. two vertical adjacent elements with margin, the larger margin is reserved

## In Flow and Out of Flow

- Elements that out of normal flow
  - floated items
  - [position](): absolute, fix
  - `<html>` element
- Get rid of Normal Flow will create a new [BFC](css-block-formatting-context.md)
