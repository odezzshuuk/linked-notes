# Lua Language Server

## What It Is

provides various language features for Lua

- support lua 5.4, lua 5.3, lua 5.2, lua 5.1, and [LuaJIT]()
- Go to Definition
- Dynamic type checking
- Find reference
- Diagnostics/Warnings

## Diagnostics Disable

disable diagnostics for specific line

```lua
--- @disable diagnostics: missing-fields
foo({ a = 1, b = 2})
```

disable diagnostics for project

- in config file, like `.luarc.json`

```json
{
    "diagnostics": {
        "disable": ["unused-function"]
    }
}
```

disbale diagnostics in neovim

```lua
require("lspconfig").lua_ls.setup({
  settings = {
    -- ...
    diagnostics = {
      disable = { "missing-type", }
    }
  },
})
```


