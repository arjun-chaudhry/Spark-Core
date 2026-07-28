# Get Started with Spark Core Durable Functions

[![PyPI](https://img.shields.io/pypi/v/spark-core-azurefunctions)](https://pypi.org/project/spark-core-azurefunctions/)

Please install this package via pip:

```bash
pip install spark-core-azurefunctions --pre
```

## Durable Agent Extension

The durable agent extension lets you host Spark Core agents on Azure Durable Functions so they can persist state, replay conversation history, and recover from failures automatically.

### Basic Usage Example

See the durable functions integration sample in the repository to learn how to:

```python
from spark_core.azure import AgentFunctionApp

_app = AgentFunctionApp()
```

- Register agents with `AgentFunctionApp`
- Post messages using the generated `/api/agents/{agent_name}/run` endpoint

For more details, review the Python [README](https://github.com/microsoft/spark-core/tree/main/python/README.md) and the samples directory.
