# Lexical Analysis

code: 

```
if (i == j)
    z = 0;
else 
    z = 1;
```

What the lexical analyzer sees:

`\tif (i == j)\n\t\tz = 0;\n\telse\n\t\tz = 1;`

## Token Class 

> For example: Identifier, Keywords, `()`

- Corresponds to a group of character strings
- Identifier: character strings starting with an English letter
- Integer: 0, 12, 001
- Keyword: if, else, begin
- WhiteSpace
- Token: `<class, string>`

The string "foo=42" in the source file is converted to Tokens:
`<Id, "foo">, <OP, "=">, <Int, "42">`

