# Work With LLM Agent

## `.prompt.md`

What's For

- Reusable, on-demand prompts for common tasks (generate code, review code, scaffold, etc.). Prompt files are standalone prompts you run in chat, and can include instructions, variables, and tool configuration.

Where to create

- Workspace scope: `.github/prompts/` (default). Add more locations via the `chat.promptFilesLocations` setting.
- User scope: your VS Code profile folder(~/.config/Code/User/prompts), available across workspaces

How to use

- Create a prompt file from Chat (Configure Chat → Prompt Files → New) or via the command palette.
- Write YAML frontmatter (optional) for metadata like `name`, `description`, `agent`, `tools`, and `model`.
- Run it in chat by typing `/prompt-name`, using Chat: Run Prompt, or the play button in the editor.

## `AGENTS.md`

What's For

- Workspace-wide custom instructions that apply to all agents. Useful when **Multiple** AI agents collaborate on the same repo.

Where to create

- Root of the workspace: `AGENTS.md`.
- Optional (experimental): additional `AGENTS.md` files in subfolders when `chat.useNestedAgentsMdFiles` is enabled.

How to use

Enable with `chat.useAgentsMdFile`. Keep instructions clear and general so they apply across tasks. Use links to point to repo conventions or workflows.

## `copilot-instructions.md`

What's For

- Project-wide custom instructions that automatically apply to all Copilot chat requests in the workspace.

Where to create

- Auto generate by Command `Chat: Generate Workspace Instructions File`
- `.github/copilot-instructions.md` at the workspace root.

How to use

- Enable `github.copilot.chat.codeGeneration.useInstructionFiles`.
- Write concise, actionable rules in Markdown.
- Use links to reference additional context instead of duplicating content.

## SKILLS.md

What's For

- Agent Skills: reusable, specialized workflows that Copilot can load on demand. Skills can include instructions plus scripts, examples, and resources.

Where to create

- Workspace skills: `.github/skills/<skill-name>/SKILL.md` (recommended).
- User skills: `~/.copilot/skills/<skill-name>/SKILL.md` (recommended).

How to use

- Define `name` and `description` in YAML frontmatter to help discovery.
- Put step-by-step instructions and examples in the body.
- Enable with `chat.useAgentSkills`. Copilot loads relevant skills automatically based on your request.

## MCP

What's For

- Model Context Protocol (MCP) connects Copilot to external tools and services (APIs, databases, file systems). MCP servers provide tools and resources that can be invoked in chat.

Where to create

- Install from the MCP server registry (Extensions view) or configure in `mcp.json` (workspace or user config).
- Servers can also be configured in dev containers or auto-discovered.

How to use

- Start the server and select its tools in the chat tool picker.
- Invoke tools automatically in agent mode or explicitly with `#tool-name`.
- Add MCP resources via Add Context → MCP Resources.
