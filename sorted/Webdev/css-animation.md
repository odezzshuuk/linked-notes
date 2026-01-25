# Animation

* [Animation Property](#animation-property)
* [keyframes](#keyframes)
* [Create An Animation](#create-an-animation)

## Animation Property

`animation` property is **shorthand** for:

- 1. `animation-name`
- 2. `animation-duration`
- 3. `animation-timing-function`
- 4. `animation-delay`
- 5. `animation-iteration-count`
- 6. `animation-direction`
- 7. `animation-fill-mode`
- 8. `animation-play-state`

```css
p {
  animation-duration: 3s;
  animation-name: slidein;
  animation-iteration-count: infinite;
  animation-direction: alternate;
}
```

replace by

```css
p {
  animation: 3s infinite alternate slidein;
}
```

if value is time value, like 0.5s, 2s. Order of values is

- 1. first value: `animation-duration`
- 2. second value: `animation-delay`

order of other values

- recommended specify animation-name as the last value

## keyframes

```css
@keyframes animationName {
  from {
    property: value;
  }
  to {
    property: value;
  }
}
```

- `animationName`: relate to `animation-name` property value

```css
@keyframes animationName {
  0% {
    top: 0;
    left: 0;
  }
  33.33% {
    top: 50px;
  }
  66.66% {
    left: 50px;
  }
  100 {
    top: 100%;
    left: 100%;
  }
}
```

## Create An Animation

index.html

```html
<link rel="stylesheet" href="style.css" />
<body>
  <div class="block">hello animation</div>
</body>
```

style.css

```css
.block {
  animation-duration: 3s;
  animation-name: slidein;
  animation-iteration-count: infinite;
  background-color: #900;
}

@keyframes slidein {

  from {
    margin-top: 100%;
    width: 30%;
  }

  to {
    margin-left: 0%;
    width: 100%;
  }
}
```