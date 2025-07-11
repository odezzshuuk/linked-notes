# Unity - Property Visitor

## Summary

> Use visitor design pattern to visit properties of a .Net object

Roles of each class corresponding to the visitor design pattern

- [Visitors](design-pattern-visitor#visitor)
  - class that implement `IPropertyVisitor` interface
  - class that inherits from base class `PropertyVisitor`
- [Elements](design-pattern-visitor#element)
  - [Properties](unity-properties-property) generate from c# members by reflection in Unity
- [Structured Object](design-pattern-visitor#structured-object): functions of structured object is seperated into 2 parts
  - [Property bag](unity-properties-propertybag) responsible for storing and traversing properties of a type
  - [Property container]() has `Accept` method to accept a visitor

[Best Practices](unity-properties-best-practices)

## Glossarys

[Property Bag](unity-properties-propertybag.md)

[Property Visitor](unity-properties-propertyvisitor.md)

[Property Container](unity-properties-propertycontainer.md)

[Unity Object Property](unity-properties-property.md)


### Property Path

- string that describe the location of a property withwin a container object

## Container Object
