# Linux - ln

* [What It Is](#what-it-is)
* [What Should be Target Argument](#what-should-be-target-argument)
* [Hard Link](#hard-link)
* [Symbolic Link](#symbolic-link)
* [Options](#options)
* [Practical Command](#practical-command)

## What It Is

- make links between files
- 2 types different links
  - [hard link](#hard-link)
  - [symbolic link](#symbolic-link)

SYNOPSIS

`ln [OPTION]... [-T] TARGET LINK_NAME`

- `LINK_NAME` should not already exist
- if `LINK_NAME` is a directory, create link inside it with the same name as file being linked

## What Should be Target Argument

for example target file is `~/dotfiles/.vimrc`

```sh
cd ~/dotfiles
ln -s .vimrc ~/.vimrc
```

check file information with `ls -l ~/.vimrc`

```sh
lrwxrwxrwx 1 username group 7 2019-01-01 00:00 $HOME/.vimrc -> .vimrc
```

- it instructs that `.vimrc` is a symbolic link to `.vimrc`
- not the file `~/dotfiles/.vimrc` what I expect

**conclusion**

- `TARGET` is a string describe symbolic link will be link to
  - path relative to `LINK_NAME`
  - or absolute path

## Hard Link

- Default link type
- Target must exist

## Symbolic Link

- Symbolic link: files that act as pointers to other files
- Set with `--symbolic`
- Each argument not to be exist

## Options

- `-s`: create [symbolic link](#symbolic-link)

## Practical Command


