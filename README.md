# AIgenta Writer System
## Folder-Based AI Writing Workspace

---

## Overview

AIgenta is a **folder-based AI writing system** inspired by Jake Van Clief's approach to replacing complex agent frameworks with simple, persistent markdown files. Instead of building AI agents with complex protocols, AIgenta uses a three-layer file-based architecture that works with **any LLM** (Claude, GPT-4, Llama 3, Mistral, Qwen, etc.).

---

## Core Philosophy

**Problems Solved:**
- ❌ **Chat Loop Hell**: Opening ChatGPT → paste prompt → lose context → repeat
- ❌ **Agent Framework Overhead**: Complex TypeScript protocols, tRPC routers, agent buses
- ❌ **Model Lock-in**: Tightly coupled to specific LLM providers
- ❌ **Token Waste**: Rebuilding context every conversation

**AIgenta Advantages:**
- ✅ **Persistent Context**: Your project structure, guidelines, and knowledge live in markdown files
- ✅ **Model Agnostic**: Works with any LLM that can read files
- ✅ **Token Efficient**: AI loads only what it needs from organized files
- ✅ **Version Controlled**: Everything is git-trackable
- ✅ **Human-Readable**: No frameworks, just files you can read and edit
- ✅ **External API Ready**: Integrations described in markdown, not hardcoded

---

## System Architecture

### Three-Layer Routing System

```
AIgenta/
│
├── Layer 1: Top-Level Identity
│   └── CLAUDE.md                    # AI entry point - routing logic
│
├── Layer 2: Workspace Context Files
│   └── workspaces/
│       └── writing/
│           ├── CONTEXT.md           # Writing-specific guidelines
│           ├── styles/              # Laura persona system
│           ├── rhetoric/            # 10 rhetorical devices
│           ├── projects/            # Actual writing projects
│           └── templates/           # Reusable templates
│
└── Layer 3: Skills & Tools
    ├── integrations/apis/           # External API docs
    └── memory/                      # Long-term knowledge base
```

---

## What's Included

### ✅ Core System Files

- **CLAUDE.md**: AI entry point with routing instructions
- **workspaces/writing/CONTEXT.md**: Writing workspace guidelines

### ✅ Laura Style System (5 Voices)

Located in `workspaces/writing/styles/`:

1. **academic.md** - Scholarly, citation-heavy, formal analysis
2. **technical.md** - Clear, precise, documentation-focused
3. **poetic.md** - Metaphorical, rhythmic, evocative
4. **screenwriter.md** - Dialogue-driven, visual, dramatic
5. **neutral.md** - Balanced, approachable, general-purpose

### ✅ Rhetorical Devices (3 of 10)

Located in `workspaces/writing/rhetoric/`:

1. **ethos.md** - Credibility and authority
2. **logos.md** - Logic and evidence  
3. **pathos.md** - Emotional appeal

*Note: 7 additional devices ready to be added (tricolon, erotesma, antithesis, anaphora, chiasmus, hyperbole, euphemism)*

---

## How to Use

### Step 1: AI Reads CLAUDE.md
When an AI assistant (Claude, GPT-4, etc.) opens this workspace, it first reads `CLAUDE.md` which:
- Explains the system's purpose
- Routes to appropriate workspaces based on the task
- Provides naming conventions and workflow guidance

### Step 2: Navigate to Workspace
For writing tasks, AI navigates to:
```
workspaces/writing/CONTEXT.md
```

This file explains:
- Laura style system
- Rhetorical devices
- Writing workflow
- File organization

### Step 3: Access Skills
AI reads relevant style/rhetoric files:
```
workspaces/writing/styles/technical.md
workspaces/writing/rhetoric/logos.md
```

### Step 4: Execute Task
AI writes content following the gathered context, saving to:
```
workspaces/writing/projects/2026-06-08_project-name.md
```

---

## Quick Start Examples

### Example 1: Write a Technical Blog Post
**User**: "Write a technical blog post about database indexing"

**AI Flow**:
1. Reads `CLAUDE.md` → routes to writing workspace
2. Reads `workspaces/writing/CONTEXT.md` → understands workflow
3. Reads `styles/technical.md` → applies technical style
4. Reads `rhetoric/logos.md` → uses logic/evidence
5. Creates `projects/2026-06-08_database-indexing.md`

### Example 2: Write a Poetic Essay
**User**: "Write a poetic reflection on memory"

**AI Flow**:
1. Reads `CLAUDE.md` → routes to writing workspace
2. Reads `workspaces/writing/CONTEXT.md`
3. Reads `styles/poetic.md` → applies poetic style
4. Reads `rhetoric/pathos.md` → uses emotional appeal
5. Creates `projects/2026-06-08_memory-reflection.md`

---

## Naming Conventions

Files use semantic naming to replace databases:

- **Projects**: `YYYY-MM-DD_project-name.md`
  - Example: `2026-06-08_synthesis-essay.md`
