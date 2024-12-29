# Regex

* [match single character](#match-single-character)
* [number of occurrences](#number-of-occurrences)
* [predefined characters](#predefined-characters)
* [Group](#group)
* [Multiple Patterns](#multiple-patterns)

## Match Single Character

use `[]` to match single character

- `[a-z]`: match the character/[group](#group) from a to z
- `[a-z0-9]`: match the character from a to z and 0 to 9
- `[^abc]`: `^` in `[]`, represents not, match any character except a, b, c

> `^` outside `[]` represents line start
> you can not use `^` exclusion syntax and inclusion syntax in the same `[]`

## number of occurrences

- `?`: match the previous character/[group](#group) 0 or 1 time, equivalent to `{0, 1}`
- `+`: match the previous character/group 1 or more times, equivalent to `{1, }`
- `*`: match the previous character/group 0 or more times, equivalent to `{0, }`
- `{n}`: match the previous character/group `n` times
- `{n, m}`: match the previous character/group from `n` to `m` times
- `{n, }`: match the previous character/group at least `n` times

## predefined characters

- `.`: any single character except `\n`
- `\cx`:
- `\n`: new line character
- `\r`: carriage return character
- `\s` whitespace character, including
  - space
  - tab
  - form feed
  - line feed
- `\S`: Match non-whitespace character
- `\f`: a form feed character
- `\t`: tab character
- `\v`: Match a vertical tab character

***

- `\d`: match any digit
- `\D`: match any non-digit
- `\w`: match any word characters, including digit, letter, and underscore
- `\W`: not word characters
- `\num`: match the num-th group
- `\b`: match word boundary, which is the position between a word character

***

`^`: line start
`$`: line end

## Group

`()` use to group, inside `()` is one group

`(abc){3}`: match string `abcabcabc`

`(abc|def)`: match `abc` or `def`

## Multiple Patterns

`|` use to match multiple patterns

`a|b`: match `a` or `b`

## VS Glob Pattern

[glob pattern](glob-pattern.md)

