# Grid

- [Foundation](#foundation)
- [flexible number of tracks(rows, columns)](#flexible-number-of-tracksrows-columns)
- [Grid And Absolutely Positioned Elements](#grid-and-absolutely-positioned-elements)
- [](#)

## Foundation

[Grid Foundation](css-grid-foundation.md)

## Flexible number of tracks(rows, columns)

- use `auto-fit` and `minmax()` in `repeat()` function to implment flexible number of tracks

```css
.wrapper {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
}
```

- unit `fr`: a fraction of the available space in the grid container

## Grid And Absolutely Positioned Elements

grid container as an absolute positioned element [containing block](css-containing-block.md)

- give a grid item `position: absolute`

```css
.wrapper {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: 200px;
  gap: 20px;
  position: relative;
}

.box3 {
  grid-column-start: 2;
  grid-column-end: 4;
  grid-row-start: 1;
  grid-row-end: 3;
  position: absolute;
  top: 40px;
  left: 40px;
}
```

- box3 has taken out of the [flow](css-normal-flow.md), and not cause additional row
