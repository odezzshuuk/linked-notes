# Github - CLI

## Create Github Repository

1. create empty repository on Github

```sh
gh repo create <repo-name> --public --confirm
```

2. create remote repository for existing local repository

```sh
gh repo create my-project --private --source=. --remote=origin --push
```

## Rename Github Repository

## Set Secret Variable From File

```sh
gh secret set -f .env
```

