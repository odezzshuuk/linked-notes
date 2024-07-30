# CSS Box Model

* [Standard Box Model](#standard-box-model)
* [Box Property](#box-property)
* [Block And Inline](#block-and-inline)
* [display property](#display-property)
* [Visibility Property](#visibility-property)
* [Alternative Model of Box Model](#alternative-model-of-box-model)
* [Margin Collapsing](#margin-collapsing)

## Standard Box Model

- box-sizing: content-box
- every element in CSS is a box

layer relationship

> margin: extending the border with **blank area**
>> border: extension from padding
>>> padding: extending from content area
>>>> content area: restrict content area

```css
.box {
    width: 350px;
    height: 150px;
    margin: 10px;
    padding: 25px;
    border: 5px solid black;
}
```

> real size of the box
> wide: 350 + 25 + 25 + 5 + 5
> high: 150 + 25 + 25 + 5 + 5

- content area, padding, border make up the visible area of the box model

> background works on content and padding

## Box Property

[Property Of Box Model](css-box-model-properties.md)

## Block And Inline

[Block Box And Inline Box](css-box-model-sorted.md)

## Display Property

[display property](css-display.md)

## Visibility Property

[visibility property](css-visibility.md)

## Alternative Model of Box Model

- set `box-sizing: border-box;`
  - `width`, `height` property is the visible width and height
  - border, padding will make content area smaller
- width = border + padding + content width
- height = border + padding + content height

Put this code at the beginning of css file is a common practice

```css
*, ::before, ::after {
    box-sizing: border-box;
}
```

or

```css
:root {
    box-sizing: border-box;
}
*,
::before, ::after {
    box-sizing: inherit;
}
```
> ::after, ::before is [pseudo-element](css-selector.md#pseudo-element-selector)

## Margin Collapsing

[Margin Collapsing](css-mastering-margin-collapsing.md)
