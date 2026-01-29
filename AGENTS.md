# AGENTS.md

## Project Overview

This repository is a Markdown knowledge base (“digital garden”) of software engineering and computer science notes. Content is organized by topic with curated notes in sorted/ and an inbox of working notes in unsorted/. The repo also includes small Node.js scripts for link normalization and filename normalization, plus a Python/Jupyter toolchain for notebook-based work.

## Repository Layout

- sorted/: curated topic notes
- unsorted/: inbox / working notes
- image/: diagrams and assets
- script/: maintenance scripts for renaming files and normalizing links
- requirements.txt: Python/Jupyter dependencies

## Setup Commands

- Python tooling (optional, for notebooks): `python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt`
- Node.js scripts: Node.js runtime only; no package.json is required.

## Development Workflow

- Primary work is editing Markdown files in place.
- Add new notes to sorted/ when the topic is decided; otherwise start in unsorted/.
- Keep filenames lowercase, kebab-case, and with .md extension.

## Content & Linking Conventions

- Use kebab-case, lowercase filenames for notes.
- Use relative Markdown links to local .md files or in-file anchors.
- Marksman is configured for title-based wiki slugs and GitLab-style heading IDs (see .marksman.toml). Keep headings stable to avoid breaking links.
- Prefer small, focused edits to individual notes; avoid mass refactors unless necessary.

## Automation Scripts

Scripts compute the repository root with path.dirname(process.cwd()), so run them from the script/ folder.

- Normalize filenames (underscores to kebab-case, lowercase):
  - `cd script && node RecursiveRename.js`
- Normalize Markdown links (underscores to kebab-case, lowercase):
  - `cd script && node ModifyUrlLink.js`

Do not edit script/lodash.js unless you are intentionally updating the vendored source.

## Testing Instructions

- No automated tests are defined.

## Build and Deployment

- No build or deployment pipeline is defined.

## Code Style

- Markdown-first repository; keep notes concise and organized.
- Prefer consistent headings and stable anchors.
- Avoid changing filenames/links unless you also update references.

## Pull Request Guidelines

- Keep changes scoped to the relevant note(s).
- If you rename files or links, use the scripts above and verify references manually.

## Troubleshooting

- If links break after renames, re-run the link normalization script from script/.
- If headings change, update in-file anchors in related notes.
