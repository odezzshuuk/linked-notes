# `@media`

- [what is this](#what-is-this)
- [take a quick look](#take-a-quick-look)
- [media query](#media-query)

## what is this

- used to define styles for different **devices** and **screen sizes**

syntax

```css
@media media-type and (media-feature: value){
  /* styles */
}
```

- `media-type` and `media-feature` together called [**media query**](#media-query)
- media-query-list looks like: `media-type and (media-feature: value)`

## take a quick look

apply style `.container { width: 600px; }` when the screen width is greater than 600px

```css
@media screen and (min-width: 600px) {
  .container {
    width: 600px;
  }
}
```

apply style `.container { width: 600px; }` when the screen width is **not** greater than 600px

```css
@media not all and (min-width: 600px) {
  .container {
    width: 600px;
  }
}
```

## media query

- query to test if a device **matches** a set of [media features](css-media-feature.md)

> for example:
> test if the device screen width is greater than 600px
> test device support hover operate
> test the number of bits per color component of the output device

- composed of optional **media type** and **media features**
- logical operators can be used to compose a complex feature

media type

- value can be chosen
  - all: Suitable for all devices
  - print: viewed on a screen in **print preview** mode
  - screen: for screens primarily
- default value is `all`
- when use logical operator `not` or `only`, must specify a media type

media features

[media feature](css-media-feature.md)

logical operators

- `and`: combine two or more media features
- `not`: negate a [media query](#media-query)
  - must specify a [media type](#media-type)
  - if separate by comma, `not` only negate to which it is applied
- `only`:

