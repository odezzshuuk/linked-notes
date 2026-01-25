# CSS box shadow

## what is this

- adds shadow effects around an element's frame

```css
.info {
  box-shadow: 10px 10px 5px red;
}
```

## feature

- takes the same rounded of element border

## syntax

can take 2, 3, 4 values

- if 2: `offset-x` `offset-y`
- if 3: `offset-x` `offset-y` `blur-radius`
  - `<blur-radius>` is the blur look
- if 4: `offset-x` `offset-y` `blur-radius` `spread-radius`
  - if `<spread-radius>` is 0, the shadow will be the same size as the element

optionally values

- `inset`: shadow inside the frame

```css
.info {
  box-shadow: 10px 10px 5px red inset;
}
```

> display the content as if it were debossed(凹入) inside the box

- `color`: shadow color

```css
.info {
  box-shadow: 10px 10px 5px red inset, 0 0 5px blue;
}
```
