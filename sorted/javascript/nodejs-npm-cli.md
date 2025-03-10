# NPM - Node Package Manager

* [config npm](#config-npm)
* [npm init](#npm-init)
* [npm-install](#npm-install)
* [npm run](#npm-run)
* [npm package](#npm-package)
* [npm exec](#npm-exec)
* [npm show latest package version](#npm-show-latest-package-version)
* [npm update](#npm-update)

## Config NPM

- use `npm config` to config npm
- environment varable: `npm_config_<key>`
- use config file located in `$HOME/.npmrc`
- global config file located in `./etc/npmrc`
- project config file located in `/path/to/project/.npmrc`
- **default config** saved at `lib/utils/defs.js`. It is **unchangable**

`.npmrc`

- a file make up of series `key=value` format expression
- `${VARIABLE_NAME}` repersent environment variable

## npm init

> equilavent to `npm create`

syntax: `npm init <initializer>`

- `initializer`: a npm package, package
- if `initializer`is omitted, there are two cases
  1. current directory has a `package.json` file, then use it
  2. current directory doesn' have a `package.json` file, then use `npm init` to create a new `package.json` file

`npm init` vs `npm exec`

- `npm init foo` $\rightarrow$ `npm exec create-foo`
- `npm init @usr/foo` $\rightarrow$ `npm exec @usr/create-foo`

create a React project

```bash
npm init react-app ./my-react-app
```

generate new workspace(a directory with package.json)

```bash
npm init -w packages/a
```

options

- `npm init -y`: skip questions

## npm-install

- install a package and its dependencies
- the order of command `npm install` to install dependencies
  - `package-lock.json`
  - `yarn.lock`
  - `npm-shrinkwrap.json`

Options:

`-D, --save-dev`:

- add package to `devDependencies`

> dev tools dependencies, like syntax check

`--no-save`:

- prevent saving to `dependencies`
- `package.json`

`--legacy-peer-deps`

- from npm version 7, default behavior for resoving peer dependencies has changed
- npm only allow installation of packages that have compatible peer dependencies
- `--legacy-peer-deps` allows to use the older algorithm for resolving peer dependencies
- not recommended for production use

## npm run


## npm package

[npm package](nodejs-npm-package.md)

## npm exec

## npm show latest package version

```bash
npm show [package-name] version
```

## npm update

**respecting the [semver](semantic-versioning.md) constraints** of both your package.json and its dependencies

- if the latest version is `1.2.2`
- if semver `^1.1.1`, `npm update` will update to `1.2.2`
- if semver `~1.1.1`, `npm update` will update to `1.1.2`
- for semver below `1.0.0`, if semver `^0.2.0`, `npm update` will update to `0.2.2`, if version `0.2.2` exist

default will not update [semver](semantic-versioning.md) value in you `package.json`

- use `--save` option to update package while update semver value in [`package.json`](nodejs-package-json.md)

```sh
npm update --save typescript
```

update all

```sh
npm update
```

## npm audit



