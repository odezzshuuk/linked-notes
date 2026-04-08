# Linux - Execute Shell Script

* [Script Like This](#script-like-this)
* [Conclusion](#conclusion)
* [./script.sh](#scriptsh)
* [bash script.sh](#bash-scriptsh)
* [source script.sh](#source-scriptsh)
* [. ./script.sh](#-scriptsh)

## Script Like This

Given `script.sh` as example

```sh
# export variable
var="hello script"
export var

# execute script
./subdir/foo.sh
bash ./subdir/foo.sh
source ./subdir/foo.sh
. ./subdir/foo.sh
```

subdirectory `subdir` contains `foo.sh`

```sh
#! /bin/bash

echo $0
```

## Conclusion

`./script.sh`

- execute the script in a new [shell](linux-shell.md)
- so the **variable** in the script is not exported as a shell variable

`bash script.sh`

- execute the script as [`./script.sh`](#scriptsh) does
- Another difference with `./script.sh` that I know is effect on the value of `dirname $0`
  - `bash path/to/script.sh` the dirname is `path/to`
  - `./path/to/script.sh` the dirname is `./path/to`, with a `./` before

`source script.sh` and `. ./script.sh`

- Execute the script like 
  - type command in current shell
  - or add the file content at current script
- So the variable in the script is exported as a shell variable

## ./script.sh

```sh
./script.sh
```

- permission denied

give execute permission

```sh
chmod +x script.sh
```

after that `script.sh` can be executed

```sh
./script.sh
```

`echo $var` **show nothing**

**that is to say**

- variable in script is not exported as a shell variable
- ~~the script.sh is executed in a sub shell~~

## bash script.sh

```sh
bash script.sh
```

`echo $var` **show nothing**

also can execute the script, but not export the variable either

## source script.sh

```sh
source script.sh
```

`echo $var`

```
hello script
```

in this way, the variable is exported as shell variable

## . ./script.sh

- alias of `source script.sh`
