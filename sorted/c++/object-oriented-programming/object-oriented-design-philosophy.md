## Object-Oriented Design Philosophy

- **Regular users** write code to use objects of a class.
- **Class designers** are responsible for writing the members and friends of a class.
- The parts of a base class that are intended to be used by derived classes should be declared as `protected`, which are inaccessible to regular users.
- The `private` members of a base class are also inaccessible to **derived classes** and **friends of derived classes**.
- The interface of a base class should be declared as `public`.
- A base class should divide the **parts implemented by itself** into two types:
  - Accessible to derived classes, declared as `protected`.
  - Accessible only by the base class and its friends, declared as `private`.
- Use `struct` for public inheritance and `class` for private inheritance; this is just a convention to increase readability, and there is no difference between the two.
