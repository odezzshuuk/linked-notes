# CSharp - IEnumerable Interface

## Features

One member `GetEnumerator`; 

- A method that returns an [IEnumerator](csharp-ienumerator.md)

## `IEnumerable<T>` And `IDisosable`

- `IEnumerable<T>` inherit [`IDisposable`](csharp-idisposable.md)

> by inherit `IDisposable` interface, the enumerator can hold resources like database connection, and can ensure that these resources are released after the enumeration ends (or stops midway)
