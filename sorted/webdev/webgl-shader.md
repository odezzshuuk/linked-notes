# WebGL - Shader

* [what it is](#what-it-is)
* [shader function](#shader-function)
* [Instance Method](#instance-method)
* [webgl shader code](#webgl-shader-code)

## What It Is

- A program
- Written using the [GLSL](webgl-fundamentals.md)
- containing the information about
  - vertices that make up a shape
  - generate the data needed to render the pixels on the screen
    - position of pixels
    - color of pixels

## Shader Function

- vertex shader function
- fragment shader function
- compile on cpu
- execute on gpu

vertex function

- `gl_Position`
  - type: [`vec4`](webgl-fundamentals.md#vec4), (x, y, z, w)
  - a special variable that vertex transfromed add saving it in
  - represent the position of a vertex in [clip space]()
  - range: `[1, -1]`

```js
const vsSource = `
  attribute vec4 aVertexposition;
  uniform mat4 uModelViewMatrix;
  uniform mat4 uProjectionMatrix;
  void main() {
    gl_Position = uProjectionMatrix * uModelViewmatrix * aVertexPosition;
  }
`;
```

- `aVertexPosition`, `uModeViewMatrix`, `uProjectionMatrix` are variables
- `vec4` represent the variable type is 4-component vector, `(x, y, z, w)`
- `mat4` represent the variable type is 4x4 matrix
- this code transform a vertex by multiplying two 4x4 matrix

Fragment Shader

- compute the color of each pixel
- the value storing in `gl_FragColor` variable is drawn on the screen

```js
const fsSource = `
  void main() {
    gl_FragColor = vec4(1.0, 1.0, 1.0, 1.0)
  }
`
```

- this just drawing a white square

## Instance Method

`gl.createShader(type)`

- type: `gl.VERTEX_SHADER` or `gl.FRAGMENT_SHADER`
- return a shader object

## Webgl Shader Code

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Hello WebGL</title>
    <style>
      canvas {
        width: 100%;
        height: 100%;
        display: block;
      }
    </style>
  </head>
  <body>
    <canvas id="canvas"></canvas>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gl-matrix/2.8.1/gl-matrix-min.js"></script>
    <script>
      // Get the canvas element and WebGL rendering context
      const canvas = document.getElementById('canvas');
      const gl = canvas.getContext('webgl');

      // Define the vertex shader code
      const vertexShaderCode = `
        attribute vec3 position;
        void main() {
          gl_Position = vec4(position, 1.0);
        }
      `;

      // Define the fragment shader code
      const fragmentShaderCode = `
        precision mediump float;
        uniform vec4 color;
        void main() {
          gl_FragColor = color;
        }
      `;

      // Create the vertex shader
      const vertexShader = gl.createShader(gl.VERTEX_SHADER);
      gl.shaderSource(vertexShader, vertexShaderCode);
      gl.compileShader(vertexShader);

      // Create the fragment shader
      const fragmentShader = gl.createShader(gl.FRAGMENT_SHADER);
      gl.shaderSource(fragmentShader, fragmentShaderCode);
      gl.compileShader(fragmentShader);

      // Create the shader program
      const shaderProgram = gl.createProgram();
      gl.attachShader(shaderProgram, vertexShader);
      gl.attachShader(shaderProgram, fragmentShader);
      gl.linkProgram(shaderProgram);

      // Define the vertex data
      const vertices = [
        0.0, 0.5, 0.0,
        -0.5, -0.5, 0.0,
        0.5, -0.5, 0.0
      ];

      // Create the vertex buffer
      const vertexBuffer = gl.createBuffer();
      gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
      gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vertices), gl.STATIC_DRAW);

      // Enable the position attribute in the shader program
      const positionAttribute = gl.getAttribLocation(shaderProgram, 'position');
      gl.enableVertexAttribArray(positionAttribute);
      gl.vertexAttribPointer(positionAttribute, 3, gl.FLOAT, false, 0, 0);

      // Set the uniform color variable
      const colorLocation = gl.getUniformLocation(shaderProgram, 'color');
      gl.uniform4f(colorLocation, 1.0, 0.0, 0.0, 1.0);

      // Clear the canvas and render the triangle
      gl.clearColor(0.0, 0.0, 0.0, 1.0);
      gl.clear(gl.COLOR_BUFFER_BIT);
      gl.useProgram(shaderProgram);
      gl.drawArrays(gl.TRIANGLES, 0, 3);
    </script>
  </body>
</html>
```
