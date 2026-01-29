# Git - Worktree

## What It Is

- A Git feature that attaches multiple working directories to a single repository while sharing one object database.
- Each worktree owns its own `HEAD`, index, and working tree; metadata lives under `.git/worktrees/`.
- Like an always-checked-out branch, but in a separate directory.

## What's For

- Keep multiple branches checked out simultaneously without stashing or cloning.
- Reduce disk and network usage compared to full clones because objects are shared.
- Parallelize workstreams (hotfix vs. feature) without disturbing the main checkout.

## How to Create

```bash
# create worktree at ../repo-feature for an existing branch
git worktree add ../repo-feature feature-branch

# create branch and worktree together
git worktree add -b feature-branch ../repo-feature

# detach to a commit (no branch)
git worktree add --detach ../repo-old <commit>
```

- Run from the primary worktree; ensure it is clean or use `--force` when you understand the risk.
- One branch can be checked out by only one worktree at a time.
- `git worktree list` shows existing worktrees and their branches.

## How to Remove

```bash
git worktree remove <worktree_path>   # remove the working tree directory and its metadata
git worktree prune                     # clean up stale entries if directories were deleted manually
```

- Use `--force` with `remove` if the worktree has uncommitted changes you are willing to discard.

## Comparison With Clone The Same Repo But Checkout To Another Branch

| Feature     | Worktree                       | Clone                      |
| :---------- | :----------------------------- | :------------------------- |
| **Storage** | Efficient (shares object DB)   | Heavy (dups `.git` folder) |
| **Config**  | Shares remotes & hooks         | Independent config         |
| **Safety**  | Enforces 1-branch-per-worktree | Allows duplicate checkouts |
| **Cleanup** | `git worktree remove`          | `rm -rf <repo>`            |

For example, without worktrees, steps to get the update branch checked out in a separate clone repo would be:

```bash
# 1. Clone the entire repository again (slow, uses disk space)
git clone <repo_url> ../repo-clone

# 2. Navigate to the new directory
cd ../repo-clone

# 3. Checkout the desired branch
git checkout <target_branch>
```

with worktrees, the update already exists in the main repo which can be merged directly




