# Python - Pip

* [What It Is](#what-it-is)
* [Where to Install Package](#where-to-install-package)
* [Checking Where Packages Are Installed](#checking-where-packages-are-installed)
* [Query Installed Packge List](#query-installed-packge-list)
* [Install Package](#install-package)
* [Remove Package](#remove-package)
* [File requirements.txt](#file-requirements.txt)
* [pyproject.toml](#pyproject.toml)

## What It Is

- package manager for python

## Where to Install Package

according to [python-virtual-environment.md](python-virtual-environment.md) there are two places to install package

- global
- [virtual environment](python-virtual-environment.md)


## Checking Where Packages Are Installed

- `pip show <package>` to see where it is installed

## Query Installed Packge List

```sh
python -m pip list
```

## Install Package

Simple Install Package

```sh
pip install <package>
```

install from [PyPI](python-glossary.md#pypi)

- version number can be specified by `==version_number` after package name

```shell
python -m pip install numpy==1.1.0
```

install from local [archives](python-glossary.md#source-distribution)

```sh
python3 -m pip install ./dist/SomeProject-1.0.1.tar.gz
```


## Remove Package

- uninstall package1 package2

```sh
python -m pip uninstall package1 package2
```

## File requirements.txt

Create Environment from `requirements.txt`

```shell
pip install -r requirements.txt
```

Write Current Environment to `requirements.txt`

```shell
pip freeze > requirements.txt
```

## pyproject.toml

- can not use like [package.json](nodejs-package-json.md) in nodejs for now

