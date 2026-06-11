# AIgenta System Manifest
## Single Source of Truth for Content

---

## Purpose

This file serves as the authoritative source for all content in the AIgenta system. It is machine-readable (tables) and human-readable (markdown). All documentation (README.md, index.html) and validation scripts should derive their information from this manifest.

**Rule**: When adding/removing files, update this manifest first, then update other documentation.

---

## Last Updated
- **Date**: 2026-06-11
- **Updated by**: System validation

---

## System Files

| File | Purpose | Lines | Status |
|------|---------|-------|--------|
| CLAUDE.md | AI entry point and routing | 116 | Active |
| README.md | Human-facing documentation | 329 | Active |
| SECURITY.md | Yolo mode safety rules | TBD | Active |
| AGENTS.md | Contributor guidelines | TBD | Active |
| index.html | Static demo UI | 524 | Active |
| studio.html | Additional UI | TBD | Active |
| .gitignore | Git exclusions | TBD | Active |

---

## Workspaces

| Workspace | Path | Purpose | Context Lines | Status |
|-----------|------|---------|---------------|--------|
| Writing | workspaces/writing/ | Writing tasks, styles, rhetoric | 153 | Active |
| Research | workspaces/research/ | Research and analysis | 166 | Active |
| Code | workspaces/code/ | Code documentation | 230 | Active |

---

## Writing Workspace: Styles

| Style Name | Path | Lines | Last Updated | Status |
|------------|------|-------|--------------|--------|
| Academic | workspaces/writing/styles/academic.md | 139 | 2026-06-08 | Active |
| Technical | workspaces/writing/styles/technical.md | 221 | 2026-06-08 | Active |
| Poetic | workspaces/writing/styles/poetic.md | 206 | 2026-06-08 | Active |
| Screenwriter | workspaces/writing/styles/screenwriter.md | 359 | 2026-06-08 | Active |
| Neutral | workspaces/writing/styles/neutral.md | 245 | 2026-06-08 | Active |

**Total Styles**: 5/5

---

## Writing Workspace: Rhetorical Devices

| Device Name | Path | Lines | Type | Last Updated | Status |
|-------------|------|-------|------|--------------|--------|
| Ethos | workspaces/writing/rhetoric/ethos.md | 195 | Aristotelian | 2026-06-08 | Active |
| Logos | workspaces/writing/rhetoric/logos.md | 151 | Aristotelian | 2026-06-08 | Active |
| Pathos | workspaces/writing/rhetoric/pathos.md | 116 | Aristotelian | 2026-06-08 | Active |
| Tricolon | workspaces/writing/rhetoric/tricolon.md | 99 | Structural | 2026-06-08 | Active |
| Anaphora | workspaces/writing/rhetoric/anaphora.md | 195 | Structural | 2026-06-08 | Active |
| Antithesis | workspaces/writing/rhetoric/antithesis.md | 173 | Contrast | 2026-06-08 | Active |
| Chiasmus | workspaces/writing/rhetoric/chiasmus.md | 148 | Inversion | 2026-06-08 | Active |
| Erotesma | workspaces/writing/rhetoric/erotesma.md | 155 | Question | 2026-06-08 | Active |
| Euphemism | workspaces/writing/rhetoric/euphemism.md | 171 | Language | 2026-06-08 | Active |
| Hyperbole | workspaces/writing/rhetoric/hyperbole.md | 195 | Language | 2026-06-08 | Active |

**Total Devices**: 10/10

---

## Writing Workspace: Templates

| Template Name | Path | Lines | Category | Last Updated | Status |
|---------------|------|-------|----------|--------------|--------|
| Essay Template | workspaces/writing/templates/essay-template.md | 133 | Academic | 2026-06-08 | Active |
| Article Template | workspaces/writing/templates/article-template.md | 167 | Blog | 2026-06-08 | Active |
| Screenplay Template | workspaces/writing/templates/screenplay-template.md | 243 | Creative | 2026-06-08 | Active |
| Technical Doc Template | workspaces/writing/templates/technical-doc-template.md | 276 | Technical | 2026-06-08 | Active |

