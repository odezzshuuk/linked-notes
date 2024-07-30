# CSS - Box Properties

- [Feature](#feature)
- [Content](#content)
- [padding](#padding)
- [border](#border)
- [margin](#margin)

## Feature

- Those properties in [block box](css-box-model-sorted.md#block-box) are repected
- but partially repected in [inline block](css-box-model-sorted.md#inline-block)

## Content

width, height

- cannot be negative
- value type
  - united number: specify the size directly, like `width: 100px;`
  - percentage: percent based on [containing block](css-containing-block.md)

max-width, max-height, min-width, min-height

- if the content of the container is mutable, the size of the element will change accordingly, min/max can limit the range of the element's adjustment
- Values
  - max-content:
  - min-content:
  - `<percentage>`:


## padding

- padding
  - `padding: 20px 10px;`: top/bottom, left/right
  - `padding: 1px 2px 3px 4px;`: top, right, bottom, left

## border

## margin

[Margin Collapsing](css-mastering-margin-collapsing.md)

