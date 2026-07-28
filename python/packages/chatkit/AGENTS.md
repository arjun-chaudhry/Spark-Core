# ChatKit Package (spark-core-chatkit)

Integration with OpenAI ChatKit (Python) for building chat UIs.

## Main Classes

- **`ThreadItemConverter`** - Converts between Spark Core and ChatKit types
- **`stream_agent_response()`** - Stream agent responses to ChatKit
- **`simple_to_agent_input()`** - Convert simple input to agent input format

## Usage

```python
from spark_core.chatkit import stream_agent_response, ThreadItemConverter

async for event in stream_agent_response(agent, messages):
    # Handle ChatKit events
    pass
```

## Import Path

```python
from spark_core.chatkit import stream_agent_response
# or directly:
from spark_core_chatkit import stream_agent_response
```
