# Java - Exception handler

## Exception Handling Process

1. Error program exit: When an error occurs in the program, no value will be returned and the method will exit through another path.
2. Throw exception: Throw an object encapsulating error information
3. Search: Starting from the wrong method, start from the top of the stack of the calling method, traverse the call stack, and search for an exception handler that can handle the program.
4. Matching type: An exception handler is considered appropriate if the type of the exception object thrown matches the type that the handler can handle.
5. Handling: When an appropriate handler is found, the runtime system passes the exception to the handler
6. Catch: The selected handler becomes the caught exception


## Try Block

- Contains one or more pieces of code that may throw exceptions
- If an exception is thrown in the try statement, the program will skip the remaining code in the try block
  - Therefore, it is usually not recommended to call the resource's close() method in the try block

## Catch Block

[Catch Block](java-exception-catch-block.md)

## Finally Block

- will be executed after try block exits
- Executed even an exception is raised

> finally block is more suitable for executing `close()` method of resource

- try block is allowed to only have finally block without catch block
- return value in finally block will override return value in try block

## Use try...with block handle resource

[try...with block](java-try-with-resources.md)
