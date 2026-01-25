# Lua - Modules

## What Is Module In Lua

- lua package represented by [table](lua-table.md)

## Define A Module

```lua
local cmp = {}
function cmp.eq(a, b) return a == b end
function cmp.lt(a, b) return a < b end
return cmp
```

- `cmp` acts as a module

## Require Function

[Require function](lua-require-function.md)

