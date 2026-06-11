---
title: OpenRouter API
type: api
created: 2026-06-08
updated: 2026-06-11
lines: 161
status: active
---
# OpenRouter API
## Universal LLM API Gateway

---

## Overview

[OpenRouter](https://openrouter.ai/) provides a unified API for accessing hundreds of LLMs (Claude, GPT-4, Llama, Mistral, Qwen, etc.) through a single endpoint. It handles model routing, fallback, and pricing normalization.

**Use case for AIgenta**: Route writing tasks to different models based on style requirements, cost constraints, or availability.

---

## Authentication

### API Key
Get your key at [openrouter.ai/keys](https://openrouter.ai/keys)

```bash
export OPENROUTER_API_KEY="sk-or-v1-xxxxxxxxxxxxxxxx"
```

### Required Headers
```
Authorization: Bearer sk-or-v1-xxxxxxxxxxxxxxxx
HTTP-Referer: https://your-site.com
X-Title: AIgenta Writer
```

---

## Base URL

```
https://openrouter.ai/api/v1
```

---

## Endpoints

### Chat Completions
```
POST /chat/completions
```

**Request:**
```json
{
  "model": "anthropic/claude-3.5-sonnet",
  "messages": [
    {
      "role": "system",
      "content": "You are a writing assistant. Read the attached context files and write in the specified style."
    },
    {
      "role": "user",
      "content": "Write a technical blog post about database indexing using the attached style guide."
    }
  ],
  "temperature": 0.7,
  "max_tokens": 4000
}
```

**Response:**
```json
{
  "id": "gen-xxxxxxxx",
  "model": "anthropic/claude-3.5-sonnet",
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "# Understanding Database Indexing..."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 1250,
    "completion_tokens": 1800,
    "total_tokens": 3050
  }
}
```

### Available Models
```
GET /models
```

Returns a list of available models with pricing and context window sizes.

### Model Routing (Automatic)
```json
{
  "model": "openrouter/auto",
  "messages": [...]
}
```
OpenRouter automatically selects the best available model based on your criteria.

---

## AIgenta Integration Pattern

### Workflow
1. Read the relevant Laura style file (e.g., `styles/technical.md`)
2. Read requested rhetoric devices (e.g., `rhetoric/logos.md`)
3. Construct a system prompt incorporating the style guidelines
4. Send user request + system prompt to OpenRouter
5. Save the response to `workspaces/writing/projects/YYYY-MM-DD_topic.md`

### Example System Prompt Construction
```
You are Laura, a technical writing specialist.

STYLE GUIDELINES:
- Clear and direct tone. No ambiguity.
- Use imperative for instructions.
- Active voice preferred.
- Short, focused sentences.
- Include code blocks with language identifiers.

RHETORICAL APPROACH:
- Primary: Logos (logic and evidence)
- Secondary: Ethos (authority through accuracy)

TASK:
Write the content requested by the user, following the above guidelines exactly.
```

---

## Pricing

OpenRouter normalizes pricing to per-million-tokens:

| Model | Input ($/M) | Output ($/M) |
|-------|-------------|--------------|
| claude-3.5-sonnet | $3.00 | $15.00 |
| gpt-4o | $2.50 | $10.00 |
| llama-3.1-70b | $0.30 | $0.60 |
| qwen-2.5-72b | $0.35 | $0.40 |

**Tip**: Use cheaper models for drafting, expensive models for final polish.

---

## Error Handling

| Code | Meaning | Action |
|------|---------|--------|
| 401 | Invalid API key | Verify key in environment |
| 429 | Rate limited | Implement exponential backoff |
| 502 | Model unavailable | Fallback to `openrouter/auto` |
| 529 | Overloaded | Retry with different model |

---

## Usage Example (Python)

```python
import os
import requests

API_KEY = os.environ["OPENROUTER_API_KEY"]

def generate_with_style(style_content, user_prompt, model="anthropic/claude-3.5-sonnet"):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "https://aigenta.local",
        "X-Title": "AIgenta Writer",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": style_content},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 4000
    }
    
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=payload
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
```

---

## See Also

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [Model Comparison](https://openrouter.ai/models)
- [Pricing Calculator](https://openrouter.ai/models)

---

**Integration Version**: 1.0  
**Last Updated**: 2026-06-08
