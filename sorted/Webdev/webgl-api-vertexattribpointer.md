# WebGL API vertexAttribPointer()

## What's for

- bind the buffer currently bound to gl.ARRAY_BUFFER to a vertex [attribute](webgl-data-in-webgl.md#attribute)

## Syntax

```js
vertexAttribPointer(
  index,
  size,
  type,
  normalized,
  stride,
  offset
)
```

- `index`: the index of the vertex attibute
  - an available value is returned by [getAttribLocation()](webgl-api-getattriblocation.md)
- `size`: vertex attribute size
  - must be 1, 2, 3, 4
- `type`: data type of each component in the array
  - possible values:
    - `gl.BYTE`: signed 8-bit integer, with values in [-128, 127]
    - `gl.SHORT`: signed 16-bit integer, with values in [-32768, 32767]
    - `gl.UNSIGNED_BYTE`: unsigned 8-bit integer, with values in [0, 255]
    - `gl.UNSIGNED_SHORT`: unsigned 16-bit integer, with values in [0, 65535]
    - `gl.FLOAT`: 32-bit floating point number
- `normalized`: a boolean specifying whether integer data values should be normalized into certain range
- `stride`: pace between consecutive vertex attributes
- `offset`: offset bytes of the first component in the vertex attribute array
  - must be a multiple of the size of the data type