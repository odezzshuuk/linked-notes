# CSS Alignment

* [Summary](#summary)
* [justify-content](#justify-content)
* [align-content](#align-content)
* [place-content](#place-content)
* [align-self](#align-self)
* [justify-self](#justify-self)
* [place-self](#place-self)
* [justify-items](#justify-items)
* [align-items](#align-items)
* [place-items](#place-items)

## Summary

treat all children as a single unit

1. [justify-content](#justify-content)
2. [align-content](#align-content)
3. [place-content](#place-content)

align single item in its area

1. [align-self](#align-self)
2. [justify-self](#justify-self): **INGORE** in flexbox and table cell layout
3. [place-self](#place-self)

default value for all [items](css-flex.md#what-is-this) inside a grid or flex container

1. [justify-items](#justify-items)
2. [align-items](#align-items)
3. [place-items](#place-items)

## justify-content

- define [`flex container`](css-flex.md#flex-container) content and space distribution along **main axis**
- define [`grid container`]() content and space distribution along [**inline direction**](css-grid-foundation.md#feature)

value

- `justify-content: flex-start;`: align at left, default value
- `justify-content: space-between;`: first item is flush with main-start edge, last item is flush with with the main-end edge

## align-content

- Describe the distribution of **all child elements as a whole** in the available space
- In flex box, describe the **main axis** distribution
- In grid container, describe the **distribution** when used area is **smaller** than the grid container

> if want attribute `align-content` take effect in grid container, requires grid container size is **larger than all content size**

[code](css-align.md)

## place-content

shorthand for

1. [justify-content](#justify-content)
2. [align-content](#align-content)

## align-self

- For **grid or flex** layout
- use to align **single item**
- override `align-items` value
- In flex box, aligns the item on the **cross axis**

value

- `align-self: stretch;`
- `align-self: center;`: at center
- `align-self: start;`: at start
- `align-self: end;`

## justify-self

- **ignored** in **flexbox** and **table cell** layout
- for **grid layout**, aligns an item inside its grid area along [inline axis](css-grid-foundation.md#feature)

value

- `justify-self: center`
- `justify-self: start`
- `justify-self: end`
- `justify-self: stretch`
  - for not sized items
  - still respecting the constraints of [max-width and max-height](css-box-model-properties.md#content)

## place-self

- shorthand for [align-self](#align-self) and [justify-self](#justify-self)

## justify-items

- define the default [justify-self](#justify-self) for all items of the box

## align-items

> influence direct children elements, not container self, not **other elements** either

- define the default [align-self](#align-self) for all items of the box
- describe the distribution of **child elements**
- in **flex container**, control the distribution of child elements in [**cross axis**](css-flex.md#cross-axis)
- in **grid container**, control the distribution of child element in grid

[code](css-align.md)

available values

- `align-items: stretch;`
- `align-items: start;`
- `align-items: end;`
- `align-items: center;`

---

- `align-items: flex-start`:
- `align-items: flex-end`

---

- `align-items:normal`: depends on the layout
  - in absolutly-positioned elements, it is `start`
  - in static position elements, it is `stretch`
  - flex items, it is `stretch`
- `align-items:
- `align-items:
- `align-items:
- `align-items:
- `align-items:

## place-items

- shorthand for [align-items](#align-items) and [justify-items](#justify-items)
