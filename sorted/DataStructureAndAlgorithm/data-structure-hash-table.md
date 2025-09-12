# Data Structure And Algorithm - Hash Table

## What It Is

- Hash is a transliteration from English, meaning scattering
- Uses a hash function to map keys to buckets
  - Inserting a new key: The hash function determines which bucket the key is assigned to
  - Searching for a key: Uses the hash function to map to the corresponding bucket, and only searches in that bucket

## Hash Function

- $hashFunction(key)$
- The return value is the hash address
- Selection of hash functions:
  - Direct addressing:
  - Digit analysis:
  - Division method: $hash(key) = key % P + b$, theory and practice show that p should be a prime number less than storage capacity
  - Mid-square method: k is the key, take the middle few digits of $k^2$ as the hash address, the number of digits can be determined by the table length, such as 1000, can take the middle three digits
  - Folding method:
  - The selection of hash functions is an open problem
- Collision: Different keys map to the same hash address

## Factors Determining Search Efficiency

- Whether the hash function is uniform
- Collision resolution method
- Number of elements vs. hash table length

## Resolving Collisions

- 1. Linear probing: $i$ is the address mapped by the key, when a collision occurs, check if $i+1$ is empty, if not, check $i+2$, and so on
- 2. Quadratic probing: Increments are $1^2, -1^2, 2^2, 2^2$
- 3. Rehashing: If hash function $H1(key)$ causes a collision, use $H2(key)$ to generate a new address, then $H3(key)$, $H4(key)$, until a non-colliding address is produced
- 4. Chaining: Use the hash address as a pointer to a **linked list**, if the hash table length is m, establish m empty linked lists
- 5. Establishing an overflow area