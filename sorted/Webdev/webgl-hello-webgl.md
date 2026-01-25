# Create A WebGL Hello World

* [Summary: Shader Program Structure](#summary-shader-program-structure)
* [Get WebGL Instance](#get-webgl-instance)
* [GLSL Code](#glsl-code)
* [USE GLSL Code To Create WebGL Shader](#use-glsl-code-to-create-webgl-shader)
* [sent code to shader](#sent-code-to-shader)
* [Compile Shader](#compile-shader)
* [Program](#program)
* [Use Program](#use-program)
* [Buffer](#buffer)
* [Buffer Data Pass To Attribute Position](#buffer-data-pass-to-attribute-position)
* [finally draw the triangle](#finally-draw-the-triangle)
* [Complete Code](#complete-code)
* [Use Uniform to Transform Position Value](#use-uniform-to-transform-position-value)
* [Use Uniform to Set Color](#use-uniform-to-set-color)

## Summary: Shader Program Structure

shader

- [create glsl code](#create-shader-glsl)
- [create shader instance](#create-webgl-shader-instance)
- [send code to shader](#sent-code-to-shader)

program:

- [Program](#program)
- [Use Program](#use-program)

drawing part

> position, color, data pass to buffer
> drawing method take data from buffer and draw

- [Buffer](#buffer)
- [Locate Attribute Position](#locate-attribute-position)
- [Enable Attribute](#enable-attribute)
- [Take Data From Buffer](#take-data-from-buffer)

uniform

## Get WebGL Instance

```js
const canvas = document.getElementById('canvas');
const gl = canvas.getContext('webgl');
```

## GLSL Code

```js
const vertexShaderSource = `
  attribute vec2 a_position;
  void main() {
    gl_Position = vec4(a_position, 0, 1);
  }
`

const fragmentShaderSource = `
  precision mediump float;
  void main() {
    gl_FragColor = vec4(0, 1, 0.5, 1);
  }
`
```

## Create WebGL Shader Instance

create a [vertex shader]() **instance**

- it is an **empty shader**

```js
const vertexShader = gl.createShader(gl.VERTEX_SHADER);
```

create a [fragment shader]() **instance**

- it is an **empty shader**

```js
const fragmentShader = gl.createShader(gl.FRAGMENT_SHADER);
```

## sent code to shader

send [glsl code](webgl-fundamentals.md#glsl) to shader

```js
gl.shaderSource(vertexShader, vertexSource);
gl.shaderSource(fragmentShader, fragmentSource);
```

`source` is a string, represent the [glsl code](#glsl-code)

## Compile Shader

- once shader has [source code](#sent-code-to-shader)

```js
gl.compileShader(vertexShader);
gl.compileShader(fragmentShader);
```

Get Compile Status

- to check if shader compile successfully
- use [getShaderParameter method](webgl-api-getshaderparameter.md)
- compile result will be stored in `gl.COMPILE_STATUS`

```js
const res = gl.getShaderParameter(shader, gl.COMPILE_STATUS);
if (res) {
  alert( `
    error occur
    ${gl.getShaderInfoLog(shader)}
  `)
  gl.deleteShader(shader);
  return null;
}
```

> `shader` can be vertex shader or fragment shader
> `res` is the value of `gl.COMPILE_STATUS`

if compile failed

- `gl.COMPILE_STATUS` is `false`
- use `gl.getShaderInfoLog` get the log information
- then delete `shader`, return null

## Program

create program

```js
const program = gl.createProgram();
```

attach shader to program

```js
gl.attachShader(program, vertexShader);
gl.attachShader(program, fragmentShader);
```
link program

```js
gl.linkProgram(program);
```

## Use Program

```js
gl.clearColor(0, 0, 0, 0);
gl.clear(gl.COLOR_BUFFER_BIT);
gl.useProgram(program);
```

## Buffer

pass data to buffer

```js
const positions = [
  0, 0,
  0, 0.5,
  0.7, 0,
]
// Create Buffer to Store **vertex positions** data
const bf = gl.createBuffer();
// Bind Buffer To Target
bindBuffer(gl.ARRAY_BUFFER, bf);
gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(positions), gl.STATIC_DRAW);
```

- [gl.ARRAY_BUFFER](webgl-fundamentals.md#webgl-constants): is a kind of buffer

## Buffer Data Pass To Attribute Position

- after create [program](#program), we need supply data to it

```js
// locate attribute position
const positionAttributeLocation = gl.getAttribLocation(program, 'position');
// Enable Attribute
gl.enableVertexAttribArray(positionAttributeLocation);
gl.vertexAttribPointer(
  positionAttributeLocation, // index
  2,        // size
  gl.FLOAT, // type
  false,    // normalize
  0,        // stride
  0,        // offset
)
```

essentially three steps here

1. locate attribute position, look up the location of the [attribute](webgl-data-in-webgl.md#attribute)
2. attribute cannot be used until it is enabled
3. bind buffer to [attribute](webgl-data-in-webgl.md#attribute) in the [GSLS Code](#glsl-code)

## finally draw the triangle

```js
gl.drawArrays(gl.TRIANGLES, 0, 3);
```

## Complete Code

html

```html
<style>
  #canvas {
    width: 640px;
    height: 480px;
  }
</style>
<canvas id="canvas"><canvas>
```

js

```js
const vertexShaderSource = `
  attribute vec2 a_position;
  void main() {
    gl_Position = vec4(a_position, 0, 1);
  }
`
const fragmentShaderSource = `
  precision mediump float;
  void main() {
    gl_FragColor = vec4(0, 1, 0.5, 1);
  }
`

function createShader(gl, type, source) {

  const shader = gl.createShader(type);
  gl.shaderSource(shader, source);
  gl.compileShader(shader);
  const success = gl.getShaderParameter(shader, gl.COMPILE_STATUS);
  if (success) {
    return shader;
  }
  console.log(gl.getShaderInfoLog(shader));
  gl.deleteShader(shader);
}

const vertexShader = createShader(gl, gl.VERTEX_SHADER, vertexShaderSource);
const fragmentShader = createShader(gl, gl.FRAGMENT_SHADER, fragmentShaderSource)

function createProgram(gl, vertexShader, fragmentShader) {

  const program = gl.createProgram();

  gl.attachShader(program, vertexShader);
  gl.attachShader(program, fragmentShader);
  gl.linkProgram(program);
  const success = gl.getProgramParameter(program, gl.LINK_STATUS);
  if (success) {
    return program;
  }
  console.log(gl.getProgramInfoLog(program));
  gl.deleteProgram(program);
}

const program = createProgram(gl, vertexShader, fragmentShader);

//
gl.clearColor(0, 0, 0, 0);
gl.clear(gl.COLOR_BUFFER_BIT);
gl.useProgram(program);
gl.viewport(0, 0, gl.canvas.width, gl.canvas.height);

// program data
const positions = [
  0, 0.7,
  0.5, -0.7,
  -0.5, -0.7,
];

const positionBuffer = gl.createBuffer();
gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(positions), gl.STATIC_DRAW);

const positionAttributeLocation = gl.getAttribLocation(program, "a_position");
gl.enableVertexAttribArray(positionAttributeLocation);
gl.vertexAttribPointer(
  positionAttributeLocation,
  2,         // 2 components per itertaion
  gl.FLOAT,  // the data is 32bit floats
  false,     // don't normalize the data
  0,         // 0 = move forward size * sizeof(type) each iteration to get the next position
  0,         // start at the beginning of the buffer
)

gl.drawArrays(gl.TRIANGLES, 0, 3);
```

## Use Uniform to Transform Position Value

- for webgl, it's drawing space is from -1 to 1
- if you want to supply pixel value, use [uniform](webgl-fundamentals.md#uniform) to transform

add uniform type variable in vertex shader

> use `uniform` variable represent the resolution of canvas

```js
const vertexSource = `
  attribute vec4 a_position;
  uniform vec2 u_resolution;  // add uniform
  void main() {
    vec2 zeroToOne = a_position.xy / u_resolution;
    vec2 zeroToTwo = zeroToOne * 2.0;
    vec2 clipSpace = zeroToTwo - 1.0;
    gl_Position = vec4(clipSpace * vec2(1, -1), 0, 1);
  }
`
```

get uniform location and pass data to uniform

```js
// get uniform location
const resolutionUniformLocation = gl.getUniformLocation(program, 'u_resolution');
// pass data to uniform
gl.uniform2f(resolutionUniformLocation, gl.canvas.width, gl.canvas.height);
```

## Use Uniform to Set Color

add uniform type variable in fragment shader

```js
const fragmentSource = `
  precision mediump float;
  uniform vec4 u_color; // add uniform
  void main() {
    gl_FragColor = u_color;
  }
`
```

get uniform location and pass data to uniform

```js
const colorUniformLocation = gl.getUniformLocation(program, 'u_color');
// set random color
gl.uniform4f(colorUniformLocation,
  Math.random(),
  Math.random(),
  Math.random(),
  1
);
```
