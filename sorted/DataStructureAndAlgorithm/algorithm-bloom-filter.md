# Bloom Filter

A Bloom filter is a space-efficient probabilistic data structure that is used to test whether an element is a member of a set.

- **False Positives**: It may have a certain false positive rate, meaning it might incorrectly identify an element as being in the set when it is not.

## Bit Array

- Each position in the array is a single bit.
- The length of the bit array determines the size of the filter.

## Principle

1.  **Mapping Elements**: To add an element, it is hashed by several random hash functions. The positions in the bit array corresponding to the resulting hash values are set to 1.
2.  **Checking for Existence**: To check if an element exists, it is hashed by the same hash functions.
    - If all the corresponding positions in the bit array are 1, the element **most likely** exists.
    - If any of the corresponding positions is 0, the element **definitely** does not exist.

## False Positive Rate

The formula for the false positive rate is:

$p \approx (1 - e^{(-kn/m)})^k$

- **k**: Number of hash functions
- **n**: Number of elements in the set
- **m**: Length of the bit array

## Determining Filter Size and Hash Functions

- **Length of the Bit Array**: To achieve a desired false positive rate (`p`), the required length of the bit array (`m`) can be calculated as:

  $m = -\frac{n \cdot \ln(p)}{(\ln(2))^2}$

- **Number of Hash Functions**: The optimal number of hash functions (`k`) can be calculated as:

  $k = \frac{m}{n} \cdot \ln(2)$