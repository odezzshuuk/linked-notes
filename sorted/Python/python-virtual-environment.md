# Python Virtual Environment

* [Virtual Env](#virtual-env)
* [deactivate virtual environment](#deactivate-virtual-environment)
* [how venvs work](#how-venvs-work)

## Virtual Env

> similar concept in other language like [project with package.json](nodejs-package-json.md)

it's general to create virtual environment in current working directory

```sh
python -m venv .venv
# or
python3 -m venv .venv
```

Create virtual environment, and specify the virtual environment directory as `env_path`

```shell
python -m venv env_path
```

Activate virtual environment

- windows
  - **cmd**: `env_path/Scripts/activate.bat`
  - **PowerShell**: `env_path/Scripts/Activate.ps1`
- unix or MacOs
  - bash/zsh: `source env_path/bin/activate`
  - fish: `source env_path/bin/activate.fish`
  - csh/tcsh: `source env_path/bin/activate.csh`
  - PowerShell: `env_path/bin/Activate.ps1`

check current activated virtual environment

- linux

```shell
echo $VIRTUAL_ENV
```

- windows

```shell
$env:VIRTUAL_ENV
```

## Deactivate/Quit Virtual Environment

```sh
deactivate
```

## How venvs Work

- python interperter running from a virtual environment
- `sys.prefix` and `sys.exec_prefix` point to the virtual environment
- `sys.base_prefix` and `sys.base_exec_prefix` point to the base environment
- use `sys.prefix == sys.base_prefix` to determine if the current interpreter is running from a virtual environment

```py
sys.prefix == sys.base_prefix
```
## conda

[conda](python-conda.md)
