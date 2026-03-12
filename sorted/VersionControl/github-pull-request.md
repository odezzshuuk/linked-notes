# Pull Request

## Introduction

- **tell others** about changes you've pushed to **a branch** in a repository **on GitHub**
- you can discuss the changes with collaborators

## Feature

- pull request has no effect on local repository
- [branch](git-branch.md) is pull request basic unit

## Pull Request Workflow

1. Prerequisite

- a new branch with new commits

> that is to say the branch **which just merged to main** can not create pull request

2. Create Pull Request

in your GitHub repository

`Pull Request` Tab -> `New Pull Request`

3. resolve conflict

> this step is **merge main changes to branch**

```bash
git pull origin main
```

```bash
git checkout branch_name
```

- branch_name: the branch which new commit

```bash
git merge main
```

- resolve conflict in local editor

```bash
git push -u origin branch_name
```

4. Merge Pull Request

> in web page click `Merge Pull Request` button

operate in local repository

- **difference** with step 3 is **third and fourth command**

> this step is **merge branch changes to main**

```bash
git pull origin main
```

```bash
git checkout main
```

```bash
git merge branch_name
```

```bash
git push -u origin main
```

## create pull request from fork

1. fork a repository
2. commit a changes on a branch
3. push to fork repository
4. contribure -> Open pull request

[my pull request on a github example repository](https://github.com/octocat/spoon-knife/pull/29038)
[another pull request on a github example repository](https://github.com/octocat/spoon-knife/pull/29039)

## Branch Naming Recommendation

- Features: `feature/add-login-system`, `feat/new-payment-method`
- Bug Fixes: `bugfix/fix-header-alignment`, `fix/issue-1234`
- Documentation: `docs/update-readme`, `docs/add-api-docs`
- Refactoring: `refactor/optimize-auth-module`, `refactor/cleanup-code`
- Chores: `chore/update-dependencies`, `chore/cleanup-unused-code`

