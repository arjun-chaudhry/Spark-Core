# Redis Package (spark-core-redis)

Redis-based storage for agent threads and context.

## Main Classes

- **`RedisHistoryProvider`** - Persistent chat history provider using Redis
- **`RedisContextProvider`** - Context provider with Redis-backed retrieval

## Usage

```python
from spark_core.redis import RedisContextProvider, RedisHistoryProvider

context_provider = RedisContextProvider(redis_url="redis://localhost:6379")
history_provider = RedisHistoryProvider(redis_url="redis://localhost:6379")
```

## Import Path

```python
from spark_core.redis import RedisContextProvider, RedisHistoryProvider
# or directly:
from spark_core_redis import RedisContextProvider, RedisHistoryProvider
```
