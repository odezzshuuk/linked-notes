---
name: note-writing
description: This skill should be used when writing or editing Markdown notes in the linked-notes knowledge base. It provides structure patterns, formatting conventions, and code example guidelines for creating flat, focused, and well-organized notes.
---

# Note Writing

## Overview

This skill provides guidance for writing structured Markdown notes in the linked-notes knowledge base. It enforces conventions for flat hierarchies, readable formatting, and compilable code examples.

## Core Principles

Follow these principles when writing notes:

1. **Flat hierarchy**: Use only H1 (`#`) for titles and H2 (`##`) for main sections
2. **Focused content**: Keep notes small and focused on a single topic or concept
3. **Link connections**: Use relative Markdown links to connect related notes
4. **Readable lines**: Break long sentences into bullet lists for better readability
5. **Working code**: Ensure all code examples are compilable and properly wrapped

## Note Structure Patterns

Choose the appropriate pattern based on the content type. See `references/structure-patterns.md` for detailed templates.

**For concept/technology notes:**

- What It Is
- Key Features
- What's It For
- How to Use
- When and How to Trigger (if compilation, configuration, or activation is involved)
- Examples
- Tips & Tricks

**For tool usage notes:**

- What It Is
- What's It For
- How to Use
- Examples
- Tips & Tricks

**For workflow/best practices notes:**

- Overview
- Prerequisites
- Step-by-Step Workflow
- Tips & Tricks

## Formatting Guidelines

### Heading Levels

Use only two levels:
- H1 (`#`) for the note title only
- H2 (`##`) for all main sections

When subsections are needed, use **bold text** instead of H3:

```markdown
## How to Use

**Basic pattern:**

Example content here...

**Advanced pattern:**

More content here...
```

### Line Length and Lists

When a line becomes too long (>80-100 characters):
- Break it into a bullet list
- Each bullet should be a concise, single point
- Use clear, complete sentences

Example:

❌ Bad:
```markdown
RefCell<T> is a smart pointer that enforces borrow rules at runtime rather than at compile time and allows you to mutate contents through an immutable reference using interior mutability.
```

✅ Good:
```markdown
Key features:
- Enforces borrow rules at runtime
- Allows mutation through immutable references
- Uses interior mutability pattern
- Tracks borrows dynamically
```

### Code Examples

All code examples must be compilable and demonstrate necessity:

**General principles:**
- Examples should show WHY the technique/feature is needed, not just HOW to use it
- Demonstrate clear advantages or solve specific problems
- Avoid examples that could be solved with simpler alternatives
- Include explanations of why this approach is necessary
- **Explain domain-specific terminology before or immediately after first appearance** When introducing new syntax, attributes, or concepts unique to the technology being documented, provide a brief explanation before showing the code example. 
  - For example, explain `#[test]` or `#[cfg(test)]` in Rust before showing a test code block.
- **One representative example is enough**: Avoid repetitive examples showing the same pattern multiple times. Show one typical case; readers can generalize.
- **Pair code with invocation/trigger**: For compilation, configuration, or activation-related content, place the build command or invocation method immediately after the corresponding code example—not separated into a different section.
- **Keep trigger information adjacent**: Explanation of "when" or "how" a code block is triggered should be next to the code, not elsewhere in the note.

Example—avoid redundancy:

❌ Bad—repetitive examples:
```rust
#[cfg(target_os = "linux")]
fn get_temp() { "/tmp" }

#[cfg(target_os = "macos")]
fn get_temp() { "/var/tmp" }

#[cfg(target_os = "windows")]
fn get_temp() { "C:\\Temp" }
```

✅ Good—one representative example:
```rust
#[cfg(target_os = "linux")]
fn get_temp() { "/tmp" }

#[cfg(not(target_os = "linux"))]
fn get_temp() { /* fallback */ }
```

Example—pair code with invocation:

✅ Good—build command adjacent to code:
```rust
#[cfg(feature = "serde")]
use serde::{Serialize, Deserialize};
```

```bash
cargo build --features "serde"
```

❌ Bad—separated:
```rust
#[cfg(feature = "serde")]
use serde::{Serialize, Deserialize};
```

(Later in a different section...)

To enable the feature, run: `cargo build --features "serde"`

**For Rust:**
- Wrap standalone expressions in `fn main() { ... }`
- Drop borrows explicitly with scopes when needed
- Include necessary `use` statements

**For other languages:**
- Include necessary imports
- Provide complete, runnable examples
- Add comments explaining key points

Example showing necessity:

```rust
use std::cell::RefCell;

struct Cache {
    data: RefCell<Vec<String>>,
}

impl Cache {
    // ✅ Must use &self for API design
    // RefCell enables mutation through immutable reference
    fn get_or_insert(&self, key: &str) -> String {
        let mut cache = self.data.borrow_mut();
        // ... cache logic
    }
}
```

❌ Avoid examples that don't show clear advantages:
- Code that could use `&mut self` instead
- Patterns that could be refactored to simpler alternatives
- Syntax demonstrations without explaining necessity

## File Naming and Links

### Filenames

Use kebab-case, lowercase filenames:
- ✅ `rust-smart-pointer_refcell_t.md`
- ❌ `Rust_Smart_Pointer_RefCell.md`

### Internal Links

Use relative paths to link to other notes:
```markdown
See [`Mutex<T>`](rust-smart-pointer_mutex_t.md) for thread-safe alternative.
```

For in-file anchors:
```markdown
See the [Examples](#examples) section below.
```

### Navigation Section for Order-Independent Sections

When a note contains multiple sibling sections where reading order doesn't matter (e.g. a list of derive macros, HTML elements, CLI flags), add a dedicated navigation section with anchor links immediately before those sections:

```markdown
## <GroupName>

- [Section A](#section-a)
- [Section B](#section-b)
- [Section C](#section-c)

## Section A
...

## Section B
...
```

- The navigation section title should name the group (e.g. `## Derives`, `## Elements`, `## Flags`)
- Anchor slugs follow GitLab-style heading IDs: lowercase, spaces replaced with `-`, special characters stripped
- Place the navigation section directly before the first section it lists, not at the top of the note

### Intra-Note Cross-Reference Links

When a section's content references or depends on another section within the same note, link the referenced term to its section anchor:

```markdown
- `Ord` requires [`Eq`](#partialeq-and-eq) to also be derived
- [`Clone`](#clone) must also be derived alongside `Copy`
```

- Wrap the referenced term in backtick + link syntax `` [`Term`](#anchor) `` when it is a code symbol
- Use plain link syntax `[Term](#anchor)` for non-code terms
- Apply this whenever the relationship is a hard requirement or strong dependency, not just a casual mention

## Quality Checklist

Before completing a note, verify:

- [ ] Uses only H1 and H2 headings
- [ ] No lines exceed 100 characters unless necessary
- [ ] Code examples are wrapped and compilable
- [ ] Examples demonstrate WHY the technique is necessary (not just HOW)
- [ ] No redundant examples that could use simpler alternatives
- [ ] Related notes are linked with relative paths
- [ ] Order-independent section groups have a navigation section with anchor links
- [ ] Intra-note dependencies and requirements are linked to their target section
- [ ] Bullet lists are used for multi-point explanations
- [ ] Filename is kebab-case and lowercase
- [ ] Note is focused on a single topic
- [ ] Domain-specific terminology is explained before or near code examples where first introduced

## References

See `references/structure-patterns.md` for detailed structure templates for each note type.
