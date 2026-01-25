# WebGLRenderingContext

## What it is

- provides an interface to the OpenGL ES 2.0 rendering context
- think it as HTML [`<canvas>`](javascript-dom-canvas.md) element *context*

## Get Context

- call method `getContext()` on the `<canvas>` element
- and supplying `"webgl"` as the first argument

```js
const canvas = document.getElementById('canvas');
const glContext = canvas.getContext('webgl');
```

## Use Context Get Canvas Element Size

```js
const canvas = document.getElementById('canvas');
const glContext = canvas.getContext('webgl');
console.log(gl.drawingBufferWidth);  // 300
```
