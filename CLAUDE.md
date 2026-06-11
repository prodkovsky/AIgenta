# AIgenta Writer System
## AI Entry Point & Routing

---

## Identity

You are working with the **AIgenta Writer System**, a folder-based AI workspace designed for model-agnostic, context-rich writing workflows.

**Core Principles:**
- **Persistent Context**: All guidelines, styles, and knowledge live in markdown files
- **Model Agnostic**: Works with any LLM (Claude, GPT-4, Llama 3, Mistral, Qwen, etc.)
- **External API Ready**: Integrations described in markdown, not hardcoded
- **Version Controlled**: Everything is git-trackable
- **Human-Readable**: No complex frameworks, just files you can read and edit

---

## Workspace Routing

This system uses a **three-layer architecture**:

### Layer 1: Top-Level Identity (This File)
You are here. This file defines the system's purpose and routes you to workspaces.

### Layer 2: Workspace Context Files
Navigate to specialized workspaces based on the task:

- **`/workspaces/writing/`** → For all writing tasks (essays, docs, creative writing, technical content)
  - Read `workspaces/writing/CONTEXT.md` for writing-specific guidelines
  - Access Laura styles in `workspaces/writing/styles/`
  - Use rhetoric devices from `workspaces/writing/rhetoric/`

- **`/workspaces/research/`** → For information gathering, synthesis, analysis
  - Read `workspaces/research/CONTEXT.md` for research guidelines

- **`/workspaces/code/`** → For code documentation, technical writing
  - Read `workspaces/code/CONTEXT.md` for code documentation standards

### Layer 3: Skills & Tools
- **Skills**: Reusable markdown files in each workspace (styles, rhetoric devices, templates)
- **Integrations**: External API documentation in `/integrations/apis/`
- **Memory**: Accumulated knowledge in `/memory/`

---

## How to Use This System

When you receive a task:

1. **Read this file** (you're doing it now)
2. **Identify the workspace** (writing, research, or code)
3. **Read that workspace's CONTEXT.md** for specific guidelines
4. **Access skills/tools** as needed from that workspace
5. **Check `/memory/`** for accumulated learnings and decisions
6. **Execute the task** using the context you've gathered
7. **Update memory** if you learn something reusable

---

## Naming Conventions

Files use semantic naming to replace databases:

- **Projects**: `YYYY-MM-DD_project-name.md`
  - Example: `2026-06-07_synthesis-essay.md`
- **Styles**: `style-name.md`
  - Example: `academic.md`, `technical.md`
- **Templates**: `template-type.md`
  - Example: `essay-template.md`
- **Memory**: Topical files like `decisions.md`, `learnings.md`

---

## Current Task Routing

**If the user asks you to write something:**
→ Navigate to `workspaces/writing/CONTEXT.md`

**If the user asks you to research something:**
→ Navigate to `workspaces/research/CONTEXT.md`

**If the user asks you to document code:**
→ Navigate to `workspaces/code/CONTEXT.md`

**If the user asks about integrations or APIs:**
→ Check `integrations/apis/` for relevant documentation

---

## System Philosophy

This system is inspired by Jake Van Clief's folder-based AI workflow, replacing complex agent frameworks with simple, persistent context files. Instead of rebuilding context in every chat, you read the files that matter and maintain continuity across sessions.

**Key advantages:**
- **Token efficient**: Only load context you need
- **Transparent**: Humans can audit what AI sees
- **Portable**: Works anywhere, with any model
- **Maintainable**: Edit a file instead of rebuilding architecture

---

## Quick Start Examples

**User says: "Write a technical blog post about database indexing"**
→ You read: `workspaces/writing/CONTEXT.md`, then `styles/technical.md`, then draft in `projects/`

**User says: "Research recent papers on neural scaling laws"**
→ You read: `workspaces/research/CONTEXT.md`, gather sources, synthesize in `projects/`

**User says: "Document this Python API"**
→ You read: `workspaces/code/CONTEXT.md`, check `templates/`, write docs

---

**Next Step**: Navigate to the appropriate workspace CONTEXT.md based on the user's task.