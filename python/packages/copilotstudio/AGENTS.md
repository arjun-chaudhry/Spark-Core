# Copilot Studio Package (spark-core-copilotstudio)

Integration with Microsoft Copilot Studio agents.

## Main Classes

- **`CopilotStudioAgent`** - Agent that connects to a Copilot Studio bot
- **`acquire_token`** - Helper function for authentication

## Usage

```python
from spark_core.microsoft import CopilotStudioAgent

agent = CopilotStudioAgent(
    bot_identifier="your-bot-id",
    environment_id="your-env-id",
)
response = await agent.run("Hello")
```

## Import Path

```python
from spark_core.microsoft import CopilotStudioAgent
# or directly:
from spark_core_copilotstudio import CopilotStudioAgent
```
