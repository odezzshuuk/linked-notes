# WegGL API uniform

## what for

- specify values of [uniform](webgl-data-in-webgl.md#uniform) variable

## syntax

`uniform[1234][fi][v](location, value)`

- for `uniform2fv(location, value)`
- the letter at the end of the function name
  - f: v0, v1 are float values
  - v: for array values
- parameter
  - `location`: the location of the uniform variable
  - `value`: is an array of float values

