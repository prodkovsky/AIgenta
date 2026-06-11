---
title: Learnings
type: memory
created: 2026-06-08
updated: 2026-06-11
lines: 67
status: active
---
# Learnings
## Accumulated Knowledge & Insights

---

## Purpose

This file captures reusable insights, patterns, and discoveries from completed AIgenta tasks. It serves as institutional memory — preventing the need to relearn what has already been figured out.

**Rule**: Every insight should be actionable. Vague observations don't help future sessions.

---

## Writing Patterns

### Effective Openings
- **Question hooks** work best for persuasive pieces (engages reader intellectually)
- **Image hooks** work best for poetic/reflective pieces (engages senses)
- **Stat hooks** work best for technical/business pieces (establishes stakes)
- **Avoid**: "Since the beginning of time..." and "In today's world..." — both are cliché openers

### Style Combinations That Work
| Primary Style | Rhetoric Device | Use Case |
|---------------|-----------------|----------|
| Technical + Logos | API documentation, tutorials |
| Neutral + Tricolon | Blog posts, articles |
| Academic + Ethos + Logos | Research papers, grant proposals |
| Poetic + Pathos | Memoir, creative essays |
| Screenwriter + Visual metaphor | Scenes, dramatic narratives |

### Common Revision Patterns
- First drafts are usually 20-30% too long — trim aggressively
- Transitions are where most first drafts fail — add explicit bridges
- Passive voice creeps in during drafting — audit specifically for it

---

## Rhetoric Insights

### Device Pairings
- **Anaphora + Tricolon**: Maximum rhythmic impact ("We want X. We want Y. We want Z.")
- **Chiasmus + Antithesis**: Sharp, memorable conclusions
- **Logos + Ethos**: Essential for any persuasive writing claiming credibility
- **Pathos + Hyperbole**: Emotional intensity, but risks melodrama if overused

### When Devices Backfire
- Anaphora beyond 5 repetitions feels mechanical
- Chiasmus that sounds forced is worse than no device
- Euphemism in technical writing creates ambiguity
- Hyperbole in legal or medical contexts undermines trust

---

## User Preferences

*(To be populated as patterns emerge from user interactions)*

| Date | Preference | Context |
|------|------------|---------|
| — | — | — |

---

## Tool & Integration Notes

### OpenRouter
- `anthropic/claude-3.5-sonnet` consistently produces the best creative writing
- `openrouter/auto` is reliable fallback but unpredictable for style adherence
- Temperature 0.7 is the sweet spot for creative tasks; 0.3 for technical

### Ollama
- `llama3.1:8b` is fast enough for drafting but needs revision
- `qwen2.5:14b` surprisingly good at following complex style instructions
- Local models struggle with very long context ( > 8K tokens) — summarize style files first

---

## System Evolution Notes

### Decisions
*(Link to `memory/decisions.md` for architectural choices)*

### What Worked
- Three-layer routing (CLAUDE.md → CONTEXT.md → skills) — simple and effective
- Date-prefixed project names — easy to browse chronologically
- Separating styles from rhetoric — allows mix-and-match

### What to Improve
- Consider adding a `workspaces/writing/editors/` folder for editing checklists
- Research workspace needs a source evaluation rubric template
- Code workspace needs language-specific subdirectories

---

**Last Updated**: 2026-06-08
