# css - align

index.html

```html
<head>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="box">
    <div class="first">A</div>
    <div class="second">B</div>
    <div class="third">C</div>
    <div class="third">C</div>
  </div>
</body>
```

style.css

```css
*, ::after, ::before {
  box-sizing: border-box;
}

body {
  margin: 0;
  padding: 0;
}

.box {
  display: grid;
  margin: 0px;
  background-color: #bbbb00;
  grid-template-columns: 200px 200px;
  grid-template-rows: 200px 200px;
  border-radius: 20px;
  align-content: space-between;
  align-items: center;
  width: 100vw;
  height: 600px;
}

.box div {
  border: 2px solid black;
  border-radius: 20px;
  margin: 20px;
  font-size: 2rem;
  text-align: center;
  padding: 0.8em 0;
}

.first {
  background-color: #f026a9
}

.second {
  background-color: #2af0af
}

.third {
  background-color: #a3f0e7
}
```
