# 浮动

- 浮动元素是指元素的float属性不为none
- 脱离[normal flow](css-normal-flow.md)
- 向左侧或右侧浮动, 允许浮动元素被text和inline元素包围
- 元素是如何浮动
  1. 脱离normal flow
  2. 移动到[container]的边界或其他浮动元素的边界
- float使用块布局, 某些情况下会修改display的值
- 如果浮动元素高度比段落文字高，则下一段会直接从上一段开始

```html
<div class="media">
    <h4>Media heading</h4>
    <p> Lorem ipsum dolor sit amet, consectetur adipisicing elit.  Quisquam, quae.  </p>
    <p> Lorem ipsum dolor sit amet, consectetur adipisicing elit.  Quisquam, quae.  </p>
</div>
<div class="media">
    <h4>Media heading</h4>
    <p> Lorem ipsum dolor sit amet, consectetur adipisicing elit.  Quisquam, quae.  </p>
</div>
<div class="media">
    <h4>Media heading</h4>
    <p> Lorem ipsum dolor sit amet, consectetur adipisicing elit.  Quisquam, quae.  </p>
</div>
<div class="media">
    <h4>Media heading</h4>
    <p> Lorem ipsum dolor sit amet, consectetur adipisicing elit.  Quisquam, quae.  </p>
</div>
```

```css
.media {
    float: left;
    width: 40%;
    margin: 1.5em;
    background-color: #333;
    border-radius: 0.5em;
}
```

## clear属性

- 指定元素的哪一侧不允许由浮动元素
- 取值:
  - left: 左侧不允许有左浮动元素
  - right: 右侧不允许有右浮动元素
  - both
  - none