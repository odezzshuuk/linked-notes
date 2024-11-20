# Computer Graphics - View Matrix

How $V$(View Matrix) constructed

1. Example scenario

- Camera position `position = (3, 2, 5)`
- Camera look at `target = (0, 0, 0)`
- World space up vector `Worldup = (0, 1, 0)`

2. Carema Forward Vector

$$
forward = \frac{target - position}{||target - position||} = \frac{(0, 0, 0) - (3, 2, 5)}{(0-3)^2 + (0-2)^2 + (0-5)^2} =  \frac{(-3, -2, -5)}{\sqrt{38}} \\
$$

3. Camera Right Vector

$$
right = worldup \times forward
$$

why `worldup` can be used to calculate camera `right`?

- Cross product of two perpendicular vectors is a vector perpendicular to both
- And `worldup` is perpendicular to the camera `forward` vector

4. Camera Up Vector

$$
Cameraup = forward \times right
$$

5. Construct the view matrix

$$
V = 
\begin{bmatrix}
r_x & u_x & f_x & 0 \\[1mm]
r_y & u_y & f_y & 0 \\[1mm]
r_z & u_z & f_z & 0 \\[1mm]
0 & 0 & 0 & 1
\end{bmatrix}
$$
