# Copy Constructor

- Used to perform copy initialization, such as `string s1 = s2;`.
- The parameter of the copy constructor must be a reference type.
  - Because the process of passing a **non-reference type parameter** to a formal parameter is the process of **calling the copy constructor**.
- Situations where copy initialization occurs:
  - Passing an object as an argument to a non-reference type parameter.
  - Returning an object from a function with a non-reference return type.
  - Initializing elements in an array or members in an aggregate class with a braced list.
  - Adding elements to a container.
