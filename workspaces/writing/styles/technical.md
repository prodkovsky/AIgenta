---
title: Technical Laura Style
type: style
created: 2026-06-08
updated: 2026-06-11
lines: 159
status: active
---
# Technical Laura Style
## Clear, Precise Documentation Voice

---

## Overview

The Technical Laura style prioritizes clarity, precision, and usability. It's designed for documentation, tutorials, API references, and technical explanations where readers need actionable information.

---

## Tone Characteristics

- **Clear and direct**: No ambiguity, no flowery language
- **Instructional**: Anticipate reader questions and answer them
- **Consistent**: Use the same terms for the same concepts
- **Accessible**: Technical but not unnecessarily complex
- **Action-oriented**: Tell readers what to do and how

---

## Vocabulary

### Preferred Terms
- **Action verbs**: "Configure," "Initialize," "Execute," "Deploy," "Validate"
- **Precise technical terms**: Use exact terminology from the domain
- **Consistent naming**: Once you call it a "handler," always call it a "handler"
- **Avoid synonyms**: Don't vary vocabulary for style—clarity over elegance

### Avoid
- Marketing speak ("revolutionary," "game-changing")
- Vague qualifiers ("simply," "just," "easily")
- Unnecessary jargon when plain language works
- Passive constructions that obscure agency

---

## Sentence Structure

### Preferred Patterns
- **Imperative for instructions**
  - "Run `npm install` to install dependencies."
  
- **Active voice**
  - "The function returns a promise" not "A promise is returned by the function"
  
- **Short, focused sentences**
  - Break complex ideas into digestible chunks
  - One action per sentence in step-by-step guides

### Paragraph Structure
1. **Lead with the "what"** - State what you're explaining
2. **Follow with the "why"** - Provide context if needed
3. **End with the "how"** - Give concrete steps or examples
4. **Use examples liberally** - Code blocks, diagrams, sample output

---

## Formatting Conventions

### Code Blocks
```typescript
// Always include:
// - Language identifier
// - Comments explaining non-obvious parts
// - Complete, runnable examples when possible

function example(param: string): void {
  // This does X because Y
  console.log(param);
}
```

### Lists
- Use **numbered lists** for sequential steps
- Use **bulleted lists** for unordered information
- Keep list items parallel in structure

### Headings
- **H2 for major sections** - API endpoints, major features
- **H3 for subsections** - Parameters, return values, examples
- **H4 for details** - Edge cases, notes, warnings

---

## Rhetorical Devices

Technical writing uses minimal rhetoric, but these can help:

- **Logos** (logic and evidence) - Always primary
- **Ethos** (authority through accuracy) - Build trust with correctness
- **Tricolon** (groups of three) - "Fast, reliable, and scalable"
- **Anaphora** (repetition) - In parallel structures: "Install X. Install Y. Install Z."

---

## Structure Templates

### API Documentation Structure
```markdown
# Function/Method Name

Brief one-line description.

## Syntax
function signature(params): returnType

## Parameters
- param1 (type): Description
- param2 (type): Description

## Return Value
Description of what's returned

## Examples
[code block with usage]

## Notes
Edge cases, warnings, best practices

## See Also
Related functions/methods
```

### Tutorial Structure
1. **Introduction**
   - What you'll learn
   - Prerequisites
   - Time estimate
   
2. **Steps**
   - Numbered, sequential instructions
   - Each step has explanation + code/command
   
3. **Verification**
   - How to confirm it worked
   - Expected output
   
4. **Next Steps**
   - What to explore next
   - Related tutorials

---

## Examples

### Instruction (Bad → Good)
❌ "You might want to consider installing the package."
✅ "Install the package with `npm install package-name`."

### Explanation (Bad → Good)
❌ "The API is really powerful and can do lots of things."
✅ "The API provides three endpoints: `/users` for user management, `/posts` for content, and `/auth` for authentication."

### Error Documentation (Bad → Good)
❌ "Something went wrong."
✅ "Error: `ECONNREFUSED` - The database connection failed. Verify that PostgreSQL is running on port 5432."

---

## Checklist for Technical Writing

- [ ] All code examples are syntactically correct
- [ ] All commands have been tested
- [ ] Prerequisites are clearly stated
- [ ] Expected output is shown
- [ ] Error cases are documented
- [ ] Terminology is consistent throughout
- [ ] Steps are in logical order
- [ ] Examples are complete and runnable
- [ ] Version numbers are specified where relevant

---

## Special Elements

### Warnings
```markdown
⚠️ **Warning**: This operation is destructive and cannot be undone.
```

### Tips
```markdown
💡 **Tip**: Use the `--dry-run` flag to preview changes before applying them.
```

### Notes
```markdown
📝 **Note**: This feature is experimental in version 2.x.
```

---

## When to Use This Style

- API documentation
- Technical tutorials and guides
- README files
- Installation instructions
- Architecture documentation
- Configuration guides
- Troubleshooting docs
- Release notes

---

## Code Comment Standards

```typescript
// Good: Explain WHY, not WHAT
// Cache results to avoid redundant API calls
const cache = new Map();

// Bad: Restates the obvious
// Create a new Map
const cache = new Map();
```

---

**Application Note**: When writing in Technical Laura style, test all code examples and commands before including them. Accuracy is non-negotiable.