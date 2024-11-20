# Linear Algebra - Matrix

* [Matrix](#matrix)
* [Identity Matrix](#identity-matrix)
* [Transpose](#transpose)
* [Inversible Matrix](#inversible-matrix)
* [Row Equivalent](#row-equivalent)

## Matrix

$$
\begin{bmatrix}
1 & 9 & -13\\[1mm]
20 & 5 & -6\\[1mm]
\end{bmatrix}
$$

## Identity Matrix

$$
\begin{bmatrix}
1 & 0 & 0\\[1mm]
0 & 1 & 0\\[1mm]
0 & 0 & 1\\[1mm]
\end{bmatrix}
$$

concisely described

- $I_n = diag(1, 1, ..., 1)$

can also written using Kronecker delta

- $(I_n)_{ij} = \delta_{ij}$

properties

- $AI_n = I_nA = A$

rank

- $rank(I_n) = n$

## Transpose

matrix $A$

$$
\begin{bmatrix}
1 & 2 \\[1mm]
3 & 4 \\[1mm]
5 & 6 \\[1mm]
\end{bmatrix}
$$

matrix $A^T$

$$
\begin{bmatrix}
1 & 3 & 5 \\[1mm]
2 & 4 & 6 \\[1mm]
\end{bmatrix}
$$

some formula

- $A = (A^T)^T$

## Inversible Matrix

an n-by-n **square matrix** A is called invertible

if there exists an n-by-n matrix B such that

$AB = BA = I$

where $I$ is [identity matrix](#identity-matrix)

then `A` is called invertible, and `B` is called the inverse of `A`.

---

Properties

- A is row equivalent to $I_n$
- A is column equivalent to $I_n$

## Row Equivalent

- two matrices are **row equivalence** if one can be changed to the other by a sequence of elementary row operations

## Matrix Multiplication

- A is an $m \times n$ matrix
- B is an $n \times p$ matrix

$$
A =
\begin{pmatrix}
    a_{11} & a_{12} & \ldots & a_{1n} \\
    a_{21} & a_{22} & \ldots & a_{2n} \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{m1} & a_{m2} & \ldots & a_{mn}
\end{pmatrix}
\hspace{3mm}
B =
\begin{pmatrix}
    a_{11} & a_{12} & \ldots & a_{1n} \\
    a_{21} & a_{22} & \ldots & a_{2n} \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{m1} & a_{m2} & \ldots & a_{mn}
\end{pmatrix}
$$

- $C = AB$, C is define to be a $m \times p$ matrix

$$
c_{ij} = a_{i1}b_{1j} + a_{i2}b_{2j} + \ldots + a_{in}b_{nj} = \sum_{k=1}^n a_{ik}b_{kj}
$$

that is $c_{ij}$ is multiplying term-by-term the entries in the $i$th **row** of A with the $j$th **column** of B, and summing these $n$ products

