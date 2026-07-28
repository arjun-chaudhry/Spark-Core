# Purview Package (spark-core-purview)

Integration with Microsoft Purview for data governance and policy enforcement.

## Main Classes

### Middleware

- **`PurviewPolicyMiddleware`** - Agent middleware for Purview policy enforcement
- **`PurviewChatPolicyMiddleware`** - Chat-level middleware for policy enforcement

### Configuration

- **`PurviewSettings`** - Pydantic settings for Purview configuration
- **`PurviewAppLocation`** / **`PurviewLocationType`** - Location configuration

### Caching

- **`CacheProvider`** - Cache provider for Purview policy caching

### Exceptions

- **`PurviewAuthenticationError`** - Authentication failures (inherits from `IntegrationInvalidAuthException`)
- **`PurviewRateLimitError`** - Rate limit exceeded (inherits from `IntegrationException` via `PurviewServiceError`)
- **`PurviewRequestError`** / **`PurviewServiceError`** - Request/service errors (inherit from `IntegrationException`)
- **`PurviewPaymentRequiredError`** - Payment required (inherits from `IntegrationException` via `PurviewServiceError`)

## Usage

```python
from spark_core.microsoft import PurviewPolicyMiddleware, PurviewSettings

settings = PurviewSettings(...)
middleware = PurviewPolicyMiddleware(settings=settings)
agent = Agent(..., middleware=[middleware])
```

## Import Path

```python
from spark_core.microsoft import PurviewPolicyMiddleware
# or directly:
from spark_core_purview import PurviewPolicyMiddleware
```
