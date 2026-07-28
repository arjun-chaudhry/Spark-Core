# Azure Cosmos DB Package (spark-core-azure-cosmos)

Azure Cosmos DB history provider integration for Spark Core.

## Main Classes

- **`CosmosHistoryProvider`** - Persistent conversation history storage backed by Azure Cosmos DB

## Usage

```python
from spark_core.azure import CosmosHistoryProvider

provider = CosmosHistoryProvider(
    endpoint="https://<account>.documents.azure.com:443/",
    credential="<key-or-token-credential>",
    database_name="spark-core",
    container_name="chat-history",
)
```

Container name is configured on the provider. `session_id` is used as the partition key.

## Import Path

```python
from spark_core.azure import CosmosHistoryProvider
# or directly:
from spark_core_azure_cosmos import CosmosHistoryProvider
```
