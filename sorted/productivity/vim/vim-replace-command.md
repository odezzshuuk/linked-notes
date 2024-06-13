# Vim - Find And Replace

```shell
:'<,>'s/foo/bar/g
```

```shell
:{作用范围}s/{目标}/{替换}/{标志}
```

替换5到12行

```
:5, 12s/foo/bar/g
```

替换当前行和接下来两行

```
:.,+2s/foo/bar/g
```

替换当前行所有

```
:s/foo/bar/g
```
