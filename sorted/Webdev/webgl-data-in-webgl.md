# Data in WebGL

## GLSL Variable

three kinds of variables

- attributes: store color, texture coordinates
- varyings
- uniforms

```c
attribute vec4 vColor;
void main() {
  attribute vec4 aVertexposition;
  uniform mat4 uModelViewMatrix;
  uniform mat4 uProjectionMatrix;
  void main() {
    gl_Position = uProjectionMatrix * uModelViewmatrix * aVertexPosition;
  }
}
```

- attribute:aVertexPosition
- uniform: uModelViewMatrix, uProjectionMatrix

## attribute

## uniform

- provide values that will be the **same for everything** drawn in the frame

## varying

- declared by vertex shader
- used to pass data to fragment shader