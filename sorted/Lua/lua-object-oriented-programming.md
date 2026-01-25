# Lua - Object-Oriented Programming

* [What Is Object In Lua](#what-is-object-in-lua)
* [Define Object](#define-object)
* [Declare a Method](#declare-a-method)
* [Call a method](#call-a-method)

## What Is Object In Lua

- a [table](lua-fundamental.md)

## Define Object

```lua
Account = {
  balance = 0,
  withdraw = function (self, v)
    self.balance = self.balance - v
  end
}
```

## Declare a Method

1. use `:` syntax to hide the `self` parameter

```lua
function Account:withdraw(v)
  self.balance = self.balance - v
end
```

2. declared with explicit `self` parameter

```lua
Account = {balance = 0}
function Account.withdraw(self, v)
  self.balance = self.balance - v
end
a1 = Account;
a1.withdraw(a1, 100)
```

## Calling A Method

Call it with `.`

- provide `self` explicitly

```lua
a = Account
a.withdraw(a, 100)
```

Call It With `:`

```lua
a1 = Account
a1:withdraw(100)
```
