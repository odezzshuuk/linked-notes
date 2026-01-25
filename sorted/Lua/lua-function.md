# Lua - Function

* [Define a Function](#define-a-function)
* [Call a Function](#call-a-function)
* [Multiple Result](#multiple-result)
* [Multiple Assignment](#multiple-assignment)
* [unpack function](#unpack-function)
* [variable number of arguments](#variable-number-of-arguments)

## Define a Function

```lua
function foo(a)
  -- function body
end
```

## Call a Function

regular function call

```lua
function foo(a)
  print(a)
end
foo("hello")
```

special call for parameter is a string literal

```lua
foo "hello"  -- equal to foo("hello")
```

special call for parameter is a table constructor

```lua
foo{a=1, b=2}  -- equal to foo({a=1, b=2})
```

## Multiple Result

Write Function return multiple result

```lua
-- return the maximum and the index in an array
function maximum(a)
  local mi = 1 -- maximum index
  local m = a[mi] -- maximum value
  for i, val in ipairs(a) do
    if val > m then
      mi = i
      m = val
    end
  end
  return m, mi
end
```

**How Multiple Result Processed**

- when call function as a statement, all results discarded
- when call function as an expression, keeps the first result is used
- when call function is the last expression in a list, all results are used, the list expression may be
  - multiple assignment
  - table constructor
  - arguments to function calls
  - return statement

```lua
s = string.find("hello Lua users", "Lua") -- s = 7
s, e = string.find("hello Lua users", "Lua") -- s = 7, e = 9
x, y, z = 10, string.find("hello Lua users", "Lua") -- x = 10, y = 7, z = 9
```

> unlike python, python return **tuple** instead of multiple result

in python

```py
def foo():
    return 1, 2, 3
t = foo()
print(type(t)) # <class 'tuple'>
```

## Multiple Assignment

```lua
function foo0 () end                  -- returns no results
function foo1 () return 'a' end       -- returns 1 result
function foo2 () return 'a','b' end   -- returns 2 results
```

Function call is not the last element always produce one result

```lua
x, y = foo2(), 20                     -- x='a', y=20
```

multiple assignment appear in another 3 places

- arguments to function
- [table constructors](lua-table.md)
- return statement

## unpack function

> seems like [spread operator in JavaScript](javascript-spread-syntax.md)

- receive an array and return its elements as multiple results

```lua
a, b = unpack{10, 20, 30}  -- a=10, b=20, 30 is discarded
```

## various number of arguments

- `...` to receive a various number of arguments

```lua
function foo(...)
  -- ...
  for i, v in ipairs(arg) do
    print(v)
  end
end
```

- hidden parameter `arg` collected in a **table**

