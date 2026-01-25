# CSS Learn From Proplem

## 1. text auto wrap at space

problem description

1. a react component define a `text` props, type is string, when pass a value with spaces in it.
2. the space in the value will auto become line break when display in the page.

here is the code

- a tooltip component
- style by tailwindcss

```js
const Tooltip = ({ children, text }) => {
  const [showTooltip, setShowTooltip] = React.useState(false);

  return (
    <div className="relative inline-block">
      <button
        onMouseEnter={() => setShowTooltip(true)}
        onMouseLeave={() => setShowTooltip(false)}
      >
        {children}
      </button>
      {showTooltip && (
        <div className="absolute top-full left-1/2 transform -translate-x-1/2 mt-2 p-2 rounded-md bg-gray-800 text-white text-center">
          <span>{text}</span>
          <div className="absolute bottom-full left-1/2 transform -translate-x-1/2 translate-y-1/2 w-4 h-4 rotate-45 bg-gray-800"></div>
        </div>
      )}
    </div>
  );
};

export default Tooltip;
```

analysis:

- because size of `absolute` position element will restrict by its container block
- when next word is too long, it will wrap to adapt the width of container block

## 2. overflow inside a flex item

> not inside a flex container

description

when

`.container` style is `display: flex`

`.content` style is `overflow: auto`

the content will overflow the container, the scroll-x bar will show. And with .container style `display: block`, the scroll-x bar will not show.

- index.html

```html
<div class="container">
  <div class="box">
    <div class="content">
      The item is sized according to its width and height
      <br/>
      properties.
      <br/>
      It shrinks to its minimum size to      fit the container, but does not grow to absorb any extra free space in the flex container. This is equivalent to setting "flex: 0 1 auto".
      auto
    </div>
  </div>
</div>
```

- style.css

```css
.container {
  display: flex;
}

.content {
  overflow: auto
}
```

solution

- set `.box` style `overflow: auto`

```css
.box {
  overflow: auto;
}
```

analysis

- flex container will make its children flex item
- and a flex item size try to adapt its content size
- so style the flex item with [`overflow: auto`](css-overflow.md#overflow-property) to add scroll bar for the content
