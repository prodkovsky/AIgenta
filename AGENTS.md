# AIgenta Agent Guidelines

## Project Overview

AIgenta is a **folder-based AI writing system** that replaces complex agent frameworks with persistent markdown files. It uses a three-layer architecture:

1. **Layer 1**: `CLAUDE.md` — AI entry point and routing
2. **Layer 2**: `workspaces/{writing,research,code}/CONTEXT.md` — workspace-specific guidelines
3. **Layer 3**: Skills, templates, rhetoric devices, and memory within each workspace

**Key principle**: Everything is a markdown file. No build step. No dependencies. Model-agnostic.

---

## Directory Structure

```
AIgenta/
├── CLAUDE.md                    # AI entry point
├── README.md                    # Human-facing documentation
├── SECURITY.md                  # Yolo mode safety rules
├── AGENTS.md                    # This file
├── index.html                   # Static demo UI
├── workspaces/
│   ├── writing/
│   │   ├── CONTEXT.md           # Writing workspace guidelines
│   │   ├── styles/              # Laura persona styles (5 files)
│   │   ├── rhetoric/            # 10 rhetorical devices
│   │   ├── templates/           # Writing templates
│   │   └── projects/            # User writing projects
│   ├── research/                # Research workspace
│   │   └── CONTEXT.md
│   └── code/                    # Code documentation workspace
│       └── CONTEXT.md
├── integrations/apis/           # External API documentation
└── memory/                      # Long-term knowledge
    ├── learnings.md
    └── decisions.md
```

---

## Coding & Content Standards

### Markdown Style
- Use ATX-style headers (`#` not underlines)
- Use `---` for horizontal rules between major sections
- Prefer `-` for unordered lists
- Use fenced code blocks with language identifiers
- Keep lines under 120 characters where practical
- End files with a single newline

### File Naming
- Projects: `YYYY-MM-DD_project-name.md`
- Styles: `style-name.md`
- Rhetoric: `device-name.md`
- Templates: `template-type.md`
- Memory: topical names like `decisions.md`

### Content Depth Standard
Rhetoric files and style files should be comprehensive (~100-200 lines):
- Overview/Definition
- Purpose / When to Use
- Structure / How to Build
- Types/Varieties (if applicable)
- Examples (3-5 famous, 2-3 modern, ❌/✅ pairs)
- Checklist
- Application Note

Templates should be copy-fill-use ready, not bare outlines.

---

## Workspace Rules

### Writing Workspace (`workspaces/writing/`)
- **Read-only**: `styles/` and `rhetoric/` are system assets — modify carefully
- **User-owned**: `projects/` contains user work — treat as read-only unless editing user content
- **System-owned**: `templates/` are meant to be copied and filled

### Research Workspace (`workspaces/research/`)
- For information gathering, source synthesis, and analysis
- No live web searches without explicit user request
- Use local markdown for reference

### Code Workspace (`workspaces/code/`)
- For code documentation, API docs, READMEs
- Do not execute code or run builds without user request
- Documentation-only unless explicitly told otherwise

---

## Safety & Boundaries

Detailed rules are in `SECURITY.md`. Summary:
- Stay within the project directory
- No destructive shell commands (`rm -rf`, etc.)
- No git commits, pushes, or history rewrites
- No secrets or credentials in files
- No network requests to external APIs in yolo mode
- Ask user before any operation outside these boundaries

---

## How to Extend the System

### Add a New Laura Style
1. Create `workspaces/writing/styles/new-style.md`
2. Follow the structure of existing style files
3. Update `workspaces/writing/CONTEXT.md` to list it
4. Update `README.md` style list
5. Update `index.html` style dropdown

### Add a New Rhetoric Device
1. Create `workspaces/writing/rhetoric/device-name.md`
2. Match depth standard (see above)
3. Update `workspaces/writing/CONTEXT.md` device list
4. Update `README.md` rhetoric count
5. Update `index.html` rhetoric pills

### Add a New Template
1. Create `workspaces/writing/templates/template-type.md`
2. Make it copy-fill-use ready
3. Update `workspaces/writing/CONTEXT.md` template list
4. Update `README.md` template status
5. Update `index.html` template cards

### Add a New Workspace
1. Create `workspaces/new-workspace/CONTEXT.md`
2. Add routing in `CLAUDE.md`
3. Add to `README.md` architecture diagram

---

## Testing & Validation

Before considering work complete:
1. **Cross-reference check**: Every path mentioned in docs exists
2. **Sync check**: README accurately reflects file counts
3. **Corruption check**: No truncation, no shell artifacts, no garbled content
4. **Depth check**: Rhetoric files within 20% line-count of each other

---

## Common Pitfalls

- **Ghost references**: Mentioning paths that don't exist yet
- **Documentation drift**: README saying one thing, filesystem showing another
- **Corruption**: Files truncated or containing shell/command artifacts
- **Inconsistent depth**: One rhetoric file at 200 lines, another at 20
- **Orphaned UI**: index.html not updated to reflect new files or counts

---

**Remember**: This system is designed to be simple, portable, and human-readable. When in doubt, prefer clarity over cleverness.
