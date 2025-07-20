# Classes that Act Like Values

- The copy and the original object are independent of each other.
- The **copy constructor** should copy the object pointed to by the pointer member, not the pointer itself.
- The **copy assignment operator** should release the object pointed to by the current pointer member and copy the object pointed to by the right-hand side pointer.
- Regarding the assignment operator:
  - If an object is assigned to itself, the assignment operator must work correctly.
  - Most assignment operators combine the work of a destructor and a copy constructor.
  - Recommended pattern:

  ```mermaid
  graph TD
  A[Copy the right-hand side operand into a local temporary object] --> B[Destroy the existing members of the left-hand side operand]
  B --> C[Copy the data from the temporary object to the members of the left-hand side operand]
  ```
