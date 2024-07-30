# CSS - Mastering Margin Collapsing

> Only happens in [block-level](css-box-model-sorted.md) elements

## scene 1: 2 vertical adjacent elements

- only keep the largest margin

## scene 2: Parent and first/last child

Conditions:

1. parent element's margin-top and first child, or parent element's margin-bottom and last child
2. 没有分开父元素与后代元素的margin-top
  - 没有创建[BFC](css-block-formatting-context.md)或没有[clear]()
  - 父元素没有border, padding, 没有inline内容,
3. 没有分开父元素与后代元素的margin-bottom
  - 父元素没有border, padding, 没有inline内容,
  - 没有设置height, min-height, max-height

## scene 3: Empty Element

- 空元素没有设置border, padding, height, min-height, max-height, inline内容, 或clear-fix, 将不同block的margin-top和margin-bottom分开
