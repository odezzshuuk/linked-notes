# LaTex - Math

* [Symbol](#symbol)
* [Space](#space)
* [Overbrace](#overbrace)
* [Aligned](#aligned)
* [Brace](#brace)
* [Matrix](#matrix)
* [Sqrt](#sqrt)
* [Trigonometry Functions](#trigonometry-functions)

## Symbol

- `^`: upper index
- `&`: column jump in math
- `_`: foot label
- `$`: math environment delimiter

## Space

- `\;`: 4/18 quad
- `\:`: 3/18 quad
- `\,`: 2/18 quad
- `\hspace{5mm}`: horizontal space

## Overbrace

$f(x)=a_nx^n+a_{n-1}$

$$
z = \overbrace{
   \underbrace{x}_\text{real} + i
   \underbrace{y}_\text{imaginary}
  }^\text{complex number}\tag{1}
$$

## Aligned

$$
\begin{aligned}
B'&=-\partial \times E,\\         % use & to specify the alignment position
E'&=\partial \times B - 4\pi j,
\end{aligned}
$$

## Brace

$$
f(x)=\left\{          % represent curly brackets
\begin{aligned}
x & = & \cos(t) \\
y & = & \sin(t) \\
z & = & \frac xy
\end{aligned}
\right.
$$

$$
\begin{aligned}
 \left.\begin{aligned}
        B'&=-\partial \times E,\\         % use & to specify the alignment position
        E'&=\partial \times B - 4\pi j,
       \end{aligned}
 \right\}
 \qquad \text{Maxwell's equations}
\end{aligned}
$$

## Matrix

parentheses matrix

$$
\begin{pmatrix}
a & b \\[2mm]
c & d
\end{pmatrix}
$$

- `[2mm]`: line space

brackets

$$
\begin{bmatrix}
a & b \\[1mm]
c & d
\end{bmatrix}
$$

inline matrix

- inline matrix here $\begin{pmatrix} a & b \\[1mm] c & d \end{pmatrix}$
- anther one $\begin{bmatrix} a & b \\[1mm] c & d \end{bmatrix}$

## Sqrt

$$
C = \sqrt{a^2+b^2}
$$

## Trigonometry Functions

relation shape between a, b in lab color and h in lch color

$$
h^\degree = \arctan(\frac{b}{a})
$$

