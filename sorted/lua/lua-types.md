# Lua - Types

* [Nil](#nil)
* [Boolean](#boolean)
* [Numbers](#numbers)
* [Strings](#strings)
* [Array](#array)
* [Table](#table)
* [Functions](#functions)
* [Threads](#threads)

## Nil

## Boolean

## Numbers

## Strings

concatenate string

- operator `..` to concatenate string

```lua
local str = "hello" .. "world"
```

## Array

- **Array is a [table](#table) with integer index**
- **By Default: lua start array index from 1**

```lua
a = {1, 2, 3}
print(a[1]) -- 1
```

Array index can start at any number

```lua
a = {}
for i=-5, 5 do
  a[i] = 0
end
```

New Array

```lua
a = {} -- empty array
```

Get Array length

```lua
a = {1, 2, 3}
print(#a) -- 3
```

With this trick, you can get the last element of an array

```lua
a = {1, 2, 3}
print(a[#a]) -- 3
```


## Table

[table](lua-table.md)

## Functions


## Threads


