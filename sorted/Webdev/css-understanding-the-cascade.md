# Understanding the Cascade

## Order

- Cascade: When two rules of the **same level** are applied to the same element, the latter rule will take effect

## Specificity

> Specificity: Selectors with smaller scope override those with larger scope; essentially different selectors have different scores

- You can think of ID, CLASS, ELEMENT as the hundreds, tens, and ones places of a number
- *, +, >, ~ don't affect the specificity of selectors

|Selector|Identifiers|Classes|Elements|Total specificity|
|--|--|--|--|:--:|
|h1|0|0|1|001|
|h1 + p::first-letter|0|0|3|003|
|li > a\[href*="en-US"]>.inline-warning|0|2|2|022|
|\#identifier|1|0|0|100|
|button:not(\#mainBtn, .cta)|1|0|1|101|

## Importance

```css
selector {
    property:value !important;
}
```
- `!important` will override all rules

