# CSS - BFC

- BFC: Block formatting context

## When BFC is created

- [x] `<html>`, root element of document
- [x] float elements(float value is not `none`)
- [x] Absolutely positioned elements, `position: absolute or fixed`
- [x] Inline-block(display: inline-block)
- [ ] Table cells
- [ ] Table captions
- [ ] Anonymous table cells
- [ ] Block elements where the value of the [overflow](css-overflow.md) property is not visible or clip
- [ ] display value is flow-root
- [ ] contain value is layout, content, paint
- [ ] Grid elements (display is grid or inline-grid), if not a flex, grid, or table container itself
- [ ] Multi-column container value is not auto
- [ ] Elements with column-span value of all always create a new BFC, even if the element is wrapped in a multi-column container

## Create BFC For Positioning or Clearing Floats

### 1. contain internal floats

Set parent element property to:

```
{
    overflow: auto
    display: flow-root
}
```

> which means create a new BFC, make parent element out of Normal Flow

```html
<style>
.float {
    float: left;
    width: 200px;
    height: 100px;
    background-color: rgba(255, 255, 255, .5);
    border: 1px solid black;
    padding: 10px;
}

.box {
    background-color: rgb(224, 206, 247);
    border: 5px solod rebeccapurple
}
</style>
<section>
    <div class="box">
        <div class="float">I am a floated box!</div>
        <p>I am content inside the container.</p>
    </div>
</section>
```

### 2. Exclude external floats

```html
<style>
    section {
        height: 150px;
    }
    .box {
        background-color: rgb(224, 206, 247);
        border: 5px solid rebeccapurple;
    }
    .box[style] {
        background-color: aliceblue;
        border: 5px solid steelblue;
    }
    .float {
        float: left;
        overflow: hidden; /* required by resize:both */
        resize: both;
        margin-right: 25px;
        width: 200px;
        height: 100px;
        background-color: rgba(255, 255, 255, 0.75);
        border: 1px solid black;
        padding: 10px;
    }
</style>
<section>
    <div class="float">Try to resize this outer float</div>
    <div class="box"><p>Normal</p></div>
</section>
<section>
    <div class="float">Try to resize this outer float</div>
    <div class="box" style="display: flow-root">
        <p><code>display:flow-root</code></p>
        <p></p>
    </div>
</section>
```


### 3. Suppress margin collapsing


