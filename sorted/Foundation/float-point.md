# Floating Point

## Binary Encoding Format for Floating Point Numbers

$$
(-1)^s \times 1.f \times 2^{e-1023}
$$

- float type: s=1 bit sign, e=8 bits exponent, f=23 bits significand 
- double type: s=1 bit sign, e=11 bits exponent, f=52 bits significand 
  - For the exponent, the first bit represents the sign, the exponent can represent the range -1024 ~ 1024 
  - 0 ~ 1023 represents negative numbers, 1024 ~ 2048 represents positive numbers

Taking `float f = 624.424` as an example

- Binary encoding: `1 00010000 0111000001101100100011`

***

- Real numbers can be represented in the form: $d_md_{m-1}...d_1d_0d_{-1}d_{-2}...d_{-n}$
- A decimal real number d can be represented as: $d = \sum_{i=-n}^m10^i \times d_i$
- A binary real number d can be represented as: $d = \sum_{i=-n}^m2^i \times d_i$
- $0.111111_2$ represents $\frac {63}{64}$
- The decimal number $12.34_{10}$ can be represented as: $1\times10^{1}+2\times10^{0}+3\times10^{-1}+4\times10^{-2}=12\frac{34}{100}$
- Considering only finite-length encoding, numbers like $\frac{1}{3}$, $\frac{5}{7}$ cannot be accurately represented
- Similarly, binary representation can only represent numbers that can be written as $x \times 2^y$, other values can only be approximated
- IEEE floating-point standard uses $V=(-1)^s \times M \times 2^E$ to represent a number
  - s=1 represents negative, s=0 represents positive
  - The significand M is a binary fraction
  - The exponent E is a power of 2
- The bits of a floating-point number are divided into three fields
  - 1 bit sign s
  - k bits to store the exponent E
  - n bits fraction field to store M
  - Single precision: $k=8, n=23$
  - Double precision: $k=11, n=52$
- $11100.101_2=0.11100101\times2^{101}$
- $11100.101$ normalized as $1.1100101\times2^{100}$
  - s=0
  - M=1.1100101
  - E=100
  