# Java - Catch block

- Captured `Exception`
- Every catch block is an exception handler

## Catch Multiple Exceptions

- Exception with inheritance relationship can be caught: `catch(IOException | SQLException e)`

```java
catch (FileNotFoundException | UnknownHostException e) {
    logger.log(Level.WARNING, "File not found or unknown host", e);
}
```

- Exception with no inheritance relationship can be caught in multiple catch blocks

## Rethrow Exception

```java
catch(SQLException e) 
{
    throw new ServletException("database error: " + e.getMessage());
}
```

## Chained Exception

-

```java
public class ChainedExceptionDemo {
    public static void main(String[] args) {
        try {
            method1();
        } catch(Exception ex) {
            ex.printStackTrace();
        }
    }
    public static void method1() throws Exception {
        try {
            method2();
        } catch (Exception ex) {
            throw new Exception("New info from method1", ex);
        }
    }
    public static void method2() throws Exception {
        throw new Exception("New info from method2");
    }
}
```

## Set the original exception as the cause of the new exception

```java
catch {
    Throwable se = new ServletException("database error");
    se.initCause(e);
    throw se;
}
```

use `getCause()` to get the original exception

```java
Throwable e = se.getCause();
```

## Logging Exception

```java
catch {
    logger.log(level, message, e);
    throw e;
}
```
