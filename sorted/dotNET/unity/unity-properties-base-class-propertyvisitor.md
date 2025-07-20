# Unity Properties - Base Class PropertyVisitor

## Which interfaces PropertyVsitor implements

- [`IPropertyVisitor`](#interface-ipropertyvisitor)
- [`IPropertyBagVisitor`](unity-properties-propertybag.md#interface-ipropertybagvisitor)
- ...

## Method To Override

`VisitorProperty<TContainer, TValue>(Property<TContainer, TValue> property, ref TConatiner container, ref TValue value)`

- Type parameter `TContainer` is the type of `container` whose properties are being visited. 
- Type parameter `TValue` is the type of property value being visited. 

## Simple Implementation

```cs
protected override void VisitProperty<TContainer, TValue>(Property<TContainer, TValue> property, ref TContainer container, ref TValue value)
{
    Debug.Log($"Visiting property: {property.Name} with value: {value} on container type {typeof(TContainer).Name}");
}
```

## Custom Operation For Specific Type Property

Property Adapter

- In visitor design pattern, visitor has multiple override methods for each concrete type of [property](unity-properties-property.md)
- For above implementation, All visited properties do the same thing
- To Add Custom Operation to specific type of [property](unity-properties-property.md)
- That's What property adapter does

Features Of Property Adapter

- Can Only be used along with `PropertyVisitor` class
- Not work with [`IPropertyVisitor`]() interface

How to

- Implement `IVisitPropertyAdapter<TProperty>` interface, `TProperty` is the concrete type of property you want to adapt
- Call `AddAdapter(this)` to register adapters

Take A Look

```cs
public class DumpObjectVisitor
    : PropertyVisitor
    , IVisitPropertyAdapter<Vector2>
    , IVisitPropertyAdapter<Color>
{

    public DumpObjectVisitor()
    {
        AddAdapter(this);  //  add self as an adapter
    }
    
    protected override void VisitProperty<TContainer, TValue>(Property<TContainer, TValue> property, ref TContainer container, ref TValue value)
    {
        // ...
    }

    public void VisitProperty(ref Vector2 container, ref Vector2 value)
    {
        Debug.Log($"Visiting Vector2 property with value: {value}");
    }

    public void VisitProperty(ref Color container, ref Color value)
    {
        Debug.Log($"Visiting Color property with value: {value}");
    }
}
```

