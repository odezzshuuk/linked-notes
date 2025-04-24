# Mac OS - Brew

* [Install Brew](#install-brew)
* [Terminology](#terminology)
  * [formula](#formula)
  * [cask](#cask)
  * [keg](#keg)
  * [rack](#rack)
  * [Cellar](#cellar)
  * [Tap](#tap)
* [Query Installed Package](#query-installed-package)
* [Search Package](#search-package)
* [Install package](#install-package)
* [clean](#clean)
* [Query Package Info](#query-package-info)
* [Generate Brewfile](#generate-brewfile)
* [switch to a specific version](#switch-to-a-specific-version)

## Install Brew

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## Terminology

### formula

- Homebrew package definition build from upstream sources(from source code)

### cask

- Homebrew package definition that installs macOS native application

### keg

- installation destination directory of a given [formula](#formula) **version**
- e.g. `/usr/local/Cellar/git/2.23.0`

### rack

- directory containing one or more versioned [kegs](#keg)
- e.g. `/usr/local/Cellar/git`

### Cellar

- directory containing one or more [racks](#rack)
- e.g. `/usr/local/Cellar`

### Tap

- a single version of a formula

## Query Installed Package

```sh
brew list
```

## Search Package

```sh
brew search <package>
```

## Install package

```sh
brew install <package>
```

## Clean

```sh
brew cleanup <package>
```

## Query Package Info

```sh
brew info <package>
```

## Generate Brewfile

```sh
brew bundle dump
# or specify the file
brew bundle dump --file=~/.dotfiles/Brewfile
```

## Switch To A Specific Version

switch from `node` version

```sh
$node -v
v20.5.1
$ brew search node
libbitcoin-node   node ✔            node@14           node@20           nodeenv
linode-cli        node-build        node@16           node_exporter     nodenv
llnode            node-sass         node@18 ✔         nodebrew          ode
```

install `node@18`

```sh
brew install node@18
```

switch to `node@18`

```sh
brew unlink node
brew link --overwrite node@18
```

