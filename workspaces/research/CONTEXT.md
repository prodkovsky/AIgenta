---
title: Research Workspace Context
type: context
created: 2026-06-08
updated: 2026-06-11
lines: 118
status: active
---
# Research Workspace Context
## Guidelines for Research Tasks

---

## Purpose

This workspace handles all research tasks: information gathering, source evaluation, synthesis, fact-checking, and analytical reporting.

Unlike the Writing workspace (which produces original content), the Research workspace prioritizes **accuracy, attribution, and intellectual honesty**.

---

## Core Principles

1. **Source quality over quantity** — One peer-reviewed source beats ten blog posts
2. **Transparency** — Always show your work: cite sources, distinguish fact from inference
3. **Synthesis over summarization** — Connect ideas across sources; don't just list them
4. **Uncertainty mapping** — Explicitly flag what is known, unknown, and contested
5. **No fabrication** — If you cannot verify a claim, say so

---

## Research Workflow

### Phase 1: Define the Question
- Clarify the exact research question
- Identify the scope (time period, geography, domain)
- Determine the output format (brief, report, annotated bibliography)

### Phase 2: Source Gathering
- Prioritize primary sources when available
- Use academic databases, official reports, and authoritative publications
- Distinguish source types:
  - **Primary**: Original data, eyewitness accounts, raw documents
  - **Secondary**: Analysis, reviews, syntheses by others
  - **Tertiary**: Encyclopedias, summaries, textbooks

### Phase 3: Source Evaluation
Apply the **CRAAP test**:
- **Currency**: When was it published? Is it still relevant?
- **Relevance**: Does it directly address the research question?
- **Authority**: Who wrote it? What are their credentials?
- **Accuracy**: Is it supported by evidence? Has it been peer-reviewed?
- **Purpose**: Why was it written? Is there bias?

### Phase 4: Synthesis
- Group findings by theme, not by source
- Identify agreements, contradictions, and gaps
- Build an argument or narrative from the evidence
- Flag limitations and areas needing further research

### Phase 5: Documentation
- Save research output to `workspaces/research/projects/YYYY-MM-DD_topic-name.md`
- Include a source list with full citations
- Distinguish direct quotes, paraphrases, and your own analysis

---

## Source Citation Format

Use a consistent citation style. Default to **APA** for social sciences, **MLA** for humanities, **IEEE** for technical fields.

### Inline Citation
> "Neural scaling laws suggest that model performance predictably improves with compute, data, and parameters (Kaplan et al., 2020)."

### Source List Entry
```
Kaplan, J., McCandlish, S., Henighan, T., Brown, T. B., Chess, B., Child, R., ... & Amodei, D. (2020). 
Scaling laws for neural language models. arXiv preprint arXiv:2001.08361.
```

### For Web Sources
Include URL and access date:
```
OpenAI. (2023). GPT-4 technical report. https://arxiv.org/abs/2303.08774 (Accessed: 2026-06-08).
```

---

## Output Formats

### Research Brief (1-2 pages)
- Executive summary
- Key findings (3-5 bullet points)
- Source list

### Research Report (3-10 pages)
- Abstract
- Research question
- Methodology
- Findings by theme
- Analysis and implications
- Limitations
- Source list

### Annotated Bibliography
- Full citation for each source
- 2-3 sentence summary
- 1-2 sentence evaluation of relevance and quality

---

## Fact-Checking Protocol

Before presenting a claim as fact:

1. **Can you trace it to a primary source?**
2. **Does the source actually say what you think it says?** (read the original, not the summary)
3. **Is there contradictory evidence?**
4. **Is the claim current?** (Has it been superseded?)
5. **Would an expert in this field accept this claim?**

If any answer is uncertain, flag the claim:
- "According to X (2023), though this finding has been contested by Y (2024)..."
- "This claim appears in popular coverage but could not be verified in the original study."

---

## Research Ethics

- **No plagiarism** — Always attribute ideas, even when paraphrased
- **No cherry-picking** — Present counterevidence, not just confirming evidence
- **No source misrepresentation** — Don't claim a source says something it doesn't
- **Respect embargoed or private data** — Don't cite sources you shouldn't have access to

---

## Integration with Writing Workspace

Research outputs often feed into writing projects:

1. Complete research in this workspace first
2. Export key findings and citations to the writing project
3. Use Laura styles to shape the presentation
4. Maintain the research file as the "source of truth" for citations

---

## File Organization

### Projects
`workspaces/research/projects/YYYY-MM-DD_research-topic.md`

Examples:
- `2026-06-08_neural-scaling-laws.md`
- `2026-06-08_remote-work-meta-analysis.md`

### Source Archives
`workspaces/research/sources/` — Raw notes, excerpts, and saved references

### Methods
`workspaces/research/methods/` — Reusable research frameworks and evaluation criteria

---

## Memory & Learning

After completing research tasks:
- Update `memory/learnings.md` with reusable insights
- Note reliable sources and databases for future reference
- Record methodological improvements

---

**Next Action**: Based on the user's research request, define the question, gather sources, evaluate them, synthesize findings, and document the output.
