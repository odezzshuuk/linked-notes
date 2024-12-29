# CSharp - LINQ

## What Is LINQ


```cs
int[] numbers = {2, 5, 28};

IEnumerable<int> lowNums = from n in numbers
                           where n < 20
                           select n;
```

Query Syntax

```cs
var numQuery = from n in numbers
               where n < 20
               select n;
```

LINQ Method

```cs
var numCount = numbers.Where(x => x < 20); 
```

[anonymous type](csharp-anonymous-types.md)

[query variable](csharp-linq-variable.md)

[expression structure](csharp-linq-expression.md)

[LINQ API](csharp-linq-standard-api.md)


