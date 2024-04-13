# Linux - Tricks

* [alias](#alias)
* [get last command output](#get-last-command-output)
* [let command output as another command's parameter](#let-command-output-as-another-command's-parameter)
* [jump back to previous directory](#jump-back-to-previous-directory)
* [Running Command In Background](#running-command-in-background)

## Alias

- define shortcut for command

```sh
alias ..='cd ..'  # type .. go back to parent directory
```

## get last command output

use `!!` to get last command output

```sh
echo "hello world"
```

then `echo !!` will

```sh
echo !!
```

## let command output as another command's parameter

use `$(command)` to get command output

- for example, use `date` command to get current date

```sh
echo "Today is $(date)"
```

remove related package

```sh
sudo apt remove $(dpkg-query --show --showformat='${Package}\n' | grep -i 'package-name')
```

remove all trusted sources in [firewalld](linux-firewalld.md)

```sh
sudo firewall-cmd --remove-source=$(sudo firewall-cmd --list-sources) --permanent
```

## jump back to previous directory

```sh
cd -
```

back to two more previous directory

```sh
cd ~2
```

## Running Command In Background

add `&` after command, it will run in background, you can continue use bash

VS [&&](linux-shell-operators.md#logic-operator)

## Hang up a process


