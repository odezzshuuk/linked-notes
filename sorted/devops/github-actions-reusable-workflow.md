# Github Actions - Reusable Workflow

## Overview

Reusable workflow is a GitHub Actions workflow that can be called by other workflows.

- It is declared with `on.workflow_call`
- It can expose 
  - `on.workflow.inputs`
  - `on.workflow.secrets`
  - `on.workflow.outputs`
- Calling workflows use `jobs.<job_id>.uses` to execute it

## Parameter Exposed by Reusable Workflow

inputs, secrets

- `jobs.steps[*].uses:` to call reusable workflow 
- `jobs.steps[*].with:` to pass inputs to reusable workflow

```yaml
on:
  workflow_call:
    inputs:
      username:
        description: 'A username passed from the caller workflow'
        default: 'john-doe'
        required: false
        type: string
    secrets:
      access-token:
        description: "A secret"
        required: false

jobs:
  print-username:
    runs-on: ubuntu-latest

    steps:
      - name: Print the input name to STDOUT
        run: echo The username is ${{ inputs.username }}
      - name: Pass the received secret to an action
      - uses: ./.github/actions/some-action
        with:
          token: ${{ secrets.access-token }}
```

- defined in `on.workflow_call`
  - `input` parameter name: `username`
  - `secrets` parameter name: `access-token`
- access in `jobs`
  - access inputs: `${{ inputs.username }}`
  - access secrets: `${{ secrets.access-token }}`

## Return Value Exposed by Reusable Workflow

Declare outputs at workflow level

- `on.workflow_call.outputs` to define the output
- `on.workflow_call.outputs.<output_name>.value: {{ jobs.<job_id>.outputs.<output_name> }}` to set the output value

Concrete output value at job level

- [Define output at job level](github-actions-job-outputs.md)
- Unlike `inputs, secrets` need `jobs.steps.with:` to pass value 

For example: 

- reusable workflow `output_value_workflow.yml`

```yaml
name: Output Value Workflow

on:
  workflow_call:
    # Map the workflow outputs to job outputs
    outputs:
      firstword:
        description: "The first output string"
        value: ${{ jobs.example_job.outputs.output1 }}
      secondword:
        description: "The second output string"
        value: ${{ jobs.example_job.outputs.output2 }}

jobs:
  example_job:
    name: Generate output
    runs-on: ubuntu-latest
    # Map the job outputs to step outputs
    outputs:
      output1: ${{ steps.step1.outputs.firstword }}
      output2: ${{ steps.step2.outputs.secondword }}
    steps:
      - id: step1
        run: echo "firstword=hello" >> $GITHUB_OUTPUT
      - id: step2
        run: echo "secondword=world" >> $GITHUB_OUTPUT
```

- `consumer_workflow.yml`

```yaml
name: Consumer workflow
on:
  workflow_dispatch:

jobs:
  job1:
    uses: octo-org/example-repo/.github/workflows/called-workflow.yml@v1

  job2:
    runs-on: ubuntu-latest
    needs: job1
    steps:
      - run: echo ${{ needs.job1.outputs.firstword }} ${{ needs.job1.outputs.secondword }}
```

## Create the reusable workflow

- `.github/workflows/reusable-node-ci.yml`

```yaml
name: Reusable Node CI
on:
  workflow_call:
    inputs:
      node-version:
        required: false
        type: string
        default: "20"
      run-lint:
        required: false
        type: boolean
        default: true
    secrets:
      NPM_TOKEN:
        required: false
    outputs:
      package-version:
        description: "Version from package.json"
        value: ${{ jobs.ci.outputs.package-version }}

jobs:
  ci:
    runs-on: ubuntu-latest
    outputs:
      package-version: ${{ steps.version.outputs.package-version }}
    steps:
      - uses: actions/checkout@v5

      - uses: actions/setup-node@v4
        with:
          node-version: ${{ inputs.node-version }}
          cache: npm

      - name: Install dependencies
        run: npm ci

      - name: Lint
        if: ${{ inputs.run-lint }}
        run: npm run lint --if-present

      - name: Test
        run: npm test --if-present

      - name: Read package version
        id: version
        run: |
          value=$(node -p "require('./package.json').version")
          echo "package-version=$value" >> "$GITHUB_OUTPUT"
```

## Call the reusable workflow

- in `.github/workflows/ci.yml`
- `uses: ./.github/workflows/reusable-node-ci.yml`: calling workflow
- `with:`: pass inputs to reusable workflow

```yaml
name: CI

on:
  pull_request:
  push:
    branches:
      - main

jobs:
  call-reusable-ci:
    uses: ./.github/workflows/reusable-node-ci.yml
    with:
      node-version: "22"
      run-lint: true
    secrets:
      NPM_TOKEN: ${{ secrets.NPM_TOKEN }}

  print-version:
    runs-on: ubuntu-latest
    needs: call-reusable-ci
    steps:
      - run: echo "Version is ${{ needs.call-reusable-ci.outputs.package-version }}"
```