- **Styles**: `style-name.md`
  - Example: `academic.md`, `technical.md`
- **Templates**: `template-type.md`
  - Example: `essay-template.md`
- **Memory**: Topical files like `decisions.md`, `learnings.md`

---

## Extending the System

### Add New Laura Styles
Create `workspaces/writing/styles/your-style.md`:
```markdown
# Your Style Name
## Brief Description

## Tone Characteristics
- Characteristic 1
- Characteristic 2

## Vocabulary
### Preferred Terms
### Avoid

## Examples
...
```

### Add New Rhetoric Devices
Create `workspaces/writing/rhetoric/device-name.md`:
```markdown
# Device Name
## Short Definition

## When to Use
## Examples
## Application Note
```

### Add API Integrations
Create `integrations/apis/service-name.md`:
```markdown
# Service Name API
## Authentication
## Endpoints
## Usage Examples
```

---

## Why This Works

### Token Efficiency
Instead of pasting your entire style guide into every chat, AI reads just the files it needs:
- Writing task? Load `CONTEXT.md` + relevant style
- 10 files × 1KB each = 10KB context
- vs. pasting 50KB every time

### Model Agnostic
Works with:
- **Cloud LLMs**: Claude, GPT-4, Gemini
- **Open Source**: Llama 3, Mistral, Qwen
- **Local**: Ollama, LM Studio
- **APIs**: OpenRouter, Together AI

### Portable
- Zip the folder → works anywhere
- Git clone → instant setup
- No npm install, no dependencies
- Just markdown files

---

## Project Status

### ✅ Completed
- [x] CLAUDE.md entry point with routing
- [x] SECURITY.md yolo mode safety rules
- [x] AGENTS.md contributor guidelines
- [x] Writing workspace context file
- [x] Research workspace context file
- [x] Code workspace context file
- [x] All 5 Laura writing styles (Academic, Technical, Poetic, Screenwriter, Neutral)
- [x] All 10 rhetorical devices at A+ depth (Ethos, Logos, Pathos, Tricolon, Anaphora, Antithesis, Chiasmus, Erotesma, Euphemism, Hyperbole)
- [x] 4 writing templates (Essay, Article, Screenplay, Technical Doc)
- [x] API integration docs (OpenRouter, Ollama)
- [x] Memory system (decisions.md, learnings.md)
- [x] Documentation (this README)
- [x] Demo UI (index.html)

### 🚧 Future Extensions
- [ ] Additional Laura styles (Journalistic, Conversational, etc.)
- [ ] More API integrations (Together AI, Anthropic direct, etc.)
- [ ] Automated validation scripts
- [ ] Multi-language support

---

## Comparison to Particulate Foundry

You previously built **Particulate Foundry** - a sophisticated multi-agent system with:
- Agent Bus, Registry, Service Directory
- MCP integration
- tRPC routers
- Complex TypeScript protocols

**AIgenta takes a different approach:**

| Particulate Foundry | AIgenta |
|---------------------|---------|
| Agent-based architecture | File-based architecture |
| TypeScript protocols | Markdown files |
| Runtime complexity | Zero runtime |
| Model-specific | Model-agnostic |
| Requires build | No build needed |
| Hard to port | Copy/paste ready |

**Both are valid** - Foundry for complex systems, AIgenta for simplicity and portability.

---

## Next Steps

1. **Use the system** — Create your first project in `workspaces/writing/projects/`
2. **Extend styles** — Add new Laura styles for your specific needs
3. **Add integrations** — Connect your preferred LLM provider
4. **Build memory** — Record learnings and decisions as you work
5. **Contribute** — Share improvements back to the system

---

## Testing

AIgenta includes lightweight testing that matches its zero-dependency philosophy.

### Automated Validation

Run the structural validator to check file integrity, content depth, corruption, and documentation sync:

```bash
python tests/validate.py
```

This checks:
- All expected files and directories exist
- Rhetoric files are within depth range (80–220 lines)
- No corruption artifacts are present
- README and index.html reflect actual file counts
- Cross-referenced paths are valid

### Manual Testing

See `tests/MANUAL_TESTING.md` for step-by-step end-to-end tests, including:
- Style routing tests
- Rhetoric device application tests
- Template-based project creation
- Cross-workspace routing
- Demo UI smoke test
- Model-agnostic verification

---

## Inspiration & Credits

- **Jake Van Clief**: Folder-based AI workflow concept
  - Video: "Stop Building AI Agents. Use This Folder System Instead"
- **Your Particulate Foundry**: Laura system, rhetoric devices, writing workflows
- **Model Context Protocol**: Inspiration for modular tool design

---

## License

This is a template system. Use it, modify it, extend it as you wish.

---

**Built on**: 2026-06-08  
**Location**: /Volumes/ON/AIgent/AIgenta  
**Purpose**: A simpler, more maintainable approach to AI-assisted writing