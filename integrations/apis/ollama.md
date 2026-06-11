---
title: Ollama API
type: api
created: 2026-06-08
updated: 2026-06-11
lines: 209
status: active
---
# Ollama API
## Local LLM Runner

---

## Overview

[Ollama](https://ollama.com/) runs large language models locally on your machine. It provides a simple API for interacting with open-source models (Llama, Mistral, Qwen, Gemma, etc.) without sending data to external servers.

**Use case for AIgenta**: Private, offline writing assistance. No API costs. No data leaves your machine.

---

## Installation

### macOS
```bash
brew install ollama
```

### Linux
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Verify Installation
```bash
ollama --version
```

---

## Authentication

Ollama runs locally and does not require API keys by default. If you configure authentication:

```bash
export OLLAMA_API_KEY="optional-key"
```

---

## Base URL

```
http://localhost:11434
```

---

## Endpoints

### Generate Completion
```
POST /api/generate
```

**Request:**
```json
{
  "model": "llama3.1:8b",
  "prompt": "Write a haiku about debugging code.",
  "system": "You are a poetic technical writer.",
  "stream": false,
  "options": {
    "temperature": 0.7,
    "num_predict": 500
  }
}
```

**Response:**
```json
{
  "model": "llama3.1:8b",
  "created_at": "2026-06-08T10:00:00Z",
  "response": "Silent console waits,\nOne semicolon misplaced,\nJoy in the fix found.",
  "done": true,
  "total_duration": 2450000000,
  "load_duration": 1230000000,
  "prompt_eval_count": 25,
  "eval_count": 45
}
```

### Chat Completions (OpenAI-Compatible)
```
POST /api/chat
```

**Request:**
```json
{
  "model": "mistral:7b",
  "messages": [
    {
      "role": "system",
      "content": "You are Laura, a neutral-style writing assistant. Be clear and approachable."
    },
    {
      "role": "user",
      "content": "Write a paragraph explaining API rate limiting."
    }
  ],
  "stream": false,
  "options": {
    "temperature": 0.7
  }
}
```

### List Local Models
```
GET /api/tags
```

**Response:**
```json
{
  "models": [
    {
      "name": "llama3.1:8b",
      "model": "llama3.1:8b",
      "modified_at": "2026-06-01T12:00:00Z",
      "size": 4920000000,
      "digest": "sha256-...",
      "details": {
        "format": "gguf",
        "family": "llama",
        "parameter_size": "8B"
      }
    }
  ]
}
```

### Pull a Model
```
POST /api/pull
```

```bash
curl http://localhost:11434/api/pull -d '{
  "name": "llama3.1:8b"
}'
```

---

## AIgenta Integration Pattern

### Workflow
1. Start Ollama locally: `ollama serve`
2. Ensure the desired model is pulled: `ollama pull llama3.1:8b`
3. Read AIgenta style/rhetoric files
4. Construct prompt with style context
5. Send to local Ollama endpoint
6. Save response to `workspaces/writing/projects/`

### Example System Prompt
```
You are Laura, a writing assistant using the Poetic style.

GUIDELINES:
- Use metaphor and sensory detail
- Vary sentence rhythm
- Engage emotion through imagery
- Avoid clichés

RHETORIC:
- Primary: Pathos (emotional appeal)
- Support: Anaphora (repetition for rhythm)

Write the user's requested content following these guidelines.
```

---

## Recommended Models for Writing

| Model | Size | Speed | Quality | Best For |
|-------|------|-------|---------|----------|
| llama3.1:8b | 8B | Fast | Good | Drafting, brainstorming |
| mistral:7b | 7B | Fast | Good | General writing tasks |
| qwen2.5:14b | 14B | Medium | Very Good | Technical content |
| llama3.1:70b | 70B | Slow | Excellent | Final polish, complex tasks |
| gemma2:9b | 9B | Fast | Good | Short-form content |

---

## Performance Tips

- **Use smaller models for drafting** (8B-14B) — faster, good enough
- **Use larger models for revision** (70B+) — better quality, worth the wait
- **Enable GPU acceleration** if available:
  ```bash
  export OLLAMA_GPU_OVERHEAD=1
  ```
- **Quantization**: Use `q4_0` or `q5_0` for faster inference with minimal quality loss

---

## Error Handling

| Issue | Cause | Solution |
|-------|-------|----------|
| Connection refused | Ollama not running | Start with `ollama serve` |
| Model not found | Not pulled locally | Run `ollama pull <model>` |
| Out of memory | Model too large for RAM | Use smaller model or enable swap |
| Slow generation | CPU-only inference | Check GPU support, reduce model size |

---

## Usage Example (Python)

```python
import requests
import json

def generate_local(style_content, user_prompt, model="llama3.1:8b"):
    url = "http://localhost:11434/api/chat"
    
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": style_content},
            {"role": "user", "content": user_prompt}
        ],
        "stream": False,
        "options": {
            "temperature": 0.7,
            "num_predict": 4000
        }
    }
    
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()["message"]["content"]

# Example usage
style = open("workspaces/writing/styles/neutral.md").read()
content = generate_local(style, "Write a blog post about remote work.")
print(content)
```

---

## Privacy Note

All inference happens locally. No data is sent to external servers. This makes Ollama ideal for:
- Sensitive or confidential writing
- Drafting before using cloud APIs
- Offline work environments
- Cost-conscious workflows

---

## See Also

- [Ollama Documentation](https://github.com/ollama/ollama/blob/main/docs/README.md)
- [Model Library](https://ollama.com/library)
- [OpenRouter Integration](openrouter.md) — for cloud model access

---

**Integration Version**: 1.0  
**Last Updated**: 2026-06-08
