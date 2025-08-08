# CSS Containing Block

- Containing block mostly is the nearest **block-level** element in the ancestor, ~~not always parent element~~

## How to determine containing block

- if [positioned element's](css-positioning.md#positioned-element) containing block is nearest positioned ancestor
- if not containing block is the nearest block container

## Description in MDN

how to determine the containing block depends on the element's [position](css-positioning.md) property

> **meaning of containing block**: the size and position of an element are often affected by its containing block, such as width, height, padding, margin, and the position properties top, right, bottom, and left

if `position` value is `static, relative, sticky`

- Its containing block may be formed by the content edge of the nearest **ancestor block**
- It may be a block container
- It may be a new [formatting context]()

If the position property is `absolute`

- The containing block is formed by the padding edge of the nearest ancestor element with a position value other than static

If the position property is `fixed`

- In the case of continuous media, the containing block is the viewport (window, such as browser window), for paged media it's the page area

If the position is `absolute` or `fixed`, the containing block may be formed by the padding edge of the nearest parent element that satisfies the following conditions:

- The value of transform or perspective is not none
- The value of will-change is transform or perspective
- The value of filter is not none or the value of will-change is filter
- The value of contain is paint.
