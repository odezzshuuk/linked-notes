# CSharp - Anonymous Types

```cs
new {FieldProp = InitExpr, FieldProp = InitExpr, ...};
```

## Cases that do not create a new anonymous type

When Compiler encounters another anonymous type with

- same parameter names
- same inferred types
- same order

