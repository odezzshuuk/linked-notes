# Accessibility Restrictions on Derived-to-Base Conversion

- Only with public inheritance can **code that uses this class** use the derived-to-base conversion.
- Regardless of how the derived class inherits, the **member functions and [[friends]] of the derived class** can use the derived-to-base conversion.
- When a derived class inherits from a base class with public or protected inheritance, the **members and friends of the derived class's derived class** can use the derived-to-base conversion.
