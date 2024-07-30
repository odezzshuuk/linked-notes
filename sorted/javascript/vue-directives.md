# Vue - Directive

## v-if

## v-else

## v-else-if

## v-for

- 基于数据渲染为多个元素
- 期望类型Array | Object | number | string | Iterable 

```html
<div v-for="item in items">{{item.text}}<div>
<div v-for="(item, index) in items"></div>`
<div v-for="(value, key) in object"></div>`
<div v-for="(value, name, value) in object"></div>
```

## v-on

- 绑定Vue对象中的methods属性中的函数
- 简写: `@event="funcName"`

## v-bind

> Attribute绑定

- 语法: `<div v-bind:id="dynamicId"></div>`
- 变量的值与属性绑定(例子中的div标签的id)
- 对于bool属性
  - 变量为[真值](javascript-foundation-primitive.md#boolean)或空字符串`""`, 标识启用属性
  - 变量为其他值时，忽略属性


不支持语句, 仅支持表达式

## v-model

- 在**表单**输入元素或组件上创建双向绑定
- 忽略所有表单元素的value, checked, selected attribute的初始值, 仅使用**Vue实例的数据**作为数据来源
- 仅限于`<input>, <select>, <textarea>`
- 修饰符
  - `.lazy`: 监听change事件而不是input
  - `.number`: 将输入转为数字
  - `.trim`: 移除输入内容两端的空格

## v-slot

- 仅限于\<template>, [组件](vue-components.md)中使用
- 用于[命名插槽](vue-component-slot.md#命名插槽)
- 用于定义[子插槽作用域](vue-component-slot.md#作用域插槽)

> 代替废弃的`slot-scope`

## v-pre

## v-once

## v-memo

## v-html

- 语法: `<h1 v-html='msg'></h1>`
  - h1的内容被替换为msg的值
- 变量为msg的值与标签内容绑定, 被解析为html
- 安全警告: 动态渲染HTML是非常危险的，容易造成[XSS漏洞]()
  - 确定内容可靠时再使用v-html
  - 永远不要使用用户提供的HTML内容

## 指令参数

```html
<a v-bind:href="url">...</a>
```

动态参数

- 动态参数的**表达式的值**应该是字符串或null
- 动态参数的表达式的约束, 不包含空格, 不包含引号
- attributeName会被当做javascript表达式进行求值

```html
<a v-bind:[attributeName]="url>...</a>
```

修饰符

- .prevent为修饰符

```
<form @submit.prevent="onSubmit">...</form>
```
