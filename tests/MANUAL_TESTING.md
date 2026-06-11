# Manual Testing Guide
## How to Test the AIgenta System

---

## Quick Start: Automated Validation

Before manual testing, run the structural validator:

```bash
python tests/validate.py
```

If this passes, the filesystem is intact. Then proceed to end-to-end tests below.

---

## Test 1: Style Routing

**Goal**: Verify the AI reads the correct Laura style file.

**Steps**:
1. Open any AI assistant (Claude, GPT-4, etc.) with access to the AIgenta folder
2. Ask: *"Write a technical blog post about database indexing using AIgenta"*
3. Verify the AI:
   - Reads `CLAUDE.md`
   - Navigates to `workspaces/writing/CONTEXT.md`
   - Reads `workspaces/writing/styles/technical.md`
   - Creates a file in `workspaces/writing/projects/` with format `YYYY-MM-DD_database-indexing.md`

**Pass Criteria**:
- Output uses imperative sentences
- Includes code blocks with language identifiers
- Avoids vague qualifiers like "simply" or "just"
- Tone matches the Technical Laura style guidelines

---

## Test 2: Rhetoric Device Application

**Goal**: Verify the AI loads and applies rhetorical devices.

**Steps**:
1. Ask: *"Write a persuasive paragraph about why exercise matters, using tricolon and logos"*
2. Verify the AI:
   - Reads `workspaces/writing/rhetoric/tricolon.md`
   - Reads `workspaces/writing/rhetoric/logos.md`
   - Applies both devices in the output

**Pass Criteria**:
- Contains at least one tricolon (rule-of-three structure)
- Uses evidence or logical reasoning
- Devices feel natural, not forced

---

## Test 3: Template-Based Project Creation

**Goal**: Verify templates are usable for generating projects.

**Steps**:
1. Ask: *"Create an article about remote work using the article template"*
2. Verify the AI:
   - Reads `workspaces/writing/templates/article-template.md`
   - Produces output with headline, hook, sections, and CTA
   - Saves to `workspaces/writing/projects/YYYY-MM-DD_remote-work.md`

**Pass Criteria**:
- Follows article structure
- Includes subheadings
- Has a clear call-to-action at the end

---

## Test 4: Cross-Workspace Routing

**Goal**: Verify CLAUDE.md correctly routes to research and code workspaces.

**Steps**:
1. Ask: *"Research the impact of remote work on productivity"*
2. Verify the AI reads `workspaces/research/CONTEXT.md`
3. Ask: *"Document this Python function"* (provide a function)
4. Verify the AI reads `workspaces/code/CONTEXT.md`

**Pass Criteria**:
- Research output cites sources and uses evaluation criteria
- Code documentation includes parameters, return values, and examples

---

## Test 5: Demo UI Smoke Test

**Goal**: Verify `index.html` reflects the current system state.

**Steps**:
1. Open `index.html` in a browser:
   ```bash
   open index.html
   # Or on Linux:
   xdg-open index.html
   ```
2. Click through all 4 tabs

**Pass Criteria**:
- **Style Tester tab**: Shows 10 rhetoric pills (Ethos, Logos, Pathos, Tricolon, Anaphora, Antithesis, Chiasmus, Erotesma, Euphemism, Hyperbole)
- **Project Creator tab**: All 4 templates show "Complete" badge
- **System Status tab**: Lists all completed components (rhetoric 10/10, templates 4/4, APIs 2/2, etc.)

---

## Test 6: Corruption Spot-Check

**Goal**: Ensure no files contain garbled or corrupted content.

**Steps**:
1. Open these files in a text editor and visually scan them:
   - `workspaces/writing/rhetoric/chiasmus.md`
   - `workspaces/writing/rhetoric/antithesis.md`
2. Run the validator, which checks for known corruption markers

**Pass Criteria**:
- Files read as coherent markdown
- No shell heredoc artifacts (`<< 'EOF'`)
- No truncated sentences mid-word
- No random character strings

---

## Test 7: Model-Agnostic Test

**Goal**: Verify AIgenta works with different LLMs.

**Steps**:
1. Test the same prompt with at least two different models
   - Example: Claude 3.5 Sonnet and GPT-4
   - Or local model via Ollama
2. Use prompt: *"Using AIgenta, write a neutral-style article about API design"*

**Pass Criteria**:
- Both models navigate the folder structure correctly
- Both produce output consistent with `styles/neutral.md`
- Quality varies by model capability but structure is followed

---

## Test 8: Memory System Test

**Goal**: Verify memory files are read and updated.

**Steps**:
1. Ask the AI to complete a writing task
2. Ask: *"Update memory/learnings.md with what worked well in that task"*
3. Check the file contents

**Pass Criteria**:
- AI reads existing `memory/learnings.md`
- Appends a new entry without overwriting
- Entry is specific and actionable

---

## Regression Checklist

Before declaring a release ready, confirm:

- [ ] `python tests/validate.py` passes
- [ ] All 10 rhetoric files are readable and coherent
- [ ] All 5 style files are readable and coherent
- [ ] All 4 templates are copy-fill-use ready
- [ ] `index.html` displays correctly in browser
- [ ] At least one end-to-end writing test produces good output
- [ ] README accurately reflects file counts

---

**Last Updated**: 2026-06-08
