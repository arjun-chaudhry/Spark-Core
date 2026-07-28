# Ollama Package (spark-core-ollama)

Integration with Ollama for local LLM inference.

## Main Classes

- **`OllamaChatClient`** - Chat client for Ollama models
- **`OllamaChatOptions`** - Options TypedDict for Ollama-specific parameters
- **`OllamaSettings`** - Pydantic settings for Ollama configuration

## Usage

```python
from spark_core.ollama import OllamaChatClient

client = OllamaChatClient(model="llama3.2")
response = await client.get_response("Hello")
```

## Import Path

```python
from spark_core.ollama import OllamaChatClient
# or directly:
from spark_core_ollama import OllamaChatClient
```
