# Git - Command List

- [git restore](#git-restore)
- [git status](#git-status)
- [git stash](#git-stash)
- [git merge](#git-merge)
- [git revert](#git-revert)
- [git reset](#git-reset)
- [git clean](#git-clean)
- [git checkout](#git-checkout)
- [git cherry-pick](#git-cherry-pick)
- [git add](#git-add)
- [git rebase](#git-rebase)

## git restore

- restore the specified files in working directory

For example

- switch master
- reverts the makefile to two versions back
- accidentally delete hello.c
- gets it back from [index]()

```bash
git switch -c master
git restore --source master~2 Makefile
rm -f hello.c
git restore hello.c
```

## git status

- check current status of working directory

## git stash

- save current working directory to a dirty working directory
- secenario: when you want to record current working state and check a commit, but you don't want to create a commit for current changes

`git stash push`: save current modification to a temporary directory, and restore to HEAD status

- Add default description: `WIP on branchname: commitid "commit message"`
- `git stash push -m "message"`: save current modification to a temporary directory, and restore to HEAD status, and add a `message`
- `git stash`: equilevant `git stash push`

`git stash list`: check the list of temporary directory

`git stash apply`: apply the most recent file snapshot in the temporary directory

- `git stash apply --index <index>`: apply specific file snapshot in temporary directory by index
- through `git stash list` you can check `index` value
- `git stash apply --index 0`: apply the most recent file snapshot in the temporary directory

`git stash pop`: apply the most recent file snapshot in the temporary directory, and delete the snapshot

## git merge

[merge](git-merge.md)

## git revert

- `git revert <commit_id>`: undo the changes made by the specified `commit_id`, and create a new commit

```sh

```

## git reset

[reset](git-reset.md)

## git clean

- remove untracked files from the working tree

## git checkout

- `git checkout <branch>`
- `git checkout -b <new-branch>`: same as `git branch <new-branch>`
- `git checkout -detach [<branch>]`
  - store local modifications in the working tree
  - current working tree status: commit record + local modifications
- `git checkout [-f|--ours|--theirs|-m|--conflict=<style>] [<tree-ish>] --pathspec-from-file=<file> [--pathspec-fil-nul]`: overwrite files by match the pathspec
  - `<tree-ish>`: most often a commit
  - use `<file>` of `<tree-ish>` to overwrite `<file>` in working tree
- `git checkout (-p|--patch) [<tree-ish>] [--] [<pathspec>...]`
  - through [interactive mode]() to finish the file overwrite operation

options

- `-f`: force to switch branch, even if there are untracked files or local modifications

## git cherry-pick

- `git cherry-pick <commit_id>`: apply the changes of specified `commit_id` to [`HEAD`](git-glossary.md#head)

## git add

## git rebase

`git rebase [-i] [options] [--exec <cmd>] [--onto <newbase> | --keep-base] [<upstream> [<branch>]]`

## git fetch

## git rm

`git rm [options] <pathspec>`

pathspec

- file to remove
- only remove the paths that [known to git](git-glossary.md#staging-area)
- globbing matches, e.g. `git rm 'd*'` will remove 'd', 'desert', ...

options

- `--cached`


