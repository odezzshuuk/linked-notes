# Unity Properties - PropertyContainer

## What's This

- A class with utility static methods to operate on data containers using properties

## Important Methods

`PropertyContainer.Accept(IPropertyVisitor visitor, ref TContainer container, ref PropertyPath path, ref VisitParameters parameters)`

basic use case

```cs
public class ExampleObject { }
ExampleObject obj = new ExampleObject();
PropertyContainer.Accept(visitor, ref obj)
```

- visitor: [IPropertyVisitor](unity-properties-propertyvisitor)
- container: the object whose properties will be visited

## Static methods

- `Accept`
- `GetProperty`
- `GetValue`
- `IsPathValid`
- `SetValue`
- `TryAccept`
- `TryGetProperty`
- `TryGetValue`
- `TrySetValue`
