# Github Action - Workflow Files Keys

## List

- [on]()
- steps
- [uses](#uses)
- with
- matrix strategy

## on

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:
```

- pull_request, push, opens an issue
- `on:workflow_dispatch`: Manually run by CLI or Github website
  - CLI: `gh workflow run greet.yml`
  - Website: 
- ...

`on.<push|pull_request|pull_request_target>.<paths|paths-ignore>`

- `paths`: Only trigger workflow when changes are made to files that match the specified paths

```yaml
on:
  push:
    paths:
      - 'src/**'
      - 'docs/**'
```

- do something when changes are made to any files in the `src` or `docs` directories

`on.issues`


## jobs

> Github Actions Core

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Hello, world!"
```

- By default, each job runs in parallel.
- Jobs can be configured to run dependent on other jobs

## steps

- A job is made up of a sequence of steps

```yaml
name: Greeting from Mona

on: push

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
      - name: Greet the world
        run: echo "Hello, world!"
```

## with 

There are 2 different `with`

- `jobs.<job_id>.steps[*].with`
- `jobs.<job_id>.with`

`jobs.<job_id>.with`

```yaml
jobs:
  call-workflow:
    uses: octo-org/example-repo/.github/workflows/called-workflow.yml@main
    with:
      username: mona
```

## uses

full name: `jobs.<job_id>.uses`

- Run Reusable action defined in a **separate repository** or in the **same repository** as job
  - syntax for separate repository: `{owner}/{repo}/.github/workflows/{filename}@{ref}`
    - `ref` can be a SHA, release tag, or branch name
  - syntax for same repository: `./.github/workflows/{filename}`

## workflow_call

full name: `on.workflow_call`

## Runner

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
```

- Virtual machine or container, such as [docker container](docker-glossary.md#container)

## inputs

## secrets

## outputs

## needs

```yaml
jobs:
  job1:
  job2:
    needs: job1
  job3:
    needs: [job1, job2]
```

- `job2` depends on `job1`'s successful completion
- `job3` depends on `job1` and `job2`'s successful completion
- Any jobs in `needs` list that fail or skipped, current job will be skipped

## Matrix Strategy

Allows you use variables in a single job definition to automatically create multiple job runs that are based on the combinations of the variables

```yaml
jobs:
  build:
    permissions:
      contents: write
    strategy:
      fail-fast: false
      matrix:
        include:
          - platform: "macos-latest"
            args: "--target x86_64-apple-darwin"
            target: "x86_64-apple-darwin"
          - platform: "ubuntu-22.04"
            args: "--bundles deb"
            target: "x86_64-unknown-linux-gnu"
          - platform: "windows-latest"
            args: ""
            target: "x86_64-pc-windows-msvc"
    steps:
      - uses: actions/checkout@v3
      - name: Install Rust
        uses: actions-rs/toolchain@v1
        with:
          platform: ${{ matrix.platform }}
          target: ${{ matrix.target }}
          build-args: ${{ matrix.args }}
          sign-binaries: true
```

- Used via syntax like `${{ matrix.platform }}`, `${{ matrix.args }}`, and `${{ matrix.target }}` in the job's steps.
