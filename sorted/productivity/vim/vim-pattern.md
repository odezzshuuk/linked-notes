# Vim - Pattern

## Best Practice

Match string that include word `foo` but not include word `bar`

- `/\v(.*<bar>.*)@!.*<foo>.*`

## Negate Pattern

why `/\v.*<foo>.*(.*<bar>.*)@!` not work as expected?

- `@!` is a zero-width negate pattern match at current position, which means already matched string will not be checked again
- This will match any string that include word `foo`, regardless of whether it include word `bar` or not


