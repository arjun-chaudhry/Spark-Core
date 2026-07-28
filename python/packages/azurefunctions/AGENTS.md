# Azure Functions Package (spark-core-azurefunctions)

Hosting agents as Azure Functions.

## Main Classes

- **`AgentFunctionApp`** - Azure Functions app wrapper for agents

## Usage

```python
from spark_core.azure import AgentFunctionApp

app = AgentFunctionApp(agent=my_agent)
```

## Import Path

```python
from spark_core.azure import AgentFunctionApp
# or directly:
from spark_core_azurefunctions import AgentFunctionApp
```
