# XSS

- XSS: Cross Site Scripting
- A type of code injection

a xss happenned when convert markdown to html

```md
this is a regular paragraph

<table>
  <tr>
    <td>Foo</td>
  </tr>
</table>

// milicious paragraph
<script>alert('hi')</script>
```

## method to mitigate it

XSS filter
