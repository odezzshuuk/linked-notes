# AJAX

## What is this

- Asynchronous JavaScript and XML
- mainly build with [XMLHttpRequest](javascript-bom-xmlhttprequest.md) object
- use number of existing technologies together, including
  - HTML or XHTML
  - CSS
  - JavaScript
  - DOM
  - XML
  - XSLT
  - XMLHttpRequest Object
  - JSON
- web application are able to make quick, incremental updates to the user interface without reloading the entire browser page

1. Send request

- Send request
  - open(method, url, async): 
    - method: request method, get, post, head
    - url: request URL
    - async: whether asynchronous
  - send(string): send request, string is the request body

```javascript
var xhr = new XMLHttpRequest();
xhr.open("GET", "example.txt", true);
xhr.send();
```

2. What to do after receiving response

```js
httpRequest.onreadystatechange = nameOfFunction;
```