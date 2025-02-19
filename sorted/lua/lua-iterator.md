# Lua - Iterator

* [What It Is Essentially](#what-it-is-essentially)
* [Features](#features)
* [Take A Look](#take-a-look)
* [ipairs](#ipairs)
* [pairs](#pairs)

## What It Is Essentially

- A function that return a function wrapped with a closure
- Both [`ipairs()`](#ipairs) and [`pairs()`](#pairs) are iterator

## Features

- Can not be accessed through index like `iter[1]`
- [Array](lua-types.md#array) and [table](lua-table.md) is not iterator
- Stop when the return value is `nil`

## Take A Look

This is a iterator

```lua
local function list_iter(t)
  local i = 0
  local n = #t
  return function()
    i = i + 1
    if i <= n then return t[i] end
  end
end

local t = {1, 2, 3, 4, nil, 6}
for element in list_iter(t) do
  print(element)
end
-- 1, 2, 3, 4
```

## ipairs

traverse array-like collection return **index** and **value**

- Used for `{"apple", "banana", "cherry"}`

## pairs

traverse table-like collection return **key** and **value**

- Used for `{a=1, b=2, c=3}`

