# CSS Transform

- [What it is](#what-it-is)
- [feature](#feature)
- [transform function pass to transform properties](#transform-function-pass-to-transform-properties)
- [transform-box](#transform-box)
- [Cartesian Coordinates](#cartesian-coordinates)
- [Homogeneous Coordinates](#homogeneous-coordinates)
- [transform functions](#transform-functions)

## What it is

- rotate, scale, skew, translate an element
- geometric transformation, **not animation**

## feature

- if `transform: value` value different than none
  - a stack context is created
  - element behaves like a containing block with `position: fixed` or `position: absolute;`

## transform function pass to transform properties

> all followed function **can be used as individual property**, for example: `transform: rotate(90deg);`

rotate()

- `transform: rotateX(val);`: rotate around x axis
- values can be: 1 deg, 0.2turn, 3rad
  - `transform: rotateX(90deg);`
  - `transform: rotateX(0.25turn);`
  - `transform: rotateX(3.142rad);`

translate()

> transform element more about element its self

- `transform: translate(x, y)`: translate on 2D plane
- `transform: translateX(20px)`: translate on $(x, y)$ to $(x + 20px, y)$
- `transform: translateX(20%)`: 20% is relative to the size [transform box](#transform-box)
  - percentage value is **different** from `left, right, top, bottom` in [positioning](css-positioning.md)
  - `positioning` is relative to the [**containing block**](css-containing-block.md)

> can't instead `top`, `left`, `bottom`, `right` in position property like `fixed`, `absolute`

`scale()`

- `transform: scale(val)`: scale on 2D plane

`matrix()`: transformation matrix

- `matrix(a, b, c, d, tx, ty)`

`perspective()`: (perspective)

- use for 3D transform

## transform-box

- `transform-box: content-box`: content box is used as the reference box
- `transform-box: border-box`: border box is used
- `transform-box: fill-box`: default, object bounding box is used as reference box
- `transform-box: stroke-box`:
- `transform-box: view-box`: the nearest SVG viewport is used as reference box

## Cartesian Coordinates

- `(0, 0)` represents the top-left conrner of any element
- down and right are positive

## Homogeneous Coordinates

- `(x, y, z)` are the coordinates of the point

## transform functions

use 2 $\times$ 2 to describe a linear transformation

- `x, y` are the coordinates of the point
- `a, b, c, d` are the transformation parameters

```tex
$$
\begin{pmatrix}
a & c \\
b & d
\end{pmatrix}
\begin{pmatrix}
x \\ y
\end{pmatrix}
=
\begin{pmatrix}
ax + cy \\
bx + dy
\end{pmatrix}
$$
```

apply several transformation

```
$$
\begin{pmatrix}
a_1 & c_1 \\
b_1 & d_1
\end{pmatrix}
\begin{pmatrix}
a_2 & c_2 \\
b_2 & d_2
\end{pmatrix}
=
\begin{pmatrix}
a_1a_2 + c_1b_2 & a_1c_2 + c_1d_2 \\
b_1a_2 + d_1b_2 & b_1c_2 + d_1d_2
\end{pmatrix}
$$
```

with this, it is posible to describe most common transformations: rotations, scaling or skewing

