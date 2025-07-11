# Unity Properties - Best Practices

```cs
// Create the following methods to encapsulate the formatting of the message and display the value.
public readonly struct PrintContext
{
    private StringBuilder Builder { get; }
    private string Prefix { get; }
    public string PropertyName { get; }

    public void Print<T>(T value)
    {
        Builder.AppendLine($"{Prefix}- {PropertyName} = {{{TypeUtility.GetTypeDisplayName(value?.GetType() ?? typeof(T))}}} {value}");
    }
        
    public void Print(Type type, string value)
    {
        Builder.AppendLine($"{Prefix}- {PropertyName} = {{{TypeUtility.GetTypeDisplayName(type)}}} {value}");
    }

    public PrintContext(StringBuilder builder, string prefix, string propertyName)
    {
        Builder = builder;
        Prefix = prefix;
        PropertyName = propertyName;
    }
}

public interface IPrintValue
{
}

public interface IPrintValue<in T> : IPrintValue
{
    void PrintValue(in PrintContext context, T value);
}

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
        if (Adapter is IPrintValue<TValue> adapter)
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
