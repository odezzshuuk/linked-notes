# Copy Assignment Operator

- The copy assignment operator is declared as `Foo& operator= (const Foo&) {}`.
- It is a type of overloaded operator, essentially a function, with a return type of `Foo&`.
- It is used to perform assignment operations like `s1 = s2;`.
- It returns a reference to the left-hand operand: `return *this;`.
- The standard library usually requires types stored in containers to have an assignment operator.
- The synthesized copy assignment operator assigns each non-static member of the right-hand operand to the corresponding member of the left-hand operand.
- The copy assignment operator may be defined as delete in certain situations.