**Total Templates**: 4/4

---

## Writing Workspace: Projects

| Project Name | Path | Lines | Date | Status |
|--------------|------|-------|------|--------|
| AIgenta Overview | workspaces/writing/projects/2026-06-08_aigenta-overview.md | TBD | 2026-06-08 | Active |

**Total Projects**: 1

---

## Research Workspace: Methods

| Method Name | Path | Lines | Purpose | Status |
|-------------|------|-------|---------|--------|
| *None yet* | - | - | - | Pending |

**Total Methods**: 0

---

## Research Workspace: Sources

| Source Name | Path | Lines | Date | Status |
|-------------|------|-------|------|--------|
| *None yet* | - | - | - | Pending |

**Total Sources**: 0

---

## Research Workspace: Templates

| Template Name | Path | Lines | Category | Status |
|---------------|------|-------|----------|--------|
| *None yet* | - | - | - | Pending |

**Total Templates**: 0

---

## Research Workspace: Projects

| Project Name | Path | Lines | Date | Status |
|--------------|------|-------|------|--------|
| *None yet* | - | - | - | Pending |

**Total Projects**: 0

---

## Code Workspace: Patterns

| Pattern Name | Path | Lines | Purpose | Status |
|--------------|------|-------|---------|--------|
| *None yet* | - | - | - | Pending |

**Total Patterns**: 0

---

## Code Workspace: Templates

| Template Name | Path | Lines | Category | Status |
|---------------|------|-------|----------|--------|
| *None yet* | - | - | - | Pending |

**Total Templates**: 0

---

## Code Workspace: Projects

| Project Name | Path | Lines | Date | Status |
|--------------|------|-------|------|--------|
| *None yet* | - | - | - | Pending |

**Total Projects**: 0

---

## API Integrations

| API Name | Path | Lines | Provider | Status |
|----------|------|-------|----------|--------|
| OpenRouter | integrations/apis/openrouter.md | 208 | OpenRouter | Active |
| Ollama | integrations/apis/ollama.md | 267 | Ollama | Active |

**Total APIs**: 2/2

---

## Memory Files

| Memory Name | Path | Lines | Last Updated | Status |
|-------------|------|-------|--------------|--------|
| Decisions | memory/decisions.md | 181 | 2026-06-08 | Active |
| Learnings | memory/learnings.md | 95 | 2026-06-08 | Active |

**Total Memory Files**: 2/2

---

## Testing

| Test File | Path | Purpose | Status |
|-----------|------|---------|--------|
| Validation Script | tests/validate.py | 456 | Active |
| Manual Testing | tests/MANUAL_TESTING.md | TBD | Active |

---

## Directories

| Directory | Purpose | Status |
|-----------|---------|--------|
| workspaces/writing/ | Writing workspace | Active |
| workspaces/writing/styles/ | Laura styles | Active |
| workspaces/writing/rhetoric/ | Rhetorical devices | Active |
| workspaces/writing/templates/ | Writing templates | Active |
| workspaces/writing/projects/ | Writing projects | Active |
| workspaces/research/ | Research workspace | Active |
| workspaces/code/ | Code documentation workspace | Active |
| integrations/apis/ | API integration docs | Active |
| memory/ | Long-term knowledge | Active |
| tests/ | Testing infrastructure | Active |

---

## Quality Thresholds

| Content Type | Min Lines | Max Lines | Current Status |
|--------------|-----------|-----------|----------------|
| Rhetoric Devices | 80 | 220 | ✅ All within range |
| Styles | 100 | - | ✅ All meet minimum |
| Templates | 100 | - | ✅ All meet minimum |
| Context Files | 50 | - | ✅ All meet minimum |
| API Docs | 30 | - | ✅ All meet minimum |
| Memory Files | 30 | - | ✅ All meet minimum |

---

## Next Steps

1. ✅ Update line counts for all files marked "TBD"
2. ✅ Add GitHub Actions workflow
3. Create Research workspace methods, templates
4. Create Code workspace patterns, templates
5. Create CLI tool for manifest updates

---

**Manifest Version**: 1.0.1
**System Version**: 0.1.0