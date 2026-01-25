# function

## calc()

```css
input {
  width: calc(100% - 20px);
}
```

`width: 100% - 20px` is invalid

## attr()

get the value of an attribute

- for demo.html

```html
<blockquote cite="https://mozilla.org/en-US/about">
  <p>
    The Mozilla Foundation is a non-profit organization dedicated to keeping the
    Internet open and accessible to all.
  </p>
</blockquote>
<blockquote cite="https://web.dev/about/">
  <p>
    Google believes in an open, accessible, private, secure web
  </p>
</blockquote>
```

- demo.css

```css
blockquote {
  margin: 1em 0;
}
blockquote::before {
  display: block;
  content: "(source: " attr(cite) ")";
  color: hotpink
}
```