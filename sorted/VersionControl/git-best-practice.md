# Git - Best Practice

* [Output Git Log In Stdout](#output-git-log-in-stdout)
* [Track A file Changes History](#track-a-file-changes-history)
* [print merges commit log](#print-merges-commit-log)
* [Check Commit Log](#check-commit-log)
* [Undo Stage/Commit](#undo-stage/commit)
* [Remove File From Stage](#remove-file-from-stage)
* [Remove File that already added to previous commit but added to .gitignore](#remove-file-that-already-added-to-previous-commit-but-added-to-.gitignore)
* [Discard All Local Changes](#discard-all-local-changes)
* [check staged files](#check-staged-files)
* [Set HEAD to specified status](#set-head-to-specified-status)
* [Append new modification to the last commit](#append-new-modification-to-the-last-commit)
* [Temporarily save current modification](#temporarily-save-current-modification)
* [Check all branches](#check-all-branches)
* [Get Remote Url](#get-remote-url)
* [Resovle Conflict](#resovle-conflict)
* [A way to make the lastest commit as the initial commit](#a-way-to-make-the-lastest-commit-as-the-initial-commit)
* [Copy Files Or Directory From Another Commit](#copy-files-or-directory-from-another-commit)
* [Check Ignored Files](#check-ignored-files)
* [Filter Commit History By Specified File](#filter-commit-history-by-specified-file)
* [Writing Git Commit Message](#writing-git-commit-message)
* [Squash Last N Commits](#squash-last-n-commits)
* [Restore File Or Directory That Deleted In Head But Undeleted In Another Commit](#restore-file-or-directory-that-deleted-in-head-but-undeleted-in-another-commit)

## Output Git Log In Stdout

```sh
git --no-pager log
```

> `git log | cat` also works, but not colorful

## Track A file Changes History


## print merges commit log

```bash
git log --merges
```

## Check Commit Log

```sh
git log
```

output

```
commit d590a26b3b988f24842d433d4b64708ff545d399 (HEAD -> main)
Author: example <62017693+example@users.noreply.github.com>
Date:   Mon May 30 15:24:20 2022 +0800

    mainwindow.cpp : 608

commit fa552d867bb6615f049720adaf336faed2727a16 (origin/main)
Author: example <62017693+example@users.noreply.github.com>
Date:   Mon May 30 09:12:14 2022 +0800
```

commit id: d590a26b3b988f24842d433d4b64708ff545d399

## Undo Stage/Commit

```bash
git reset [--soft | --mixed [-N] | --hard |--merge | --keep] [-q] <commitid>
```

| option  | undo commit | undo `git add` | discard modification | is default options |
| ------- | ----------- | -------------- | -------------------- | ------------------ |
| --soft  | yes         | no             | no                   | no                 |
| --mixed | yes         | yes            | no                   | yes                |
| --hard  | yes         | yes            | yes                  | no                 |

## Remove File From Stage

```sh
git rm --cached [<file>...]
git rm --cached -r [<dir>...] # recursive remove
```

## Remove File that already added to previous commit but added to .gitignore

1. remove a file from stage
2. then git add back again

```sh
git rm --cached -r . # remove all files from stage 
git add . # add all files to stage
```

## Discard All Local Changes

```sh
git reset --hard # discard all local changes and untracked files
git clean -fxd # delete untracked files
```

## check staged files

```bash
git ls-files
```

## Set HEAD to specified status

```bash
git reset --hard <commitid>
```

## Append new modification to the last commit

- `git commit --amend` after some changes have been made

for example forget to add a file to the last commit

```sh
git commit -m "commit with partial files" 
git add forgotten_file
git commit --amend
```

## Temporarily save current modification

- And go check other commits without committing current modification

temporarily store modification

```sh
git stash
```

save modification and new files temporarily

```sh
git stash --include-untracked
```

restore modification and delete stash record

```sh
git stash pop
```

## Check all branches

```bash
git branch -a
```

> repository download use `git clone` will only show current branches

## Get Remote Url

```sh
git remote -v
```

## Resovle Conflict


## A way to make the lastest commit as the initial commit

```sh
git checkout --orphan new_main
git add -A
git commit -m "initial commit message what you want"
git branch -D main
git branch -m main
git push -f origin main
```

## Copy Files Or Directory From Another Commit

```sh
git checkout <commitid> <relative_path>
```

## Check Ignored Files

```sh
git status --ignored
```

## Filter Commit History By Specified File

ok

```sh
git log -- <file>
```

`--follow` will follow file across renames

```sh
git log --follow -- <file>
```

specified line number

```sh
git log -L 1,1:<file>
```

## Writing Git Commit Message

Format: `<type>(<scope>): <description>`

- type: feat, fix, docs, style, refactor, test, chore
- scope: optional, such as auth, ui, api
- description: short description of the change

## Squash Last N Commits

[git rebase](git-rebase.md#squash-last-n-commits)

## Restore File Or Directory That Deleted In Head But Undeleted In Another Commit

```sh
git restore --source=<commitid> <path/to/file_or_directory>
```

## Branch Name Convention

prefix/short-description

```sh
feature/user-authentication
bugfix/login-error-handling
hotfix/critical-security-patch
release/v2.3.0
docs/api-readme-update
chore/update-dependencies
refactor/payment-service
test/add-unit-tests-for-auth
```

prefix/issue-number-short-description

```sh
feature/JIRA-1234-add-password-reset
bugfix/GH-56-fix-navbar-overflow
hotfix/INC-89-database-timeout
```

username/experimental-work

```sh
username/experiment-new-cache
username/wip-refactor-config
```

Common prefix

- feature:	New features or enhancements
- bugfix:	Fixing a non-critical bug
- hotfix:	Urgent production fix (often from main)
- release:	Preparing a new release
- docs:	Documentation only changes
- chore:	Maintenance, config, build, or tooling
- refactor:	Code restructuring without behavior change
- test:	Adding or fixing tests
- experiment:	Exploratory or throwaway work
- wip:	Work in progress (temporary)
