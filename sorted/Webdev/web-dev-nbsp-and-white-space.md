# white space and &nbsp

## in one word

- `&nbsp;` is a useful where to create fixed-width

## `&nbsp;`

```html
<p>This&nbsp;&nbsp;&nbsp;is&nbsp;&nbsp;&nbsp;&nbsp;a&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;test</p>
```

output

```
This is      a        test
```

## white space

will be collapsed by [white-space](css-content.md#white-space)

```html
<p>This   is      a         test</p>
```

output

```
this is a test
```

