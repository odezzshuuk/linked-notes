# CSS - Property Display

## What Is This

decide inside and outer display type of an element

- [outer type](#outer-display-type) decide element is [block box](css-box-model-sorted.md) or [inline box](css-box-model-sorted.md)
- [inner type](#inside-display-type) control children element layout

## Outer Display Type

Set element **outer** display type

- `block`: generate a [block box](css-box-model-sorted.md#block-box), tag `h1`-`h6`, `p`, `div` are default block
- `inline`: generate an [inline box](css-box-model-sorted.md), tag `span`, `a`, `b`, `i`, `u`, `s` are default inline
- `inline-block`: equilavent to `display: inline flow-root`

## Inside Display Type

Set element **inner** display type

- `flow`: Element's content will apply [flow layout](css-normal-flow.md)(block and inline layout)
- `flow-root`: create new [BFC](css-block-formatting-context.md), define root position 
- `table`: create an implicit table inside element
- `flex`: [flex layout](css-flex.md)
- `grid`: [grid layout](css-grid.md)
- ruby

set inner element display type 

- `table-cell`: element behavior similar to `<td>` tag, create [BFC](css-block-formatting-context.md)

## Element Visibility

> compare with [visibility](css-visibility.md)

- `none`: **remove** element from [normal flow](css-normal-flow.md)

