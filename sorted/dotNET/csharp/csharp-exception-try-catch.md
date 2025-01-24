# CSharp - try...catch...finally

## One Word

- Try block includes code that is protected from exceptions
- catch statement
  - handle the exception
  - can have multiple catch blocks
- finally block will always be executed at any case

## catch statement

Catch any exception but without any information

```cs
catch
{
    // Statements
}
```

Match exception type `SomeException`

```cs
catch(SomeException e)
{
    // Statements
}
```

## finally

- Always execute, even if there is a return statement in the try block

