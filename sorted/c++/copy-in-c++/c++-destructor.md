# Destructor

- Objects within a class created through [[direct memory management]] require special attention from the destructor.
- Format: `~Foo() {}`
- Releases the resources used by the object.

> After an explicit declaration, a definition must be provided.

***

- No return value.
- Does not take parameters.
- Therefore, it cannot be overloaded.

***

- The destructor destroys members in the reverse order of their initialization.

Situations where the destructor is called automatically:

- A variable goes out of scope.
- When an object is destroyed, its members are destroyed.
- For a container (whether a standard library container or an array), its elements are destroyed.
- For a dynamically allocated object, it is destroyed when the `delete` operator is applied to a pointer to it.
- For a temporary object, it is destroyed when the expression that created it ends.

