# Preventing Copying

- A `delete` function is a function that, although declared, cannot be used in any way.
- Add **=delete** after the **parameter list** of the function to indicate that we want to define it as deleted.
- For example, the **iostream** class prevents copying.
- Copying is prevented by defining the **copy constructor** and **copy assignment operator** as **delete** functions.
- If the destructor is defined as `delete`, then the member cannot be destroyed.
- For some classes, the compiler-synthesized default constructor is defined as **delete**.
  - The ***destructor*** of a <u>class member</u> is deleted or inaccessible (e.g., private).
  - The ***copy constructor*** of a <u>class member</u> is deleted or inaccessible.
  - The ***copy assignment operator*** of a <u>class member</u> is deleted or inaccessible.
  - The <u>class has a reference member</u> without an in-class initializer, or a const member without an in-class initializer and its type does not explicitly define a default constructor.
  > Summary: If a class has a data member that cannot be default constructed, copied, assigned, or destroyed, the corresponding member function will be defined as deleted.
- private copy control
  - Declare and define a private copy constructor, which can be accessed by friends and member functions.
  - Declare but do not define a private copy constructor, which prevents any copy action and will cause compilation and linking errors.
