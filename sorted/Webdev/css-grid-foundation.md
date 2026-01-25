# CSS Grid Foundation

* [feature](#feature)
* [declare grid container](#declare-grid-container)
* [set columns and rows](#set-columns-and-rows)
* [repeat()](#repeat())
* [fr unit](#fr-unit)
* [minmax()](#minmax())
* [cross row or column elements](#cross-row-or-column-elements)
* [Grid Gap](#grid-gap)

## Feature

- elements in grid can overlap
- **inline direction**: left to right(main direction)
- **block direction**: downward(cross direction)

## declare grid container

- `display: grid;`

## set columns and rows

- `grid-template-columns`: define grid number of columns and width of each column
- `grid-template-rows`: define grid number of rows and height of each row

```css
.wrapper {
  display: grid;
  grid-template-columns: 100px 100px 100px;
}
```

- `.wrapper` is a grid container with 3 columns, each column width is 100px

## repeat()

when there are many columns, use repeat() to simplify code

- `repeat(3, 100px)` equal to `100px 100px 100px`

## fr unit

- fr is a unit, has the similar effect with [flex-grow](css-flex.md#flex-grow)
- According to available space distribute space by proportion
- A flexible size
- Can be mixed used with absolute unit(px)

## minmax()

`minmax(min, max)`

- when grid size is auto, minmax() can set min width and max width

```css
.wrapper {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-rows: minmax(100px, auto);
}
```

- row height: 100px ~ auto

## cross row or column elements

- `grid-column-start`: start column
- `grid-column-end`: end column
- `grid-row-start`: start row
- `grid-row-end`: end row

```css
.box1 {
  grid-column-start: 1;
  grid-column-end: 4;
  grid-row-start: 1;
  grid-row-end: 3;
}
```

## Grid Gap

- `grid-column-gap`: column gap
- `grid-row-gap`: row gap

