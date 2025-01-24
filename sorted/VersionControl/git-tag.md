# Git - Tag

* [List Tag](#list-tag)
* [2 Types Of Tag](#2-types-of-tag)
* [Tag A Historical Commit](#tag-a-historical-commit)
* [Sharing Tag](#sharing-tag)

## List Tag

```sh
git tag
```

## 2 Types Of Tag

Lightweight Tag

- Just a pointer to a commit
- Create by `git tag <tag-name>`

> Github default tag is lightweight tag

Annotated Tag

- stored as full objects in the Git database, contains
  - tag name
  - date
  - email
  - having tag message
- create by `git tag -a <tag-name> -m <tag-message>`

## Tag A Historical Commit

```sh
git tag -a <tag-name> -m <tag-message> <commit>
```

## Add Tag To Remote Repository

- Just like sharing branch

```sh
git push origin <tag-name>
```

