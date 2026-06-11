# Yolo Mode Security Guidelines
## AIgenta Project — Scoped Safety Rules

---

## Purpose

These guidelines govern AI agent behavior when operating in **yolo mode** (auto-approved execution) within the AIgenta project. They are **project-scoped only** and apply exclusively to `/Volumes/ON/AIgent/AIgenta/` and its subdirectories.

---

## 1. Boundary Rules

### ✅ Allowed
- Create, read, update, and delete markdown files within the project directory
- Create subdirectories for workspaces, skills, templates, and projects
- Run non-destructive shell commands (`ls`, `cat`, `find`, `wc`, `mkdir`)
- Generate content (text, markdown, HTML, CSS) for the writing system
- Validate file structure and cross-references

### ❌ Forbidden
- **Never** modify files outside the project directory (`../`, `/etc/`, `~/.bashrc`, etc.)
- **Never** run destructive shell commands (`rm -rf`, `dd`, `mkfs`, `chmod -R 777 /`)
- **Never** execute downloaded scripts or binaries
- **Never** install system-wide packages or modify global configuration
- **Never** access, read, or write sensitive files (`.env`, `id_rsa`, `credentials`, API keys)
- **Never** make git commits, pushes, rebases, or any repository mutations

---

## 2. File System Safety

### Read Scope
- Only read files within the project tree
- Only read files relevant to the current task

### Write Scope
- Only write to paths that are part of the AIgenta system architecture
- Prefer creating new files over overwriting existing ones
- When overwriting is necessary, preserve the original intent and structure

### Destructive Operations
Before any file deletion or directory removal:
1. Verify the path is within the project directory
2. Confirm the item is not tracked or referenced by other files
3. Prefer archiving (`mv old.md old.md.bak`) over deletion

---

## 3. Content Safety

### Generated Content
- All generated content must be safe, legal, and non-harmful
- No generation of malware, exploits, or instructions for illegal activities
- No generation of hate speech, harassment, or discriminatory content
- Writing styles and rhetoric devices must be used for legitimate creative/technical purposes only

### External Data
- Do not fetch live data from the internet unless explicitly requested
- Do not call external APIs (OpenRouter, Ollama, etc.) in yolo mode
- If API documentation is needed, read the local markdown files in `integrations/apis/`

---

## 4. Network & Execution Safety

### Shell Commands
- **Allowed**: `ls`, `cat`, `find`, `wc`, `mkdir`, `touch`, `cp`, `mv`, `diff`, `grep`, `head`, `tail`
- **Forbidden**: `curl | bash`, `wget` to executable, `sudo`, `su`, `ssh`, `nc`, `nmap`, any network listener
- **Forbidden**: `rm` with wildcards, `find . -exec rm`, `xargs rm`

### Background Tasks
- Background tasks are allowed for long-running operations within the project
- Must include clear descriptions and reasonable timeouts
- Must not spawn persistent services or daemons

---

## 5. Git & Version Control

- **Never** run `git commit`, `git push`, `git reset`, `git rebase`, `git merge`
- **Never** modify `.git/` directory contents
- **Never** force-push or rewrite history
- If git operations are needed, ask the user for explicit confirmation

---

## 6. Secrets & Credentials

- **Never** create, read, or write files containing API keys, passwords, tokens, or private credentials
- If a secrets file is needed (e.g., for API integration docs), use placeholder values only:
  ```
  API_KEY=your_api_key_here
  ```
- If an existing secrets file is found, do not read its contents

---

## 7. Workspace-Specific Rules

### Writing Workspace
- Content in `projects/` is user work product — treat as read-only unless asked to edit
- Styles and rhetoric files are system assets — modify carefully, preserve structure

### Research Workspace
- Do not execute live web searches without user request
- Use local markdown for reference; internet is opt-in only

### Code Workspace
- Do not execute code or run build processes without user request
- Documentation-only workspace unless explicitly told otherwise

---

## 8. Escalation Rules

If any of the following occur, **stop execution and ask the user**:
- A task requires modifying files outside the project directory
- A task requires destructive operations on git history
- A task requests access to or generation of secrets/credentials
- A task involves network requests to external APIs
- Ambiguity about whether an operation is safe

---

## 9. Audit Trail

When operating in yolo mode:
- Prefer explicit file writes over shell-based text manipulation
- Use `WriteFile` and `StrReplaceFile` for changes (self-documenting)
- Avoid `sed` or `awk` for file modifications when purpose-built tools exist
- Keep changes minimal and focused

---

**Scope**: These rules apply only to the AIgenta project at `/Volumes/ON/AIgent/AIgenta/`
**Effective**: Immediately
**Enforced by**: Agent self-check before every tool call
