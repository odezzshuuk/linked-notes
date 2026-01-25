# WebGL Fundamentals

* [What is WebGL](#what-is-webgl)
* [WebGL Context](#webgl-context)
* [vec4](#vec4)
* [GLSL](#glsl)
* [vertex](#vertex)
* [fragment](#fragment)
* [clip space](#clip-space)
* [shader](#shader)
* [WebGL Constants](#webgl-constants)
* [WebGL Types](#webgl-types)
* [uniform](#uniform)

## What is WebGL

- WebGL only care two things
  - clip space, (1, 1) to (-1, -1), (0, 0) is the center
  - colors

## WebGL Context

to gert WebGL context

- call `getContext` on canvas

## vec4

`(x, y, z, w)`

- `(x, y, z)` is the position in Cartesian coordinate system
- w represent the depth in of 3d Space

(x, y, z, w) in Homogeneous coordinate convert to (x', y', z') in Cartesian coordinate

```
x = x'/w
y = y'/w
z = z'/w
```

## GLSL

- GL Shader Language
- strictly typed like C/C++

A pair of functions

1. [Vertex shader](#vertex)
2. [fragment shader](#fragment)

## vertex

- Compute the position of each vertex

## fragment

- Compute color of each pixel

## clip space

## shader

[shader](webgl-shader.md)

## WebGL Constants

- store the data that rendering pipeline needs
- can be pass to function or pass as variable
- all constants are type `GLenum`

why it's constant when the data is changing?

- Once the buffer is created, the memory location will not change

## WebGL Types

GLenum

GLboolean

GLbitfield

GLbyte

## uniform

- declared in [shader code](#shader-code)
- hold various types of data
  - floats
  - vectors
  - matrices
  - textures
  - ...
- called `uniform` is because they are **constant** for all [vertices](#vertex) and [fragments](fragment)

> similar to global variable in javascript

get uniform use WebGL api

```js
const gl = canvas.getContext('webgl');
gl.uniform1f();
```
