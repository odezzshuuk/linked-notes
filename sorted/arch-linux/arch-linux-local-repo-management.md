# Arch Linux - Local Repository Management

## Overview

When a package is not published in the official Arch repositories or the AUR,
you can still manage it with `pacman` by creating your own local repository.

This is useful for:
- Private packages used only on your machines
- Locally patched versions of upstream packages
- Packages built from PKGBUILDs that you do not want to publish to the AUR
- Offline or semi-offline environments

The important idea is:
- `pacman -U package.pkg.tar.zst` installs a single package file directly
- That package is recorded in the local install database
- But it is not part of a sync repository database
- Without a repository database, `pacman -Syu` cannot discover newer builds of it

If you want `pacman` to treat your package like a normal repository package,
create a local repository and register it in `pacman.conf`.

## Prerequisites

You should have:
- A package source directory or files you want to package
- A directory that will store repository packages
- Root access to update `/etc/pacman.conf`

The package should be built with Arch packaging tools such as `makepkg`.
Managing raw binaries or random extracted folders is possible, but it defeats
most of the value of `pacman`.

## Build the Package File

The repository does not build `my-tool-1.0.0-1-x86_64.pkg.tar.zst`.
`makepkg` builds that file from a `PKGBUILD`.

The usual flow is:
- Prepare a directory for one package
- Write a `PKGBUILD`
- Put the files to install beside it or fetch them in the `source` array
- Run `makepkg`
- Publish the resulting `.pkg.tar.zst` file into your local repository

**Minimal example layout**

```text
my-tool/
├── PKGBUILD
└── my-tool
```

In this example, `my-tool` is a small executable script that will be installed
to `/usr/bin/my-tool`.

Example `my-tool` script:

```bash
#!/usr/bin/env bash
echo "hello from my-tool"
```

Make it executable:

```bash
chmod +x my-tool
```

**Minimal `PKGBUILD`**

`PKGBUILD` is the Arch package recipe.
It declares the package name, version, architecture, sources, and install step.

```bash
pkgname=my-tool
pkgver=1.0.0
pkgrel=1
pkgdesc="Small example tool"
arch=('x86_64')
license=('custom')
depends=('bash')
source=('my-tool')
sha256sums=('SKIP')

package() {
	install -Dm755 "$srcdir/my-tool" "$pkgdir/usr/bin/my-tool"
}
```

Important fields:
- `pkgname` becomes the package name used by `pacman -S`
- `pkgver` and `pkgrel` become part of the final filename
- `arch=('x86_64')` matches the architecture suffix in the package filename
- `package()` copies files into the package staging directory

With the values above, the built package filename will be:

```text
my-tool-1.0.0-1-x86_64.pkg.tar.zst
```

That name is derived from:
- `my-tool` from `pkgname`
- `1.0.0` from `pkgver`
- `1` from `pkgrel`
- `x86_64` from `arch`

**Build the package**

Run this inside the directory that contains `PKGBUILD`:

```bash
makepkg -f
```

Useful variants:
- `makepkg -si` builds and installs the package locally
- `makepkg -sf` rebuilds and re-downloads missing sources if needed
- `makepkg --printsrcinfo` is useful when also maintaining AUR metadata

After a successful build, you will get:
- `my-tool-1.0.0-1-x86_64.pkg.tar.zst`
- Optional debug packages depending on your build configuration

## Step-by-Step Workflow

**0. Build the package with `makepkg`**

Create a package file first:

```bash
cd my-tool
makepkg -f
```

This produces the `.pkg.tar.zst` file that your local repository will index.

**1. Create a directory for the local repository**

```bash
sudo mkdir -p /srv/repo/custom
```

This directory will contain:
- The `.pkg.tar.zst` package files
- The repository database files such as `custom.db.tar.gz`

**2. Copy or move your package into the repository directory**

```bash
sudo cp my-tool-1.0.0-1-x86_64.pkg.tar.zst /srv/repo/custom/
```

