# Foundry Local Package (spark-core-foundry-local)

Integration with Microsoft Foundry Local for local model inference.

## Main Classes

- **`FoundryLocalClient`** - Chat client for Foundry Local models
- **`FoundryLocalChatOptions`** - Options TypedDict for Foundry Local parameters
- **`FoundryLocalSettings`** - Pydantic settings for configuration

## Usage

```python
from spark_core.foundry import FoundryLocalClient

client = FoundryLocalClient(model="your-local-model")
response = await client.get_response("Hello")
```

## Import Path

```python
from spark_core.foundry import FoundryLocalClient
```
