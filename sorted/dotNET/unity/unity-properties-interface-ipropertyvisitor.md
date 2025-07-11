## Unity Properties - Interface IPropertyvisitor

## Method to override 

- `IPropertyVisitor.Visitor<Container, TValue>(Property<TConatiner, TValue> property, ref TContainer container)`

## Simple Implementation

```cs
void IPropertyVisitor.Visit<TContainer, TValue>(Property<TContainer, TValue> property, ref TContainer container)
{
    Debug.Log($"Visiting property: {property.Name} on container type {typeof(TContainer).Name}");
}
```

where this method be called

- Inside `Property.Accept(propertyVisitor, ref container)` method body

## Write Property Visitor

- To write property visitor with `IPropertyVisitor` interface, you need cooperate with [`IPropertyBagVisitor`](unity-properties-propertybag#interface-ipropertybagvisitor) interface

## Custom Specific Type Property Visitor Operation

- cause `IPropertyAdapter`

work with [mark interface](tag-interface.md)