If you rebuild the package later, copy the new version into the same directory.

**3. Create the pacman repository database**

`repo-add` generates the sync database that `pacman` understands.

```bash
cd /srv/repo/custom
sudo repo-add custom.db.tar.gz ./*.pkg.tar.zst
```

After this step, the directory will contain files like:
- `custom.db`
- `custom.db.tar.gz`
- `custom.files`
- `custom.files.tar.gz`

Those files are the repository metadata read by `pacman`.

**4. Register the repository in `pacman.conf`**

Edit `/etc/pacman.conf` and add:

```ini
[custom]
SigLevel = Optional TrustAll
Server = file:///srv/repo/custom
```

Notes:
- `file://` tells `pacman` to use a local filesystem path as a repository
- `SigLevel = Optional TrustAll` is convenient for a private local repository
- For a stricter setup, sign packages and configure signature verification

**5. Refresh databases and install through pacman**

```bash
sudo pacman -Sy
sudo pacman -S my-tool
```

From this point on, the package behaves like a repository package:
- `pacman -Ss` can search it
- `pacman -Si` can show repository metadata
- `pacman -Syu` can upgrade it when a newer build is added to the local repo

**6. Publish updates by replacing the package and regenerating the database**

Suppose you build `my-tool-1.1.0-1-x86_64.pkg.tar.zst`.

Copy it into the repository and update the database:

```bash
sudo cp my-tool-1.1.0-1-x86_64.pkg.tar.zst /srv/repo/custom/
cd /srv/repo/custom
sudo repo-add custom.db.tar.gz my-tool-1.1.0-1-x86_64.pkg.tar.zst
```

Then upgrade normally:

```bash
sudo pacman -Syu
```

## Tips & Tricks

**Use `pacman -U` only for one-off installation**

`pacman -U` is fine when testing a package once.
If you expect future upgrades, put the package into a repository early.

**Keep old package files only if you want rollback options**

If you keep many old builds in the repository directory, `repo-add` can index
them too. That may be useful for rollback, but it also makes the repository
harder to maintain.

For a simple setup:
- Keep only the newest package file for each package
- Remove stale package files before or after running `repo-add`

**Use a dedicated directory name per repository**

Examples:
- `/srv/repo/custom`
- `/srv/repo/work`
- `/srv/repo/testing`

This makes it easier to separate stable packages from experimental ones.

**A local repository can serve multiple machines**

The repository does not have to stay on the same machine.
You can expose the directory through:
- A local web server
- NFS or Samba
- SSHFS or another shared filesystem

Then replace the `file://` URL with an `http://` or `https://` repository URL.

**Signing is better for long-term maintenance**

For a personal single-machine setup, unsigned packages are common.
For multi-machine use, package signing gives better integrity and trust control.

## Example

Create a package directory:

```bash
mkdir -p my-tool
cd my-tool
```

Add an executable file:

```bash
cat > my-tool <<'EOF'
#!/usr/bin/env bash
echo "hello from my-tool"
EOF
chmod +x my-tool
```

Add a `PKGBUILD` and then build the package:

```bash
makepkg -f
```

The output file will be:

```text
my-tool-1.0.0-1-x86_64.pkg.tar.zst
```

Create the repository and publish the package:

```bash
sudo mkdir -p /srv/repo/custom
sudo cp ./my-tool-1.0.0-1-x86_64.pkg.tar.zst /srv/repo/custom/
cd /srv/repo/custom
sudo repo-add custom.db.tar.gz ./*.pkg.tar.zst
```

Register it in `/etc/pacman.conf`:

```ini
[custom]
SigLevel = Optional TrustAll
Server = file:///srv/repo/custom
```

Install it with `pacman`:

```bash
sudo pacman -Sy my-tool
```

## Related Idea

If the software is only unpacked manually under `/opt`, `/usr/local`, or your
home directory, `pacman` does not manage it at all.

If you want upgrade tracking, file ownership, and clean removal, package it
first and then publish that package through a local repository.

