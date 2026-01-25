# CSS - Positioning

* [what it is](#what-it-is)
* [position: static](#position:-static)
* [position: relative](#position:-relative)
* [position: absolute](#position:-absolute)
* [position: fixed](#position:-fixed)
* [position: sticky](#position:-sticky)
* [positioned element](#positioned-element)
* [Positioning Contexts](#positioning-contexts)
* [Property align](#property-align)

## what it is

- Allows to take elements out of Normal Flow and make them have different behaviors, for example, put on another element, or keep in the same position in the browser

## position: static

- **Default** position value
- Only indicates that the element is positioned in normal position of [**normal flow**]
- `top, right, bottom, left` has no effect

> `inset` is shorthand for `top, right, bottom, left`, `inset: 10px 30% 20px 0;`

## position: relative

- Allows to modify the position of the element in the document with property `top, right, bottom, left`
- `top, right, bottom, left` can be understood as the direction of **force**

## position: absolute

- Allows to modify the position of the element in the document with property `top, right, bottom, left`
- Positioned relative to the closest [positioned](#positioned-element) ancestor. The ancestor could be parent, grandparent or even further element
- Or position relative to closet [containing block](css-containing-block.md)
- Removed from [normal document flow](css-normal-flow.md)

> in most cases, height or width set to `auto` to fit its content, or fill available space

## position: fixed

- positioned relative to the initial [**containing block**](css-containing-block) [**established by viewport**](css-containing-block.md)
  - except ancestors has `transform` or `perspective` , or `filter` property set to something other than `none`

> in most cases, relative to the browser window

- **remove** [normal document flow](css-normal-flow.md)
- final position determine by `top`, `right`, `bottom`, `left`

> won't be rendered before one of `top`, `right`, `bottom`, `left` properties set

## position: sticky

a hybrid between `relative` and `fixed`

- Act like **relative** position until scroll to a certain threshold
- Then act like **fixed** positioned
- But the space it takes up is still calculated as if it were **relative** positioned
- **MUST** specify one of `top`, `right`, `bottom`, `left` property to make sticky work

```css
.box {
  position: sticky;
  top: 100px;
}
```

- when sticky element top property larger than 100px
  - positioned as `relative`
- when sticky element top property smaller than 100px
  - positioned as `fixed` at `top: 100px`

> [sticky sidebar inside box](sticky-inside-box.md)

stick to the nearest **scrolling ancestor**

- scrolling ancestor is the nearest ancestor with scrolling mechanism
- scrolling ancestor is:
  - overflow is `hidden`, `auto`, `scroll`, `overlay`
    - note that with `overflow: hidden`, the element seems like relative to its ancestor
    - cause there is no scrollbar
  - have fixed height or width

[sticky and overflow](css-sticky-and-overflow.md)

## positioned element

positioned element is the element that property `position` value is:

- [relative](#position-relative)
- [absolute](#position-absolute)
- [fixed](#position-fixed)
- [sticky](#position:-sticky)

which is not `static`

## Positioning Contexts

## Property align

`vertical-align` property available values

- baseline
- top
- middle
- bottom
- sub
- text-top

