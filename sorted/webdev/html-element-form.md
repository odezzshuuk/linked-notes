# form

## What is for

- interactive controls containing submitting information
- use to collect user input

## form related elements

- tag that used inside form
- form-associated elements
  - [button]
  - fieldset
  - [input](html-element-input.md)
  - object
  - output
  - select
  - textarea
  - img

## action property

- value of action is the program [uri](computer-network-uri.md) that will handle the submitted form data
- can be overridden by `formaction` attribute on `<button>, <input type="submit">, <input type="image">` elements

## method property

- specific [http method](http-request-method.md) to submit form data
- available value: 1.post 2.get 3.dialog

get method

- form data is appended to the action attribute URL with a '?' as a separator
- the corresponding name/value pairs are concatenated after the '?', for example `/url?key1=value1&key2=value2`

## enctype property

```html
<form action="demo_post_enctype.html"
method="post" enctype="multipart/form-data">
  First name: <input type="text" name="fname"><br>
  Last name: <input type="text" name="lname"><br>
  <input type="submit" value="submit">
</form>
```

- enctype property specifies how the form-data should be encoded when submitting it to the server

Available Value

<table>
  <tr>
    <td>application/x-www-form-urlencoded</td>
    <td>Default, spaces are converted to '+', special characters are converted to ASCII HEX values</td>
  </tr>
  <tr>
    <td>multipart/form-data</td>
    <td>Required when the form has file upload controls</td>
  </tr>
  <tr>
    <td>text/plain</td>
    <td>Converts spaces to '+', does not encode special characters</td>
  </tr>
</table>