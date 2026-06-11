# Writing Workspace Context
## Guidelines for Writing Tasks

---

## Purpose

This workspace handles all writing tasks: essays, articles, documentation, creative writing, screenplays, and technical content.

---

## Laura Style System

**Laura** is our writing persona/style system. Each Laura style is a reusable voice profile that shapes tone, structure, and rhetorical approach.

### Available Styles

Located in `workspaces/writing/styles/`:

1. **Academic** - Scholarly, citation-heavy, formal analysis
2. **Technical** - Clear, precise, documentation-focused
3. **Poetic** - Metaphorical, rhythmic, evocative
4. **Screenwriter** - Dialogue-driven, visual, dramatic
5. **Neutral** - Balanced, approachable, general-purpose

### How to Use Laura Styles

When the user requests a specific style:
1. Read the corresponding style file (e.g., `styles/academic.md`)
2. Apply its guidelines to your writing
3. Use its vocabulary, sentence patterns, and rhetorical devices
4. Match its tone and structure expectations

---

## Rhetorical Devices

Located in `workspaces/writing/rhetoric/`:

We maintain 10 classical rhetorical devices as reusable tools. Each device has:
- Definition
- When to use it
- Examples
- Writing patterns

**The 10 Devices:**
1. **Ethos** - Credibility and authority
2. **Logos** - Logic and evidence
3. **Pathos** - Emotional appeal
4. **Tricolon** - Rule of three
5. **Erotesma** - Rhetorical question
6. **Antithesis** - Contrasting ideas
7. **Anaphora** - Repetition at beginning
8. **Chiasmus** - Inverted structure (AB-BA)
9. **Hyperbole** - Exaggeration for effect
10. **Euphemism** - Indirect expression

---

## Writing Workflow

### Standard Process

1. **Understand the request**
   - What type of writing? (essay, article, screenplay, etc.)
   - What style? (check if Laura style is specified)
   - What rhetorical approach? (persuasive, informative, narrative, etc.)

2. **Gather context**
   - Read relevant style files if style is specified
   - Check rhetoric devices if persuasive writing
   - Review templates in `templates/` for structure guidance
   - Check `memory/learnings.md` for past insights

3. **Draft the content**
   - Apply the chosen Laura style
   - Use appropriate rhetorical devices
   - Follow project naming convention: `YYYY-MM-DD_project-name.md`
   - Save in `workspaces/writing/projects/`

4. **Refine**
   - Ensure consistency with style guidelines
   - Verify rhetorical device usage
   - Check tone, structure, and flow

---

## Templates

Located in `workspaces/writing/templates/`:

- **essay-template.md** - Standard essay structure
- **article-template.md** - Blog/article format
- **screenplay-template.md** - Screenplay format
- **technical-doc-template.md** - Technical documentation

---

## File Organization

### Projects
`workspaces/writing/projects/YYYY-MM-DD_project-name.md`

Examples:
- `2026-06-07_database-indexing-article.md`
- `2026-06-07_synthesis-essay.md`

### Styles
`workspaces/writing/styles/style-name.md`

### Rhetoric
`workspaces/writing/rhetoric/device-name.md`

### Templates
`workspaces/writing/templates/template-type.md`

---

## Integration with External APIs

For LLM-enhanced writing:
- Check `integrations/apis/` for available LLM providers
- Use them for style analysis, text refinement, or generation
- Document API usage in project files

---

## Memory & Learning

After completing writing tasks:
- Update `memory/learnings.md` with reusable insights
- Note successful patterns, phrases, or structures
- Record user preferences for future tasks

---

## Quick Commands

**To write in a specific style:**
→ Read `styles/{style-name}.md` first, then apply guidelines

**To use rhetorical devices:**
→ Read `rhetoric/{device-name}.md` for usage patterns

**To start from a template:**
→ Copy from `templates/{template-type}.md` and fill in

**To check past projects:**
→ Browse `projects/` folder by date

---

**Next Action**: Based on user's writing request, select appropriate style, devices, and templates, then draft content.