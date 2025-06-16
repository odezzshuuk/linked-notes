# Java - Checked And Unchecked Exceptions

## Checked Exception

- Other exceptions are called checked exceptions
- Must be handled, two ways to handle:
  - Declare the exception in the method
  - Call it within a try-catch block

## Unchecked Exception

- unchecked exception: Exception that inherit from [Error]() or [RuntimeException]()
- it is impossible to predict and recover from these errors in most cases
- can be catched, but it is not required to catch unchecked exception

> Runtime Exception: 
>> Designer believes that declaring Runtime exceptions does not significantly help program correctness
>> The level of information available to the Java compiler and the level of analysis performed by the compiler are usually insufficient to determine that such runtime exceptions will not occur

  
## When to declare checked exception

- Call a method that throws a checked exception
- An error is discovered during program execution
- An error occurs in the program
- An internal error occurs in the Java Virtual Machine and runtime library

