# CSharp - try...catch...finally

## One Word

- Try block includes code that is protected from exceptions
- catch statement
  - handle the exception
  - can have multiple catch blocks
- finally block will always be executed at any case

## catch statement

```c#
catch
{
    Statements
}
```

match any type of exception

```c#
catch(Exception Type)
{
    Statements
}
```


```c#
catch(Exception e)
{
    Statements
}
```

## finally

- Always execute, even if there is a return statement in the try block

