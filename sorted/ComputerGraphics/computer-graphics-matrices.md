# Computer Graphic - Coordinates And Matrices

* [Homogeneous Coordinates](#homogeneous-coordinates)
* [Model/Transform Matrix](#modeltransform-matrix)
* [View/Camera Matrix](#viewcamera-matrix)
* [Clip/Projection Matrix](#clipprojection-matrix)
* [Normalized Device Coordinates](#normalized-device-coordinates)
* [Equation](#equation)

## Homogeneous Coordinates

- Also called projective coordinates
- This coordinates are used to describe objects(a point) itself

$$
\begin{bmatrix}
x \\[1mm]
y \\[1mm]
z \\[1mm]
w \\[1mm]
\end{bmatrix}
$$

- `w` for perspective projection

## Model/Transform Matrix

$M$: [Model Matrix Detail](computer-graphics-model-matrix.md)

What's For

- Transforming object in the [world space]()

## View/Camera Matrix

$V$: [View Matrix Detail](computer-graphics-view-matrix.md)

What's For

- Transforming the [world space]() to the [camera space]()

## Clip/Projection Matrix

$C$: [Clip Matrix](computer-graphics-clip-matrix.md)

For maps 3D coordinates to 2D coordinates

## Transformation Path

Convention

- $P_{model}$: The object matrix

Equation

$
P_{world} = M \times P_{model} \\[1mm]
P_{view} = V \times P_{world} \\[1mm]
P_{clip} = C \times P_{view}
$

## Normalized Device Coordinates

- The coordinates are in the range of $[-1, 1]$

Conversion from [Clip space] to **Normalized Device Coordinates**

$
x_{\text{NDC}} = \frac{x_{\text{clip}}}{w_{\text{clip}}}, \quad y_{\text{NDC}} = \frac{y_{\text{clip}}}{w_{\text{clip}}}, \quad z_{\text{NDC}} = \frac{z_{\text{clip}}}{w_{\text{clip}}}
$

[NDC](#normalized-device-coordinates) range

- $x_{\text{NDC}}, y_{\text{NDC}}, z_{NDC} \in [-1, 1]$

## Screen Space

Conversion from **NDC** to **Screen Space**

$
x_{\text{screen}} = \frac{(x_{\text{NDC}} + 1)}{2} \cdot \text{viewport width} \\[1mm]
y_{\text{screen}} = \frac{(y_{\text{NDC}} + 1)}{2} \cdot \text{viewport height}
$

