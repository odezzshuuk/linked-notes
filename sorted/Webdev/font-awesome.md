# Font Awesome

## What It Is

- 是一个图标字体库，包括图标字体、CSS框架、LESS/SASS源文件、Web字体文件、SVG矢量图标、PNG图像等。
- inline元素, 使用`<i>`和`<span>`标签

```html
<body>
    <i class="fa fa-home"></i>
    <i class="fa fa-home fa-2x"></i>
</body>
```

## How To Use

### HTML页面

- 在HTML页面中引入Font Awesome的CSS文件
> 不需要安装或下载

```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
```

### CSS文件

```css
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css');
```

### 在Vue中使用

[official tutorial](https://fontawesome.com/docs/web/use-with/vue/)


- 添加SVG core: `npm install --save @fortawesome/fontawesome-svg-core`
- 添加Icon Packages
  - `npm install --save @fortawesome/free-solid-svg-icons`
  - `npm install --save @fortawesome/free-regular-svg-icons`
  - `npm install --save @fortawesome/free-brands-svg-icons`
- 添加Pro Icon Packages
  - `npm install --save @fortawesome/pro-solid-svg-icons`
  - `npm install --save @fortawesome/pro-regular-svg-icons`
  - `npm install --save @fortawesome/pro-light-svg-icons`
  - `npm install --save @fortawesome/pro-thin-svg-icons`
  - `npm install --save @fortawesome/pro-duotone-svg-icons`
  - `npm install --save @fortawesome/sharp-solid-svg-icons`

添加library

```js
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAewsomeIcon } from '@fortawesome/vue-fontawesome'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
library.add(faUserSecret)
Vue.component('font-awesome-icon', FontAwesomeIcon)
```

在组件中使用

```html
<template>
    <div id="app">
        <font-awesome-icon icon="fa-solid fa-user-secret" />
    </div>
</template>
```

- fa-solid: 图标外观
- fa-user-secret: 图标内容

## Animating Icons

```html
<div class="fa-3x">
    <i class="fa fa-circle-plus fa-beat"></i>
</div>
```
