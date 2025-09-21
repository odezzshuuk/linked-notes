# CSS - Best Practicas

## Center an Element

1. use [flex layout](css-flex.md)

2. use margin and transform

```css
.foo {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translateX(-50%);
}
```

## Convention

```css
.Convention {
    /* 1. Position & Display */
    /* 1.1 Position: top, right, bottom, left, z-index */
    /* 1.2 Display: flex, grid, inline, block, hidden */

    /* 2. Box Model */
    /* 2.1 Width & Height */
    /* 2.2 Padding, Margin, Border */
    margin: 0;
    padding: 0;
    border-width: 0;

    /* 3. Layout */
    /* 3.1 justify, align, col, row */
    /* 3.2 gap, space, wrap */
    /* 3.3 flex-grow, flex-shrink, flex-basis */

    /* 4. Typography */
    /* 4.1 font-family, font-size, font-weight */
    /* 4.2 color, inline-height, text-align */

    /* 5. Background */
    /* 5.1 bg-color, bg-image, bg-size */

    /* 6. Effects */
    /* 6.1 transform, transition, animation */

    /* 7. Miscellaneous(Visual Effects) */
    /* 7.1 box-shadow, overflow, cursor, visibility */
    /* 7.2 filter, backdrop, mask, clip-path */

    /* 8. pseudo-classes */
    /* 8.1 hover, focus, active, visited */
}


```
