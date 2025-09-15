# Git - git commit

* [How to commit](#how-to-commit)
* [What Happen When Git Commit](#what-happen-when-git-commit)
* [Relative Reference Represent A Commit](#relative-reference-represent-a-commit)
* [check commit range](#check-commit-range)
* [Amend Commit](#amend-commit)
* [Cleanup Commit History](#cleanup-commit-history)
* [Check Changes](#check-changes)
* [Rewrite Commit Message](#rewrite-commit-message)

## How to commit

commit with message

```bash
git commit -m "commit message"
```

## What Happen When Git Commit

- commit save a **pointer** to the [snapshot] of the [staged](git-glossary.md#staging-area) content

for example there are three files in a directory, add all files to [stage area](git-glossary.md#staging-area), and commit

**So what happens when use git commit**

- Git check every subdirectory and save as a tree object to Git repository;
- create a new commit object, and a pointer to the root project tree;
- for that moment, there are 5 objects in [git repository](git-glossary.md#git-directory):
  - three blob(file content)
  - a tree structure: contains files in the directory, and indicate which files are blob
  - a commit: contains commit metadata and a pointer to the root tree

next commit

- next commit contains a pointer to the previous commit

## Relative Reference Represent A Commit

using relative **reference symbol** with **branch name** can represent a commit

- relative reference symbol: `^` and `~`
  - `^`: parent commit
  - `~3`: the 3th generation ancestor commit

```shell
git checkout HEAD^   # check parent commit
git checkout main^^  # check 2th generation ancestor commit
git checkout HEAD~3  # check 3th generation ancestor commit
git branch -f main HEAD^  # force move main branch to parent commit
```

## check commit range

- properly to answer question: what changes have I not yet applied to my master branch from this branch?
- Double Dot: `git log <commit1>..<commit2>`: display all commits after commit1 separated with commit2 on commit2, **not include commit2**
- Triple Dot: `git log <commit1>...<commit2>`: display all commits between commit1 and commit2

## Amend Commit

`git commit --amend`: modify the last commit message

- this command will use core.editor in [git config](git-configuration.md) to open a editor to modify the commit message
- default editor is vim
- can be changed by `git config --global core.editor <editor name>`
- or edit in ~/.gitconfig file

## Cleanup Commit History

## Check Changes

Show Changes Of A Commit

```sh
git show <commit>
```

Show Changes Between Two Commits

```sh
git diff <commit1>~ <commit2>
```

## Rewrite Commit Message

```sh
```

