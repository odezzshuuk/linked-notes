# WebGL Texture

## set image texture

[code](webgl-boilerplate.md#image-processing)

## variable u_image

- u_image is default to use unit o
- calling `gl.bindTexture()` will auto bind to u_image

the following code to set [uniform](webgl-api-uniform.md) value is not necessary

- because u_image is default to use unit 0

```js
const u_imageLoc = gl.getUniformLocation(program, 'u_image');
gl.uniform1i(u_imageLoc, 0);
```

