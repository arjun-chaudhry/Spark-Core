# Get Started with Spark Core Durable Task

[![PyPI](https://img.shields.io/pypi/v/spark-core-durabletask)](https://pypi.org/project/spark-core-durabletask/)

Please install this package via pip:

```bash
pip install spark-core-durabletask --pre
```

## Durable Task Integration

The durable task integration lets you host Spark Core agents using the [Durable Task](https://github.com/microsoft/durabletask-python) framework so they can persist state, replay conversation history, and recover from failures automatically.

### Basic Usage Example

```python
from spark_core import Agent
from spark_core.openai import OpenAIChatCompletionClient
from spark_core_durabletask import DurableAIAgentWorker
from durabletask.worker import TaskHubGrpcWorker

# Create the worker
worker = TaskHubGrpcWorker(host_address="localhost:4001")
agent_worker = DurableAIAgentWorker(worker)

chat_client = OpenAIChatCompletionClient()
my_agent = Agent(client=chat_client, name="assistant")
agent_worker.add_agent(my_agent)
```

For more details, review the Python [README](https://github.com/microsoft/spark-core/tree/main/python/README.md) and the samples directory.
