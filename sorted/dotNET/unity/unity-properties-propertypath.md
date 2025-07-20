# Unity Properties - Property Path

## What's This

- string that describe the location of a property withwin a container object

## What's For

- Get or set the data of an object at a specific path
- Accept a visitor on a sub-property of an object

## Create a Property Path

- Using Constructor

```cs
PropertyPath path = new("foo.bar.baz[2]");
```

- Using API

```cs
PropertyPath path = PropertyPath.FromName("foo");
path = path.AppendName(path, "bar");
path = path.AppendName(path, "baz");
path = path.AppendIndex(path, 2);
```

## Parsing a Property Path

For a property path `"foo.bar.baz[2]"`

- 2nd element of `baz` list container in `bar` property of `foo` sub-container which is a property of container to be visited

```cs
public class ExampleData {
    public Foo foo;
}
public class Foo {
  public Bar bar;
}

public class Bar {
   public baz[] baz = {
         new Baz { Value = "First" },
         new Baz { Value = "Second" },
         new Baz { Value = "Third" }
   }
}

public class Baz {
    public string Value;
}

public class Program{
    public void Execute() {
        PropertyPath path = PropertyPath.FromName("foo");
        path = path.AppendName(path, "bar");
        path = path.AppendName(path, "baz");
        path = path.AppendIndex(path, 2);

        var exampleData = new ExampleData();
        PropertyContainer.Accept(visitor, ref new ExampleData(), path);
    }
}
```

