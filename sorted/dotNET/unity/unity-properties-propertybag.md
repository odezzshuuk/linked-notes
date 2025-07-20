# Unity properties - PropertyBag

## What's this

- Properties collection of .Net object
- Untiy uses reflection to generate property bag for a type, once per type
- Determining how to traverse operation that [structured object](design-pattern-visitor#structured-object) role does in [visitor design pattern](design-pattern-visitor)
- Is a companion object for given type

## Features

- **Unity Generate** for given type
- Property bag with corresponding type together form the [structured object]() role in visitor design pattern

## Interface IPropertyBagVisitor

Method to override 

- `Visit<TContainer>(PropertyBag<TContainer> propertyBag, ref TContainer container)`
- Type parameter `TContainer` is the type of `container` whose properties are being visited. 
- Parameter 
  - `propertyBag`: has a method `GetProperties(ref container)` to get [iterator]() of [`IProperty<TContainer>`](unity-properties-property.md)

Simple Implementation:

```cs
public class ExampleAttribute : Attribute { }
public class ExamplePropertyVisitor : IPropertyBagVisitor, IPropertyVisitor {
    protected override void IPropertyBagVisitor.Visit<TContainer>(IPropertyBag<TContainer> propertyBag, ref TContainer container) {
        foreach (var property in propertyBag.GetProperties(ref container))
        {
            if (property.HasAttribute<ExampleAttribute>())
            {
                // do something
            }
            property.Accept(this, ref container);
        }
    }
}
```

Where this method be called:

- Inside `PropertyContainer.Accept(propertyBagVisitor, ref container)` method body
  - who play the [structured object](design-pattern-visitor#structured-object) role in visitor design pattern

## Unity generating property for which C# member 

- public field
- private or internal field tagged with `[SerializeField]`, `[SerializeReference]`, or `[CreateProperty]`
- public, private, or internal C# property tagged with `[CreateProperty]`

> Doesn't generate a property for `[DontCreateProperty]`
