# CSS Containing Block

- Containing block mostly is the nearest **block-level** element in the ancestor, ~~not always parent element~~

## How to determine containing block

- if [positioned element's](css-positioning.md#positioned-element) containing block is nearest positioned ancestor
- if not containing block is the nearest block container

## Description in MDN

how to determine the containing block depends on the element's [position](css-positioning.md) property

> **meaning of containing block**: the size and position of an element are often affected by its containing block, such as width, height, padding, margin, and the position properties top, right, bottom, and left

if `position` value is `static, relative, sticky`

- 其包含块可能由最近的**ancester block**的内容区边缘组成
- 可能是一个block container
- 可能是新的[formatting context]()

如果position属性为`absolute`

- 包含块由最近的position不是static的祖先元素的padding边缘组成

如果position属性是`fixed`

- 在continuous media情况下, 包含块是viewport(窗口, 如浏览器窗口), 分页媒体是page area

如果position是`absolute`或`fixed`, 包含块可能由满足以下条件的最近父级元素的padding的边缘组成

- transform或perspective的值不为none
- will-change的值是transform或perspective
- filter的值不是none 或 will-change的值是filter
- contain的值是paint
