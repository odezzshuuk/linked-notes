# Member Access Control

- `public int func(args) {}`
- `private`: **friends** and **base classes** can access, **derived classes** cannot.
- `protected`: **base classes**, **derived classes**, and **friends** can access.
  - Members or friends of a derived class can only access protected members of the base class through a derived class object.
- A `using` declaration can change the access rights of a **base class member**. The access rights of a **member changed by `using` in a derived class** are determined by the access control specifier before the `using` declaration.
