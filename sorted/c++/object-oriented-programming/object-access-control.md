# Object Access Control

- Appearance: `class Pub_Derv : public Base {}`
- The **access specifier of the derived class** has no effect on whether the **members and friends of the derived class** can access the members of its direct base class.
- The **access specifier of the derived class** controls the access rights of the <font color="red">**object (instance) of the derived class**</font> to the members of the base class.
- The **access specifier of the derived class** also continues to control the **downstream** derived classes of the derived class.
- `public`
- `private` means that the public members in the base class are private to the **object of the derived class**.
- `protected` means that the public members in the base class are [protected](member-access-control.md) to the **derived class and friend objects**.
