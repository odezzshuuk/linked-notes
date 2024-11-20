# Computer Graphics - Clip Space

## Perspective Projection

$$
C =
\begin{bmatrix}
\frac{1}{\text{tan}(\frac{fov}{2}) \cdot \text{aspect}} & 0 & 0 & 0 \\
0 & \frac{1}{\text{tan}(\frac{fov}{2})} & 0 & 0 \\
0 & 0 & \frac{z_{far} + z_{near}}{z_{near} - z_{far}} & \frac{2 \cdot z_{far} \cdot z_{near}}{z_{near} - z_{far}} \\
0 & 0 & -1 & 0
\end{bmatrix}
$$

- $z_{near}$ and $z_{far}$ are the near and far clipping planes
- $fov$: the field of view in radians
- $aspect$: is the aspect ratio of the screen

## Orthographic Projection

$$
C_{\text{ortho}} =
\begin{bmatrix}
\frac{2}{r - l} & 0 & 0 & \frac{-(r + l)}{r - l} \\
0 & \frac{2}{t - b} & 0 & \frac{-(t + b)}{t - b} \\
0 & 0 & \frac{-2}{z_{far} - z_{near}} & \frac{-(z_{far} + z_{near})}{z_{far} - z_{near}} \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

- $r, l, t, b$ are the right, left, top, and bottom of the screen