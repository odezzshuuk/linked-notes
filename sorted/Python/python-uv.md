# Python - uv

## What is uv?

- An extremely fast Python package and project manager, written in Rust.
- Designed to be a single tool that can replace many existing Python utilities, including `pip`, `pip-tools`, `pipx`, `poetry`, `pyenv`, `twine`, and `virtualenv`
- Aims to make Python development faster, simpler, and more reliable by providing a unified interface for managing packages, projects, environments, scripts, and Python versions.

## Best Practices

1. Managing a Project

```bash
# Initialize a new project
uv init myproject

cd myproject

# Add a dependency/package
uv add requests

# Run a tool (e.g., Ruff linter)
uv run ruff check

# Lock dependencies
uv lock

# Sync environment with lockfile
uv sync
```

2. Running Scripts with Dependencies

```bash
# Create a script
echo 'import requests; print(requests.get("https://astral.sh"))' > example.py

# Add a dependency to the script
uv add --script example.py requests

# Run the script in an isolated environment
uv run example.py
```

3. Installing and Using CLI Tools

```bash
# Run a tool in an ephemeral environment
uvx pycowsay 'hello world!'

# Install a tool globally
uv tool install ruff

# Use the installed tool
ruff --version
```

4. Managing Python Versions

```bash
# Install multiple Python versions
uv python install 3.10 3.11 3.12

# Create a virtual environment with a specific Python version
uv venv --python 3.12.0

# Pin a Python version for the current directory
uv python pin 3.11
```

5. Using the pip-Compatible Interface

```bash
# Compile requirements into a universal requirements file
uv pip compile requirements.in --universal --output-file requirements.txt

# Create a virtual environment
uv venv

# Install requirements from a lockfile
uv pip sync requirements.txt
```

## Installation

You can install uv in several ways:

**Standalone Installer (Recommended):**
```bash
# macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Via pip or pipx:**
```bash
pip install uv
# or
pipx install uv
```

## Purpose

Uv's main goal is to streamline Python development by:

- Dramatically speeding up package installation and environment management (10-100x faster than pip).
- Unifying project, dependency, and environment management under one tool.
- Providing reproducible, platform-independent dependency resolution.
- Supporting modern workflows, including workspaces, lockfiles, and inline script dependencies.

## Key Features

- **Blazing Fast**: Written in Rust, uv is much faster than traditional Python tools.
- **All-in-One Tool**: Replaces pip, pip-tools, pipx, poetry, pyenv, twine, and virtualenv.
- **Universal Lockfile**: Ensures reproducible builds and dependency management.
- **Script Support**: Manages dependencies for single-file scripts with inline metadata.
- **Python Version Management**: Installs and switches between multiple Python versions.
- **Tool Management**: Installs and runs CLI tools published as Python packages.
- **pip-Compatible Interface**: Drop-in replacement for pip and related tools.
- **Workspaces**: Supports multi-project, monorepo-style workspaces.
- **Global Cache**: Deduplicates dependencies to save disk space.
- **Cross-Platform**: Works on macOS, Linux, and Windows.
