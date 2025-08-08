# Modularized CSS

- Module selectors are composed of a single class name
- **Descendant selectors** are prohibited in modular CSS, because using descendant selectors:
  - Increases CSS coupling
  - Increases specificity, which may require further specificity increases for future modifications
  - Poor reusability, not convenient to use in other locations

## Using modifiers to represent different module states

> Such as message--error

```css
.message {
    padding: 0.8em 1.2em;
    border-radius: 0.2em;
    border: 1px solid #265559;
    color: #265559;
    background-color: #e0f0f2;
}

.message--success {
    color: #2f5926;
    border-color: #2f5926;
    background-color: #cfe8c9;
}

.message--warnig {
    color: #594826;
    border-color: #594826;
    background-color: #e8dec9;
}

.message--error {
    color: #592626;
    border-color: #592626;
    background-color: #e8c9cf;
}
```

- Add both the main module name and the modifier class name to the element

```html
<div class="message message--error">
    Invalid email address
</div>
```

## Multi-element modules

- Class names start with the module name, separated by `__`, followed by the sub-element name


```css
.media {
    padding: 1.5em;
    background-color: #eee;
    border-radius: 0.5em;
}
.media::after {
    content: "";
    display: block;
    clear: both;
}
.media__image {
    float: left;
    margin-right: 1.5em;
}
.media__body {
    overflow: auto;
    margin-top: 0;
}
.media__body > h4 {
    margin-top: 0;
}
```