# Java Annotation

- [Introduction](#introduction)
- [Custom Annotation](#custom-annotation)
- [Use Annotation](#use-annotation)
- [Built-in Annotation](#built-in-annotation)
- [Annotation Interface](#annotation-interface)

## Introduction

- Annotations are labels in the source code.
- The compiler generates the same virtual machine instructions for code with and without annotations.

## Custom Annotation

[Custom Annotation](java-custom-annotation-type.md)

## Use Annotation

- Can be used in declarations of classes, fields, methods.

```java
@ClassPreamble(
    author = "John Doe",
    date = "01/01/2017",
    reviewers = {"Alice", "Bob", "Charlie"}
)
public class Generation3List {
    // ...
}
```

Using a single-value annotation:

- You can omit `value=`.

```java
@Copyright("2017")
public class Generation3List {
    // ...
}
```

## Built-in Annotation

Normal Built-in Annotation:

- `@Deprecated`
- `@Override`
- `@FunctionalInterface`: Used to mark a [functional interface](java-functional-interface.md).
- `@SuppressWarnings`
- `@SafeVarargs`

Annotations applied to other annotations, also called meta-annotations:

- `@Retention`
  - `RetentionPolicy.SOURCE`: Annotations not included in the class file.
  - `RetentionPolicy.CLASS`: Annotations included in the class file, but the virtual machine does not need to load them.
  - `RetentionPolicy.RUNTIME`: Annotations included in the class file and loaded by the virtual machine, **accessible via reflection**.
- `@Repeatable`: Allows the same annotation to be used multiple times on the same element.
- `@Documented`: Elements using this should be documented by Javadoc tools.
- `@Target`: Restricts the elements to which the annotation can be applied.
- `@Inherited`: The annotation type is automatically inherited.
  - When searching for an annotation of this type, if it is not found in the current class, it will be searched for in its superclass.
  - The search process continues up the inheritance chain **until it is found** or **reaches Object**.

## Annotation Interface

[Interface Annotation](java-interface-annotation.md)
