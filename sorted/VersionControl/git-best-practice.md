# Git - Best Practice

* [Output Git Log In Stdout](#output-git-log-in-stdout)
* [Track A file Changes History](#track-a-file-changes-history)
* [print merges commit log](#print-merges-commit-log)
* [Check Commit Log](#check-commit-log)
* [Undo commit](#undo-commit)
* [Remove File From Stage](#remove-file-from-stage)
* [Discard All Local Changes](#discard-all-local-changes)
* [check staged files](#check-staged-files)
* [Set HEAD to specified status](#set-head-to-specified-status)
* [changes forgotten to add to the last commit](#changes-forgotten-to-add-to-the-last-commit)
* [Temporarily save current modification](#temporarily-save-current-modification)
* [check all branches](#check-all-branches)
* [Get Remote Url](#get-remote-url)
* [Resovle Conflict](#resovle-conflict)
* [A way to make the lastest commit as the initial commit](#a-way-to-make-the-lastest-commit-as-the-initial-commit)
* [Copy Files Or Directory From Another Commit](#copy-files-or-directory-from-another-commit)
* [Check Ignored Files](#check-ignored-files)
* [Filter Commit History By Specified File](#filter-commit-history-by-specified-file)

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
Author: enigmaiiiiiiii <62017693+enigmaiiiiiiii@users.noreply.github.com>
Date:   Mon May 30 15:24:20 2022 +0800

    mainwindow.cpp : 608

commit fa552d867bb6615f049720adaf336faed2727a16 (origin/main)
Author: enigmaiiiiiiii <62017693+enigmaiiiiiiii@users.noreply.github.com>
Date:   Mon May 30 09:12:14 2022 +0800
```

commit id: d590a26b3b988f24842d433d4b64708ff545d399

## Undo commit

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

remove files that new add to `.gitignore` from stage that already add by previous commit 

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

## changes forgotten to add to the last commit

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

## check all branches


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

