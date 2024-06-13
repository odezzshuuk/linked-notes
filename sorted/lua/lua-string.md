# Lua - String

## Pattern-Matching Functions

`string.sub(s, i [, j])`

- return substring

`string.find(s, pattern, [, init[, plain]])`

- parameters:
  - `init`: start index, where to start
  - `plain`: if `true`, `pattern` is a plain string, [magic characters](lua-regex.md) will not be interpreted
- [multiple return value](lua-function.md#multiple-result), the order is:
  - first, start index of the first match
  - second, end index of the first match
  - if pattern has [captures](#capture), captured values returned after two indices

```lua


`string.gsub(s, pattern, repl[, n])`

- `repl`: can be a string, a table, a function
  - when `repl` is a string, the value is used for replacement
  - when `repl` is a table, the first capture is used as the key to index the table, and replace captured with the value

```lua
local t = { name = "lua", version = "5.4" }
x = string.gsub("$name-$version.tar.gz", "%$($w+)", t)
-- x = "lua-5.4.tar.gz"
```

## Capture

use `()` to capture

```lua
pair = "name = Anna"
_, _, key, value = string.find(pair, "(%a+)%s*=%s*(%a+)")
print(key, value)  -- name Anna
```

## Escape Sequences

- wrap in `[[ ]]` to avoid escape sequences

> '\' will be ignored

```lua

```

