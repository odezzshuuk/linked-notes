# c++ - std_move

- Utility header file  
- Returns an [rvalue reference](c++-rvalue-reference.md) bound to an lvalue  
- After moving, the source object should not be used except for **assignment** or **destruction**  
- `move` does not reallocate memory  
- The source object after moving must be destructible

[`std_forward`](std-forward-function-template.md)

