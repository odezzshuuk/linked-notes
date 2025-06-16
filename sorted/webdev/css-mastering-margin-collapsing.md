# CSS - Mastering Margin Collapsing

> Only happens in [block-level](css-box-model-sorted.md) elements

## scene 1: 2 vertical adjacent elements

- only keep the largest margin

## scene 2: Parent and first/last child

Conditions:

1. Parent element's margin-top and first child, or parent element's margin-bottom and last child:
2. The margin-top of the parent element and its descendant elements is not separated:
  - No Block Formatting Context (BFC) has been created (e.g., via overflow: hidden, float, or display: flow-root), or no clear property has been applied.
  - The parent element has no border, padding, or inline content (e.g., text or inline elements).
3. The margin-bottom of the parent element and its descendant elements is not separated:
  - The parent element has no border, padding, or inline content.
  - The parent element has no height, min-height, or max-height set.

## Ccene 3: Empty Element

- An empty element (with no content) that has no border, `padding`, `height`, `min-height`, `max-height`, inline content, or clear-fix (e.g., overflow: auto or a pseudo-element to clear floats) will not prevent the margin-top and margin-bottom of different blocks from collapsing together.
