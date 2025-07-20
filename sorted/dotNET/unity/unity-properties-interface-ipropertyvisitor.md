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

- Cause `IVisitPropertyAdapter` incapable with `IPropertyVisitor` interface
- To add custom operation for specific type of property, you can use marker interface

work with [marker interface](tag-interface.md)

```cs
public class DumpObjectVisitor
    : IPropertyBagVisitor
    , IPropertyVisitor
    , IPrintValue<Vector2>
    , IPrintValue<Color>
{
    public IPrintValue Adapter { get; set; }
        
    public DumpObjectVisitor()
    {
        // For simplicity
        Adapter = this;
    }
    void IPropertyVisitor.Visit<TContainer, TValue>(Property<TContainer, TValue> property, ref TContainer container)
    {
        // Here, we need to manually extract the value.
        var value = property.GetValue(ref container);
        
        var propertyName = GetPropertyName(property);
        
        // We can still use adapters, but we must manually dispatch the calls. 
        if (Adapter is IPrintValue<TValue> adapter)  // TValue is the type of the property value
        {
            var context = new PrintContext(m_Builder, Indent, propertyName);
            adapter.PrintValue(context, value);
            return;
        }
            
        // Fallback behaviour here 
    }
        
    void IPrintValue<Vector2>.PrintValue(in PrintContext context, Vector2 value)
    {
        context.Print(value);
    }
    void IPrintValue<Color>.PrintValue(in PrintContext context, Color value)
    {
        const string format = "F3";
        var formatProvider = CultureInfo.InvariantCulture.NumberFormat;
        context.Print(typeof(Color), $"RGBA({value.r.ToString(format, formatProvider)}, {value.g.ToString(format, formatProvider)}, {value.b.ToString(format, formatProvider)}, {value.a.ToString(format, formatProvider)})");
    }
}
```



