# Package In NPM

- a package must contain a [package.json](nodejs-package-json.md) file in order to be published to the npm registry.

## package

~~~
- a) folder include package.json。
- b) Compressed tarball include (a)
- c) URL parsed as (b)。
- d) `<name>@<version>` and (c) both published to the registry
- e) `<name>@<tag>` Point to (d)
- f) `<name>` with latest tag satisfying (e)
- g) A git url，get (a) when git clone 
~~~

git url format:

- `git://github.com/user/project.git#commit-ish`
- `git+ssh://user@hostname:project.git#commit-ish`
- `git+http://user@hostname/project/blah.git#commit-ish`
- `git+https://user@hostname/project/blah.git#commit-ish`

## VS Module

- Module may be not a package, only module with package.json is a package
