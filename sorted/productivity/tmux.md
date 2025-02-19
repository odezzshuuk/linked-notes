# Tmux

* [Usage](#usage)
* [Config](#config)
* [Format](#format)
* [Options](#options)
* [Status Line](#status-line)
* [default key bindings](#default-key-bindings)
* [basic object in tmux](#basic-object-in-tmux)
* [Plugin](#plugin)
* [plugin: tmux-powerline](#plugin:-tmux-powerline)
* [Cheat Sheet](#cheat-sheet)

## Usage

`<prefix> [command]`

- `prefix` is `Ctrl + b` by default
- `[command]` is keys for tmux operation

## Config

[Tmux Configuration](tmux-configuration.md)

## Format

[Format](tmux-format.md)

## Options

[Tmux Options](tmux-options.md)

## Status Line

[tmux status line](tmux-status-line.md)

## default key bindings

switch window

- `<prefix> n`
- `<prefix> p`

## basic object in tmux

[tmux object](tmux-object.md)

## Plugin

plugin manager

(https://github.com/tmux-plugins/tpm)

install plugin

1. add plugin to `~/.tmux.conf`

```conf
set -g @plugin '...'
```

2. press `<prefix> I`(capital i) to install plugin

uninstalling plugin

`~/.tmux/plugins/tpm/bin/clean_plugins`

## plugin: tmux-powerline

tmux-powerline

- generate default config file

```sh
~/.tmux/plugins/tmux-powerline/generate_rc.sh
```

- follow the output tips to do next steps

## Cheat Sheet

[tmux cheat sheet](tmux-cheat-sheet.md)
