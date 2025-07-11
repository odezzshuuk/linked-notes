# Design Pattern - Visitor

## Features

## When To Use

- When you have a stable set of classes but need to perform varying operations on them
- Those operations depend on the concrete type of the element

## Components

- [Visitor](#visitor)
- [Element](#element)
- [Structured Object](#visiting-place)

## Visitor

Abstract

- Responsible for defining how to visit each [element](#element) type Where the operation logics are defined

How To Code

- Visit means this instance will be passed as argument to element
- Contains **multiple** overloaded `Visit` methods for each concrete [element](#element) type
  - `Visit(ElementA element)`
  - `Visit(ElementB element)`
  - ...

## Element

Abstract

- Base unit of the [structured object](#structured-object) to perform operations

How To Code

- Containing **one** method `Accept(IVisitor visitor)` to accept visitor
- Simplest implementation of Accept method

```cs
public void Accept(IVisitor visitor) {
    visitor.Visit(this);
}
```

## Structured Object

Abstract

- Where [visitor](#visitor) visit to 
- Consists of various [elements](#element)
- Has a stable structure

What this does

- A container that stores [elements](#element) and  methods that manage [elements](#element)
- Method that accept a visitor traverse [elements](#element) and call `Accept` method on each [element](#element)

## Example Code

```cs
public interface IDocumentVisitor {
  void Visit(TextElement text);
  void Visit(ImageElement image);
}

// Element interface
public interface IDocumentElement {
  void Accept(IDocumentVisitor visitor);
}

// Concrete Elements
public class TextElement : IDocumentElement {
  public string Content { get; }

  public TextElement(string content) {
    Content = content;
  }

  public void Accept(IDocumentVisitor visitor) {
    visitor.Visit(this);
  }
}

public class ImageElement : IDocumentElement {
  public string FilePath { get; }

  public ImageElement(string filePath) {
    FilePath = filePath;
  }

  public void Accept(IDocumentVisitor visitor) {
    visitor.Visit(this);
  }
}

// Concrete Visitor 1: Renders elements to console
public class RenderVisitor : IDocumentVisitor {
  public void Visit(TextElement text) {
    Console.WriteLine($"Rendering text: {text.Content}");
  }

  public void Visit(ImageElement image) {
    Console.WriteLine($"Rendering image from: {image.FilePath}");
  }
}

// Concrete Visitor 2: Exports elements to JSON
public class JsonExportVisitor : IDocumentVisitor {
  public void Visit(TextElement text) {
    Console.WriteLine($"Exporting text to JSON: {{ \"type\": \"text\", \"content\": \"{text.Content}\" }}");
  }

  public void Visit(ImageElement image) {
    Console.WriteLine($"Exporting image to JSON: {{ \"type\": \"image\", \"filePath\": \"{image.FilePath}\" }}");
  }
}

// Object Structure
public class Document {
  private readonly List<IDocumentElement> _elements = new List<IDocumentElement>();

  public void AddElement(IDocumentElement element) {
    _elements.Add(element);
  }

  public void Accept(IDocumentVisitor visitor) {
    foreach (var element in _elements) {
      element.Accept(visitor);
    }
  }
}

public class Program {
  public static void Main() {

    // Create document with elements
    var document = new Document();
    document.AddElement(new TextElement("Hello, Visitor!"));
    document.AddElement(new ImageElement("photo.jpg"));

    // Apply different visitors
    var renderVisitor = new RenderVisitor();
    var jsonVisitor = new JsonExportVisitor();

    Console.WriteLine("Rendering document:");
    document.Accept(renderVisitor);

    Console.WriteLine("\nExporting document to JSON:");
    document.Accept(jsonVisitor);
  }
}
```


