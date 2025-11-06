# Github Actions

## Best Practice

[Best Practices](github-actions-best-practices.md)

## What It Is

- A series jobs trigger by events running on corresponding runner

Running Logic

- Event
  - Runner A
    - Job 1, Job 2, Job 3
    - Job 4
  - Runner B
    - Job 1, Job 2, Job 3

## Components

Jobs

- By default, each job runs in parallel.
- Jobs can be configured to run dependent on other jobs

Events

- pull request
- push
- opens an issue
- ...

Actions

- A set of [jobs](#jobs)
- Reusable

Runner

- Virtual machine or container, such as [docker container](docker-glossary.md#container)

## Github Actions Core

[Jobs](github-actions-jobs.md)


