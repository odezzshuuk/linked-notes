# Github - Github Actions Workflow Files 

* [.github/workflows](#.github/workflows)
* [Here is an example](#here-is-an-example)
* [References](#references)


## .github/workflows

What It Does: Define Github Actions

```
.github/workflows
├── build.yml
├── deploy.yml
└── test.yml
```

- Any .yml or .yaml files in this directory will be detected by Github will be treated as Github [Actions](#actions) workflow files.
- "Action will be Detected" Which means that not all .yml or .yaml files must be Action file
  - Only those that follow the correct syntax and structure will be detected and executed by Github Actions.
  - Some files may be used for other purposes, such as for better organization

## Actions

- A set of [jobs](#jobs)
- Defined in a YAML file in the .github/workflows directory of a repository
- Reusable

## Here is an example

```yaml
name: Build Nuxt4 Application
on:
  workflow_dispatch:
  push:
    branches:
      - main
jobs:
  build:
    runs-on: ubuntu-latest
    env:
      BASE_URL: https://${{ github.repository_owner }}.github.io/${{ github.event.repository.name }}
      NUXT_APP_BASE_URL: /${{ github.event.repository.name }}/
      NEON_POSTGRESQL_DB_HOST: ${{ secrets.NEON_POSTGRESQL_DB_HOST }}
      JWT_SECRET: ${{ secrets.JWT_SECRET }}
      SQLITE_DB_PATH: ${{ secrets.SQLITE_DB_PATH }}
      OAUTH_GITHUB_CLIENT_ID: ${{ secrets.OAUTH_GITHUB_CLIENT_ID }}
      OAUTH_GITHUB_CLIENT_SECRET: ${{ secrets.OAUTH_GITHUB_CLIENT_SECRET }}
    steps:
      - run: |
          echo ${NUXT_APP_BASE_URL} 
          echo ${NEON_POSTGRESQL_DB_HOST}
          echo ${JWT_SECRET}
          echo ${SQLITE_DB_PATH}
          echo ${OAUTH_GITHUB_CLIENT_ID}
          echo ${OAUTH_GITHUB_CLIENT_SECRET}
      - name: Checkout
        uses: actions/checkout@v5.0.0
        with:
          submodules: true
      - run: corepack enable
      - uses: actions/setup-node@v4
        with:
          node-version: "20"
      # Pick your own package manager and build script
      - uses: pnpm/action-setup@v4
      - run: pnpm install
      - run: npx nuxt build --preset github_pages
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./.output/public
  # Deployment job
  deploy:
    # Add a dependency to the build job
    needs: build
    # Grant GITHUB_TOKEN the permissions required to make a Pages deployment
    permissions:
      pages: write      # to deploy to Pages
      id-token: write   # to verify the deployment originates from an appropriate source
    # Deploy to the github_pages environment
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    # Specify runner + deployment step
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

In this file

- `build`, `deploy` define two jobs
- `on` defines the events 
  - trigger the workflow, which are `workflow_dispatch` 
  - `push` to `main` branch in this case
- `runs-on` defines the runner, which is `ubuntu-latest` in this case

## References

[References](github-actions-workflow-files-keys)


