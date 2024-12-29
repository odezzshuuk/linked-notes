# CSS - Flex

* [what is this](#what-is-this)
* [Main Axis](#main-axis)
* [Cross Axis](#cross-axis)
* [flex Container](#flex-container)
* [flex Property](#flex-property)
* [flex-grow](#flex-grow)
* [Create Gap](#create-gap)
* [remaining space](#remaining-space)

## What Is This

- element set `display: flex` performance for outside like [**block box**](css-box-model-sorted.md#block-box)
- a kind of layout that arranges elements in a single dimension
- main axis: dimension that flex items are arranged in
- cross axis: dimension perpendicular to main axis
- **flex container**: element whose style attribute set to `display: flex`
- **flex item**: all elements in flex container called flex item

## Main Axis

- main axis: default is horizontal

`flex-direction: <value>;` set main axis direction, available value:

- `row`: horizontal distribution
- `row-reverse`: horizontal direction, reverse
- `column`: vertical distribution
- `column-reverse`: vertical direction, reverse 

## Cross Axis

- cross axis: default is vertical

## flex Container

property

- `flex-direction: row;`: set [main axis](#main-axis) direction, default value is `row`
- `flex-wrap: wrap;`: when content is too much, wrap to next line
- `flex-flow: row wrap;`: equivalent to set `flex-direction` and `flex-wrap` at same time
- `align-items: center`:

## flex Property

- set how **flex item** will grow

`flex` is shoothand for `flex-grow`, `flex-shrink`, `flex-basis`

- 1. `flex-grow: <number>`: ratio of how much of the **remaining space** should be assigned
  - default: 0
  - Nagative values are invalid
  - when number is positive, allow item to fill any available space
- 2. `flex-shrink`: when size of all flex items larger than containe, flex items will be shrinked
  - default: 1
  - when 0: the item will not shrink
- 3. `flex-basis`: initial main size of a flex item
  - basis value grow or shrink
  - default: auto
  - `flex: 0 0 300px` equilavent to create an inflixible item

may be specified using 1, 2, 3 values

- one-value
  - `flex: 2`: `flex 2 1 0`, means `flex: <flex-grow> 1 0`
  - `flex: 200px`: `flex 1 1 200px`, means `flex: 1 1 200px`
- two-value
  - fisrt must be `flex-grow``
  - number value with unit for `flex-shrink`
  - number value without unit for `flex-basis`
- three-value

```css
article {
    flex: 1 200px;
}

article:nth-of-type(3) {
    flex: 2 200px;
}
```

- flex item's minimum size is 200px, remaining space distribution by proportion


## flex-grow

set proportion of [remaining space](#remaining-space) distribution

```css
#one { flex-grow: 1 }
#two { flex-grow: 2 }
#thr { flex-grow: 3 }
```

- if without wrap, elements `one`, `two`, `three` occupy 1/6, 2/6, 3/6 respectively

## Create Gap

- margin
- negative margin on flex container

```css
#container {
    display: flex;
    margin: 10px;
}
```

## remaining space

