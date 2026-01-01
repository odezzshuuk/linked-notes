# Lua - Metatable

* [What It Is](#what-it-is)
* [setmetatable](#setmetatable)
* [metamethod](#metamethod)
* [arithmetic metamethods](#arithmetic-metamethods)
* [__index metamethod](#__index-metamethod)

## What It Is

## What's For

- With Metatable, you can change the behavior of a table, include
  - add tables
  - compare tables
- metamethods are defined on the metatable

## setmetatable

`setmetatable(table, metatable)`

- set or change metatable

## metamethod

called by specific operator or function in lua, for example

- `__add` for `+`
- `__sub` for `-`
- `__metatable` for `getmetatable` and `setmetatable`
- `__tostring` for `print()`

## arithmetic metamethods

```lua
Set = {}

-- a function to have a look at the table
function Set.tostring(set)
  local s = "{"
  local sep = ""
  for e in pairs(set) do
    s = s .. sep .. e
    sep = ", "
  end
  return s .. "}"
end

function Set.union(a, b)
  local res = Set.new{}
  for k in pairs(a) do res[k] = true end
  for k in pairs(b) do res[k] = true end
  return res
end

Set.mt = {}
-- This function a Set with empty metatable
function Set.new(t)
    local set = {}
    setmetatable(set, Set.mt)
    for _, l in ipairs(t) do set[l] = true end
    return set
end

-- define __add metamethod
Set.mt.__add = Set.union

-- check the result
s1 = Set.new{10, 20, 30, 50}
s2 = Set.new{30, 1}
s3 = s1 + s2 print(Set.tostring(s3))
```

- other arithmetic metamethods similar to `__add`
  - `__sub` for subtraction
  - `__mul` for multiplication
  - `__div` for division
  - `__mod` for modulo
  - `__pow` for exponentiation
  - `__unm` for negation
  - `__concat` for concatenation
  - `__len` for computing the length of a table
  - `__eq` for equality
  - `__lt` for less-than
  - `__le` for less-than-or-equal

## __index metamethod

- when access to an absent field in a table, the result usually is `nil`
- if a provide `__index` function on the metatable, lua will call it with the table and the absent key

```lua
window = {}
window.mt = {}
function window.new(w)
  setmetatable(w, window.mt)
end

window.prototype = {x=0, y=0, width=100, height=100}
window.mt.__index = function (table, key)
  return window.prototype[key]
end

w = window.new{x=10, y=20}
print(w.width)  -- 100
```
