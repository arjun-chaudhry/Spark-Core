# Mem0 Package (spark-core-mem0)

Integration with Mem0 for agent memory management.

## Main Classes

- **`Mem0ContextProvider`** - Context provider that integrates Mem0 memory into agents

## Usage

```python
from spark_core.mem0 import Mem0ContextProvider

provider = Mem0ContextProvider(
    api_key="your-key",
    user_id="user-id",
)
```

## Import Path

```python
from spark_core.mem0 import Mem0ContextProvider
# or directly:
from spark_core_mem0 import Mem0ContextProvider
```

## Notes

Mem0 telemetry is disabled by default. Set `MEM0_TELEMETRY=true` to enable.
