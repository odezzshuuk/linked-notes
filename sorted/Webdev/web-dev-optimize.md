# web dev optimization

## glossary

- layout: The process where the browser calculates geometric information for elements, size and location. This process is called reflow in Chrome, Opera, Safari, and is called layout in Firefox
- reflow: layout in Firefox

## Pipeline Shipping A Frame

Shipping a frame to screen order:

JS -> Style -> Layout -> Paint -> Composite

1. JS: js, css animation, web animation api
2. Style: css file
3. layout: width
4. paint: color, background
5. composite: layer

three changes pipeline

1. visual change: JS -> Style -> Layout -> Paint -> Composite
2. paint change: JS-> Style -> Paint -> Composite
3. composite change(layer change): JS -> Style -> Composite

## Avoid Forced Synchronous Layout

- **Synchronous Layout**: it is posible to for a browser to perform a layout earlier with js

optimize example

- some properties like offsetHeight, offsetWidth will trigger synchronous layout

```js
requestAnimationFrame(logBoxHeight);

function logBoxHeight() {
  box.classList.add('super-big');  // change style
  console.log(box.offsetHeight);
}
```

- get box.offsetHeight will trigger synchronous layout
- If you don't need to immediately get the box.offsetHeight after the style change, get it before re-layout

```js
console.log(box.offsetHeight);
box.classList.add('super-big');
```

## force reflow


