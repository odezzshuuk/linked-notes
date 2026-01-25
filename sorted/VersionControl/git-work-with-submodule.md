# Git - Work With Submodule

## Add Submodule

Go to submodule directory, then

```bash
git init
```

if there is no remote repository, create first

- Use [Github CLI](github-cli.md)

```bash
gh repo create
```

then

```bash
git submodule add <submodule_url> <submodule_local_path>
```

## When Parent Module Already Commit Without Set Submodule Url

> Where Error "fatal: '<submodule_path>' already exists in the index" Occurs
> When `git submodule add <submodule_url>` directly without Parent Module set Submodule Url 

Run commands In parent module repository directory

```bash
git rm -r --cached <submodule_local_path>
git commit -m "<message_after_remove_submodule_path>"  # optional
git submodule add <submodule_url> <submodule_local_path>
```

Then file `.gitmodules` created, and content may like

```ini
[submodule "<submodule_local_path>"]
    path = <submodule_local_path>
    url = <submodule_url>
```

## Can I Commit Submodule From Parent Module? No

- No, submodule is a separate repository, commit submodule separately.
- If there is a new commit in submodule. Parent module should decide whether to follow the new commit or not.

## Remove Submodule

```sh
git submodule deinit -f <submodule_local_path>
```

