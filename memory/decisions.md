---
title: Decisions
type: memory
created: 2026-06-08
updated: 2026-06-11
lines: 128
status: active
---
# Decisions
## Architectural & Design Decisions

---

## Purpose

This file records significant decisions about the AIgenta system architecture, file organization, and design philosophy. Each entry includes the decision, the rationale, and the trade-offs accepted.

**Rule**: Record decisions while they're fresh. Future maintainers (including future AI sessions) need to understand why things are the way they are.

---

## Decision Log

### 2026-06-08: Markdown-Only Architecture
**Decision**: The entire system is built from markdown files. No databases, no build steps, no dependencies.

**Rationale**:
- Maximum portability — zip the folder and it works anywhere
- Maximum transparency — humans can read and audit every file
- Maximum compatibility — any LLM can read markdown
- Zero maintenance — no version conflicts, no security patches

**Trade-offs**:
- No dynamic features (search, filtering, user accounts)
- No validation or schema enforcement
- Manual file management required

**Status**: ✅ Implemented

---

### 2026-06-08: Three-Layer Routing System
**Decision**: AI reads `CLAUDE.md` → workspace `CONTEXT.md` → specific skills/tools.

**Rationale**:
- Progressive disclosure — AI loads only what it needs
- Scalable — adding new workspaces doesn't require changing the entry point
- Clear separation of concerns — system, workspace, and skill levels

**Structure**:
```
Layer 1: CLAUDE.md — System identity and routing
Layer 2: workspaces/*/CONTEXT.md — Workspace guidelines
Layer 3: styles/, rhetoric/, templates/, memory/ — Skills and knowledge
```

**Trade-offs**:
- Requires AI to follow routing discipline (cannot enforce)
- Deep nesting means more file reads per task

**Status**: ✅ Implemented

---

### 2026-06-08: Laura Style System
**Decision**: Writing voices are organized as named "Laura" styles — reusable persona files.

**Rationale**:
- Consistent voice across projects
- Mix-and-match flexibility (style + rhetoric)
- Easy to extend — add a new style by creating one file
- Named persona makes it easier for AI to embody the voice

**Current Styles**: Academic, Technical, Poetic, Screenwriter, Neutral

**Trade-offs**:
- Styles can become stale if not updated
- AI might over-constrain creativity with rigid rules
- No automated validation that output matches style

**Status**: ✅ Implemented — 5 styles

---

### 2026-06-08: 10 Rhetorical Devices as Modular Files
**Decision**: Each classical rhetorical device is a standalone markdown file with definition, examples, and application guidance.

**Rationale**:
- AI can load only the devices relevant to the current task
- Consistent depth across devices creates predictable quality
- Devices can be combined (anaphora + tricolon, chiasmus + antithesis)

**Selected Devices**:
1. Ethos, Logos, Pathos (Aristotelian appeals)
2. Tricolon, Anaphora (structural repetition)
3. Antithesis, Chiasmus (contrast and inversion)
4. Erotesma, Hyperbole, Euphemism (language manipulation)

**Trade-offs**:
- 10 devices may be too many or too few for some users
- No automated detection or suggestion of appropriate devices
- Western rhetorical tradition bias — devices from other traditions not included

**Status**: ✅ Implemented — 10 devices at A+ depth

---

### 2026-06-08: Date-Prefixed Project Naming
**Decision**: All projects use `YYYY-MM-DD_project-name.md` format.

**Rationale**:
- Chronological sorting in file explorers
- Easy to identify when work was done
- Prevents name collisions
- Human-readable and git-friendly

**Trade-offs**:
- Projects without fixed dates (evergreen content) feel awkward
- Renaming breaks links if referenced elsewhere
- Dates in filenames can feel bureaucratic

**Status**: ✅ Implemented

---

### 2026-06-08: Static HTML Demo Interface
**Decision**: Include `index.html` as a visual demonstration of the system.

**Rationale**:
- Immediate visual understanding for new users
- Showcases style and rhetoric combinations
- Serves as a "business card" for the project

**Trade-offs**:
- Static file — not functional without backend integration
- Must be manually updated when files change
- Adds a non-markdown file to a markdown-centric project

**Status**: ✅ Implemented

---

### 2026-06-08: Model-Agnostic Design
**Decision**: No hardcoded integration with any single LLM provider.

**Rationale**:
- Works with Claude, GPT-4, Llama, Mistral, Qwen, Gemini, etc.
- Users can switch models without changing system files
- Future-proof as new models emerge
- Local and cloud options both supported

**Trade-offs**:
- No model-specific optimizations
- API integration docs are generic examples, not tested code
- Different models follow style instructions with varying fidelity

**Status**: ✅ Implemented — docs for OpenRouter and Ollama

---

### 2026-06-08: SECURITY.md for Yolo Mode
**Decision**: Added explicit safety boundaries for auto-approved execution.

**Rationale**:
- Yolo mode removes human approval friction
- Project-scoped rules prevent accidental damage
- Self-documenting — AI reads the file and follows it

**Trade-offs**:
- Rules are advisory — cannot be technically enforced
- May be overly restrictive for some workflows
- Requires maintenance as project evolves

**Status**: ✅ Implemented

---

## Open Questions

| Question | Context | Status |
|----------|---------|--------|
| Should we add a `workspaces/writing/editors/` folder? | Editing checklists and revision workflows | Under consideration |
| Should styles include more non-Western voices? | Academic, technical voices are Western-centric | Under consideration |
| Should we add automated validation? | Script to check file counts, corruption, sync | Under consideration |
| Should projects support subdirectories? | Series or multi-chapter works | Under consideration |

---

**Last Updated**: 2026-06-08
