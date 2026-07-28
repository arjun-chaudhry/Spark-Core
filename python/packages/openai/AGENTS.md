# AGENTS.md — spark-core-openai

OpenAI integration package for Spark Core. Contains OpenAI Responses API and Chat Completions API clients.

## Package Structure

```
spark_core_openai/
├── __init__.py                 # Public API exports
├── _chat_client.py             # OpenAIChatClient (Responses API) + RawOpenAIChatClient
├── _chat_completion_client.py  # OpenAIChatCompletionClient (Chat Completions API) + RawOpenAIChatCompletionClient
├── _embedding_client.py        # OpenAIEmbeddingClient
├── _exceptions.py              # OpenAI-specific exceptions
└── _shared.py                  # OpenAISettings and shared config helpers
```

## Key Classes

| Class | API | Status |
|---|---|---|
| `OpenAIChatClient` | Responses API | Primary |
| `OpenAIChatCompletionClient` | Chat Completions API | Primary |
| `OpenAIEmbeddingClient` | Embeddings API | Primary |

All clients follow the Raw + Full-Featured pattern (e.g., `RawOpenAIChatClient` + `OpenAIChatClient`).

The generic OpenAI clients support both OpenAI and Azure OpenAI routing. Precedence is:
explicit Azure inputs (`credential`, `azure_endpoint`, `api_version`) → OpenAI API key
(`OPENAI_API_KEY`) → Azure environment fallback (`AZURE_OPENAI_*`).

## Dependencies

- `spark-core-core` — core abstractions
- `openai` — OpenAI Python SDK
