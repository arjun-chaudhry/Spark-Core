# Anthropic Package (spark-core-anthropic)

Integration with Anthropic's Claude API.

## Main Classes

- **`AnthropicClient`** - Chat client for Anthropic Claude models
- **`AnthropicFoundryClient`** - Anthropic chat client for Microsoft Foundry's Anthropic-compatible endpoint
- **`AnthropicBedrockClient`** - Anthropic chat client for Amazon Bedrock
- **`AnthropicVertexClient`** - Anthropic chat client for Google Vertex AI
- **`AnthropicChatOptions`** - Options TypedDict for Anthropic-specific parameters

## Usage

```python
from spark_core.anthropic import AnthropicClient

client = AnthropicClient(model="claude-sonnet-4-20250514")
response = await client.get_response("Hello")
```

## Import Path

```python
from spark_core.anthropic import AnthropicClient
# or directly:
from spark_core_anthropic import AnthropicClient
```
