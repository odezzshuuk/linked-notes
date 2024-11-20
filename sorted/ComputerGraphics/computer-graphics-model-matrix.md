# Compute Graphics - Model Matrix

Matrix

$$
\mathbf{M} =
\begin{bmatrix}
s_x r_{xx} & s_y r_{yx} & s_z r_{zx} & t_x \\
s_x r_{xy} & s_y r_{yy} & s_z r_{zy} & t_y \\
s_x r_{xz} & s_y r_{yz} & s_z r_{zz} & t_z \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

- `s`: scale
- `r`: rotation
- `t`: translation, represent the position
- `[0, 0, 0, 1]` is for transform in [Homogeneous Coordinates](#homogeneous-coordinates)

Dissociate the matrix into 3 parts

- Position-only

$$
\begin{bmatrix}
1 & 0 & 0 & t_x \\
0 & 1 & 0 & t_y \\
0 & 0 & 1 & t_z \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

- Rotation-only Matrix

$$
\begin{bmatrix}
r_{xx} & r_{yx} & r_{zx} & 0 \\
r_{xy} & r_{yy} & r_{zy} & 0 \\
r_{xz} & r_{yz} & r_{zz} & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

- Scale-only Matrix

$$
\begin{bmatrix}
s_x & 0 & 0 & 0 \\
0 & s_y & 0 & 0 \\
0 & 0 & s_z & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Perform A Transformation

$$
\begin{bmatrix}
x' \\[1mm]
y' \\[1mm]
z' \\[1mm]
1
\end{bmatrix}
=
\begin{bmatrix}
s_x r_{xx} & s_y r_{yx} & s_z r_{zx} & t_x \\
s_x r_{xy} & s_y r_{yy} & s_z r_{zy} & t_y \\
s_x r_{xz} & s_y r_{yz} & s_z r_{zz} & t_z \\
0 & 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
x \\[1mm]
y \\[1mm]
z \\[1mm]
1
\end{bmatrix}
$$
