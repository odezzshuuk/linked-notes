# Lua - require function

* [What It Is](#what-it-is)
* [Feature](#feature)
* [LUA_PATH](#lua_path)
* [package.path](#package.path)
* [Search Paths](#search-paths)
* [Who determine the search path](#who-determine-the-search-path)
* [Return Value](#return-value)

## What It Is

- loading and run libraries
- Doing the same job as [`dofile`](lua-built-in-functions.md) function, but has different mechanism and more features

## Feature

- controls whether a library has already been run to avoid running it twice

## LUA_PATH

- `require` first search `LUA_PATH`

## package.path

```lua
$ print(package.path)

/opt/homebrew/share/lua/5.4/?.lua;
/opt/homebrew/share/lua/5.4/?/init.lua;
/opt/homebrew/lib/lua/5.4/?.lua;
/opt/homebrew/lib/lua/5.4/?/init.lua;
./?.lua;
./?/init.lua
```

- `package.path` is a string initialized by the environment variable [`LUA_PATH`](#lua_path)

**Caveat**:

- `.` is **not the relative path of the script who call `require` function**
- `.` in relative path `./?.lua` or `./?/init.lua` represent the directory of the entry script of program, that is where the `lua` command is executed

For example, if execute command `lua script.lua` at the root of following directory structure, for `require('add')` in `/mod/init.lua` will cause module not found error

```
.
├── mod
│   ├── add.lua
│   └── init.lua
└── script.lua
```

## Search Paths

If a search path value is: `?;?.lua;c:\windows\?;/usr/local/lua/?/?.lua`

`require "foo"` will try to open the following files:

- `foo/`
- `foo/init.lua
- `foo.lua`
- `c:\windows\foo`
- `/usr/local/lua/foo.lua`

Check Search Paths With

```lua
print(package.path)
```

## Who determine the search path

- first, the global variable `LUA_PATH` is checked `

## Return Value

return a lua [module](lua-modules.md)

- add.lua

```lua
function add(a, b)
    return a + b
end
```

- main.lua

```lua
local f = require "add"
sum = f.add(1, 2)
```

