# Element List

- [pre](#pre)
- [tb](#tb)
- [a](#a)
- [form](#form)
- [section](#section)
- [Division Tags](#division-tags)
- [img tag](#img-tag)
- [head tag](#head-tag)
- [link](#link)
- [meta](#meta)

## canvas

- default size is 300x150

## textarea

- can use like a comment on a review or feedback form

## pre

- for presenting **exactly** what is written in the html

Attribute

## tb

- represents a cell in a table

## a

attribute

- href: link to navigate to
  - value "javascript:void(0)" means no navigation
- target
  - _blank: open in new window
  - _self: open in current window
  - _parent: open in parent window
  - _top: open in top-level window
- rel:
  - noopenner: the resource navigates to will not set [`window.opener`]() property on **browsing context**
  - noreferrer: to omit [`refferrer`](http-request-header.md#referer) header when navigating to the URL

## form

[form](html-element-form.md)

## section

- a section of a document, such as a chapter, a header, a footer, or a sidebar

## division tags

- div: takes up an entire line
- span: **inline** element shares a line
  - cannot modify width and height

HTML5 additions

- header
- main
- footer
- section
- nav

## img tag

- **inline-block** element, shares a line
- can modify width and height

## head tag

- contains 6 tags
  - title: tag name displayed in the browser
  - meta: defines special information for the page
  - style: CSS styles are defined here
  - link: also defines CSS styles, indicates importing external CSS styles
  - script: JavaScript code is defined here
  - base: not meaningful

## link

integrity

`<link href="style.css" integrity="hashvalue">`

- used to verify the integrity of resources, prevent resources from being tampered with

## meta

name

- `name="keywords/description/author/copyright"`
  - keywords 
  - description 
  - author
  - copyright

```html
<!DOCTYPE html>
<html>
    <meta name="keyword" content="notes, knowledge structure, frontend"/>
    <meta name="description" content="This is a note about frontend, the name attribute keyword description is used for webpage description"/>
</html>
```

Attribute: http-equiv : defines the encoding used by the webpage, defines webpage automatic refresh and redirection

- `<meta http-equiv="Content-Type" content="text/html;charset=utf-8"/>`, declares the page uses utf-8 encoding
- `<meta charset="utf-8"/>`, in HTML5 the above code can be simplified to this form
- if you see garbled text when opening, first consider this attribute
- `<meta http-equiv="refresh" content="6:url=http://www.baidu.com"/>`, indicates the page will automatically redirect to baidu.com after 6 seconds

Attribute: `property`

- og:title:`<meta property="og:title" content="title"/>`
  - og is Open Graph Protocol, provides a rich preview when a link is shared on social media platforms