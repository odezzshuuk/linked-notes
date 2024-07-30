# Git - Branch

* [Create New Branch From Current Commit](#create-new-branch-from-current-commit)
* [Switch Branch](#switch-branch)
* [Merge Branch](#merge-branch)
* [Resolved Conflict](#resolved-conflict)
* [Delete Branch](#delete-branch)
* [Manage Branch](#manage-branch)
* [Create a new orphan branch, ](#create-a-new-orphan-branch)
* [Branch workflow](#branch-workflow)
* [HEAD Pointer](#head-pointer)

## Create New Branch From Current Commit

```bash
git branch <branch_name>
```

what happen when `git branch`

- create a new pointer to current commit

> new branch $\rightarrow$ current commit

## Switch Branch

`git switch <branch>`

- **switching is not allowed**, if there are **uncommitted changes** in the working directory or staging area

`git checkout <branch>`

- **checkout can perform a switch**, even if working directory or staging area have uncommitted changes
- this command does two things
  - move `HEAD` to the specified `<branch>`
  - carry current modifications to the specified `<branch>`

> git log will not show all branch

## Merge Branch

merget basic usage, like: merge to master

1. check to `master` branch
2. `git merge <branch>`, `branch` is the branch you want to merge to `master`

- generally merge will use three snapshots
  - **two branch ends**
  - **common ancestor** as merge base
- git will **decide** which ancestor is the best merge base

## Resolved Conflict

- ...

## Delete Branch

- `git branch -d <branch>`

## Manage Branch

- `git branch`: display all local branch names
- `git branch -a`: display all branch names, including remote branch

***

- `git branch -v`: display all local branch names and last commit message
- `git branch --merged <branch_name>`: check `branch_name` merged branch, if `branch_name` is omitted, it will check current branch
- `git branch --no-merged <branch_name>`: check `branch_name` not merged branch, if `branch_name` is omitted, it will check current branch 

***

- `git branch -d <branch_name>`: delete branch `branch_name`
- `git branch --move <branch_name> <new-branch-name>`: rename branch `branch_name` to `new-branch-name`

after change local branch name, delete remote old branch

- `git push --set-upstream origin <newbranch>`: let others see the new branch
- `git push origin --delete <branch>`: delete remote old branch

## Create a new orphan branch

`git checkout --orphan <new-branch>`

- The first commit made on this new branch will have no parents 
- it will be the root of a new history totally disconnected from all the other branches and commits.

## Branch workflow

Long-running Branches - Work Flow

- the way is applied by most developers: master is stable branch, and another parallel branch is named develop or next

Topic Branch - Work Flow

- is a short-lived branch
- VCS before to create a branch is expensive
- in Git, it's common to create, work on, merge, and delete branches several times a day
- keep changes for minutes, days, or months, and merge when ready

## HEAD Pointer

[Head Pointer](git-reference-head.md)
