# CSS Transition

## Introduction

- A way to control animation speed when CSS property changed
- When css property changed, provide a gradual animation effect instead of changing immediately

## transition properties

shorthand properties: `transition: property duration timing-function delay;`

`transition-property`: CSS property to add transition effect

- `transition-property: prop1, prop2;`
  - transition effect applied to properties `prop1` and `prop2`
- `transition-property: all;`
  - transition effect apply on **all properties changing**
- `transition-property: none;`
  - no transition effect

`transition-duration`: duration of the transition effect

`transition-timing-function`: control animation speed at different points in time

- control animation speed by [bezier curve](math-bezier-curve.md) control points
- `transition-timing-function: linear;`: animation speed is constant during the animation
- `transition-timing-function: ease;`: slow at the beginning, then speed up, then slow down

`transition-delay`: delay before the transition effect

## create a transition

```css
.target {
  font-size: 14px;
  transition-property; font-size;
  transition-duration: 4s;
}

.target:hover {
  font-size: 20px;
}
```
