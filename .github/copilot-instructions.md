# Copilot instructions for linked-notes

## Project overview

- This repo is a Markdown knowledge base (“digital garden”) with topic notes; the core structure is described in [README.md](README.md).
- Content lives primarily in [sorted/](sorted/) (curated topics) and [unsorted/](unsorted/) (inbox/working notes). Assets like diagrams live in [image/](image/).

## Note Taking Philosophy

- Try to keep notes small and focused on a single topic or concept.
- Use links to connect related notes rather than duplicating content.
- Try not to use heading levels beyond H2 (##) to keep notes flat and easy to navigate.
- For concept type content, prefer structured sections like:
  - What It Is
  - Features
  - Detail sections
- For tool usage content, prefer structured sections like:
  - What It Is
  - What's It For(Use examples to illustrate why to use it)
  - How to Use
  - Tips & Tricks
- For best practices or workflows, prefer structured sections like:
  - Overview
  - Prerequisites
  - Step-by-Step Workflow

## Note organization & linking conventions

- Notes are Markdown files with kebab-case, lowercase filenames; scripts exist to normalize underscores and casing (see [script/RecursiveRename.js](script/RecursiveRename.js)).
- Markdown links are relative and point to local .md files or in-file anchors; see examples in [sorted/modeling/maya.md](sorted/modeling/maya.md).
- Marksman is configured for title-based wiki slugs and GitLab-style heading IDs; follow the settings in [.marksman.toml](.marksman.toml) when adding headings or links.

## Automation scripts

- Link normalization is handled by the script in [script/ModifyUrlLink.js](script/ModifyUrlLink.js).
- Both rename/link scripts compute the target root with path.dirname(process.cwd()), so they are intended to be executed from the script folder.
- [script/lodash.js](script/lodash.js) is a vendored utility file; avoid editing it unless you are intentionally updating the vendored source.

## Dependencies & tooling

- Python dependencies in [requirements.txt](requirements.txt) appear geared toward notebooks and content tooling (Jupyter stack). There are no repo-defined build or test commands.

## Editing guidance for agents

- Prefer small, focused edits to individual notes rather than mass refactors; keep filenames and links consistent with existing kebab-case conventions.
- When adding new notes, place them under the appropriate topic in [sorted/](sorted/) or in [unsorted/](unsorted/) if the topic is undecided.
