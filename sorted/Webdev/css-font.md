# CSS Font

## font-family

- specifies a prioritized **list** of one or more font family name
- values are separated by commas
- the are alternatives
  - browser will select the first font in the list that is installed
  - or that can be downloaded using `@font-face` rule

```css
.font {
  font-family: 'Gill Sans Extrabold', sans-serif;
}
```

- `'Gill Sans Extrabold'` is the font name
- `sans-serif` is a generic font family
  - `serif`, `sans-serif`, `monospace`, `cursive`, `fantasy`, is commonly available on most operating systems
  - generic font is a fallback mechanism
  - if the browser does not find the font, it will use the fallback font
