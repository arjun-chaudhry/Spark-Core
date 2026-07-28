# Python Samples

This directory contains samples demonstrating the capabilities of Spark Core for Python.

## Structure

| Folder | Description |
|--------|-------------|
| [`01-get-started/`](./01-get-started/) | Progressive tutorial: hello agent → hosting |
| [`02-agents/`](./02-agents/) | Deep-dive by concept: tools, middleware, providers, orchestrations |
| [`03-workflows/`](./03-workflows/) | Workflow patterns: sequential, concurrent, state, declarative, explicit output designation |
| [`04-hosting/`](./04-hosting/) | Deployment: Azure Functions, Durable Tasks, A2A |
| [`05-end-to-end/`](./05-end-to-end/) | Full applications, evaluation, demos |

## Getting Started

Start with `01-get-started/` and work through the numbered files:

1. **[01_hello_agent.py](./01-get-started/01_hello_agent.py)** — Create and run your first agent
2. **[02_add_tools.py](./01-get-started/02_add_tools.py)** — Add function tools with `@tool`
3. **[03_multi_turn.py](./01-get-started/03_multi_turn.py)** — Multi-turn conversations with `AgentSession`
4. **[04_memory.py](./01-get-started/04_memory.py)** — Agent memory with `ContextProvider`
5. **[05_functional_workflow_with_agents.py](./01-get-started/05_functional_workflow_with_agents.py)** — Call agents inside a functional workflow
6. **[06_functional_workflow_basics.py](./01-get-started/06_functional_workflow_basics.py)** — Write a workflow as a plain async function
7. **[07_first_graph_workflow.py](./01-get-started/07_first_graph_workflow.py)** — Build a workflow with executors and edges
8. **[08_host_your_agent.py](./01-get-started/08_host_your_agent.py)** — Host your agent via Azure Functions

## Prerequisites

```bash
pip install spark-core-foundry
```

Install only the specific Spark Core distributions required by the sample you want to run.
Individual sample READMEs and PEP 723 metadata list any additional packages.

### Environment Variables

Samples call `load_dotenv()` to automatically load environment variables from a `.env` file in the `python/` directory. This is a convenience for local development and testing.

**For local development**, set up your environment using any of these methods:

**Option 1: Using a `.env` file** (recommended for local development):
1. Copy `.env.example` to `.env` in the `python/` directory:
   ```bash
   cp .env.example .env
   ```
2. Edit `.env` and set your values (API keys, endpoints, etc.)

**Option 2: Export environment variables directly**:
```bash
export FOUNDRY_PROJECT_ENDPOINT="your-foundry-project-endpoint"
export FOUNDRY_MODEL="gpt-4o"
```

**Option 3: Using `env_file_path` parameter** (for per-client configuration):

All client classes (e.g., `OpenAIChatClient`, `OpenAIChatCompletionClient`) support an `env_file_path` parameter to load environment variables from a specific file:

```python
from spark_core.openai import OpenAIChatClient

# Load from a custom .env file
client = OpenAIChatClient(env_file_path="path/to/custom.env")
```

This allows different clients to use different configuration files if needed.

For the generic OpenAI clients (`OpenAIChatClient` and `OpenAIChatCompletionClient`), routing
precedence is:

1. Explicit Azure inputs such as `credential`, `azure_endpoint`, or `api_version`
2. `OPENAI_API_KEY` / explicit OpenAI API-key parameters
3. Azure environment fallback such as `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_API_KEY`

If you keep both OpenAI and Azure variables in your shell, the generic clients stay on OpenAI until
you pass an explicit Azure input.

For the getting-started samples, you'll need at minimum:
```bash
FOUNDRY_PROJECT_ENDPOINT="your-foundry-project-endpoint"
FOUNDRY_MODEL="gpt-4o"
```

#### Consolidated sample env inventory

This is the single source of truth for package-level environment variables read by packages included by
`spark-core-core[all]`. It intentionally excludes variables that are only read by standalone samples,
package sample folders, or tests. When package code adds, removes, or renames an environment variable,
update this table in the same change.

Example values below are illustrative. For entries not backed by a single public class, the `class`
column names the closest public surface, helper, or package-level initialization point that reads the
variable.

| package | class/module | env var | example value |
| --- | --- | --- | --- |
| `spark-core-anthropic` | `AnthropicClient` | `ANTHROPIC_API_KEY` | `sk-ant-api03-...` |
| `spark-core-anthropic` | `AnthropicClient` | `ANTHROPIC_CHAT_MODEL` | `claude-sonnet-4-5-20250929` |
| `spark-core-foundry` | `FoundryEmbeddingClient` | `FOUNDRY_MODELS_ENDPOINT` | `https://my-endpoint.inference.ai.azure.com` |
| `spark-core-foundry` | `FoundryEmbeddingClient` | `FOUNDRY_MODELS_API_KEY` | `env-key` |
| `spark-core-foundry` | `FoundryEmbeddingClient` | `FOUNDRY_EMBEDDING_MODEL` | `text-embedding-3-small` |
| `spark-core-foundry` | `FoundryEmbeddingClient` | `FOUNDRY_IMAGE_EMBEDDING_MODEL` | `Cohere-embed-v3-english` |
| `spark-core-azure-ai-search` | `AzureAISearchContextProvider` | `AZURE_SEARCH_ENDPOINT` | `https://my-search.search.windows.net` |
| `spark-core-azure-ai-search` | `AzureAISearchContextProvider` | `AZURE_SEARCH_API_KEY` | `search-key` |
| `spark-core-azure-ai-search` | `AzureAISearchContextProvider` | `AZURE_SEARCH_INDEX_NAME` | `hotels-index` |
| `spark-core-azure-ai-search` | `AzureAISearchContextProvider` | `AZURE_SEARCH_KNOWLEDGE_BASE_NAME` | `hotels-kb` |
| `spark-core-azure-cosmos` | `CosmosHistoryProvider` | `AZURE_COSMOS_ENDPOINT` | `https://my-cosmos.documents.azure.com:443/` |
| `spark-core-azure-cosmos` | `CosmosHistoryProvider` | `AZURE_COSMOS_DATABASE_NAME` | `agent-history` |
| `spark-core-azure-cosmos` | `CosmosHistoryProvider` | `AZURE_COSMOS_CONTAINER_NAME` | `messages` |
| `spark-core-azure-cosmos` | `CosmosHistoryProvider` | `AZURE_COSMOS_KEY` | `C2F...==` |
| `spark-core-bedrock` | `BedrockChatClient` | `BEDROCK_REGION` | `us-east-1` |
| `spark-core-bedrock` | `BedrockChatClient` | `BEDROCK_CHAT_MODEL` | `anthropic.claude-3-5-sonnet-20241022-v2:0` |
| `spark-core-bedrock` | `BedrockEmbeddingClient` | `BEDROCK_REGION` | `us-east-1` |
| `spark-core-bedrock` | `BedrockEmbeddingClient` | `BEDROCK_EMBEDDING_MODEL` | `amazon.titan-embed-text-v2:0` |
| `spark-core-bedrock` | `BedrockChatClient / BedrockEmbeddingClient` | `AWS_ACCESS_KEY_ID` | `AKIAIOSFODNN7EXAMPLE` |
| `spark-core-bedrock` | `BedrockChatClient / BedrockEmbeddingClient` | `AWS_SECRET_ACCESS_KEY` | `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY` |
| `spark-core-bedrock` | `BedrockChatClient / BedrockEmbeddingClient` | `AWS_SESSION_TOKEN` | `IQoJb3JpZ2luX2VjEO7//////////wEaCXVzLXdlc3QtMiJHMEUCIQD...` |
| `spark-core-copilotstudio` | `CopilotStudioAgent` | `COPILOTSTUDIOAGENT__ENVIRONMENTID` | `00000000-0000-0000-0000-000000000000` |
| `spark-core-copilotstudio` | `CopilotStudioAgent` | `COPILOTSTUDIOAGENT__SCHEMANAME` | `cr123_agentname` |
| `spark-core-copilotstudio` | `CopilotStudioAgent` | `COPILOTSTUDIOAGENT__TENANTID` | `11111111-1111-1111-1111-111111111111` |
| `spark-core-copilotstudio` | `CopilotStudioAgent` | `COPILOTSTUDIOAGENT__AGENTAPPID` | `22222222-2222-2222-2222-222222222222` |
| `spark-core-core` | `observability` | `ENABLE_INSTRUMENTATION` | `true` |
| `spark-core-core` | `observability` | `ENABLE_SENSITIVE_DATA` | `false` |
| `spark-core-core` | `observability` | `ENABLE_CONSOLE_EXPORTERS` | `true` |
| `spark-core-core` | `observability` | `OTEL_EXPORTER_OTLP_ENDPOINT` | `http://localhost:4317` |
| `spark-core-core` | `observability` | `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` | `http://localhost:4318/v1/traces` |
| `spark-core-core` | `observability` | `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT` | `http://localhost:4318/v1/metrics` |
| `spark-core-core` | `observability` | `OTEL_EXPORTER_OTLP_LOGS_ENDPOINT` | `http://localhost:4318/v1/logs` |
| `spark-core-core` | `observability` | `OTEL_EXPORTER_OTLP_PROTOCOL` | `grpc` |
| `spark-core-core` | `observability` | `OTEL_EXPORTER_OTLP_HEADERS` | `api-key=demo` |
| `spark-core-core` | `observability` | `OTEL_EXPORTER_OTLP_TRACES_HEADERS` | `api-key=trace-demo` |
| `spark-core-core` | `observability` | `OTEL_EXPORTER_OTLP_METRICS_HEADERS` | `api-key=metric-demo` |
| `spark-core-core` | `observability` | `OTEL_EXPORTER_OTLP_LOGS_HEADERS` | `api-key=log-demo` |
| `spark-core-core` | `observability` | `OTEL_SERVICE_NAME` | `sample-agent` |
| `spark-core-core` | `observability` | `OTEL_SERVICE_VERSION` | `1.0.0` |
| `spark-core-core` | `observability` | `OTEL_RESOURCE_ATTRIBUTES` | `deployment.environment=dev,service.namespace=spark-core` |
| `spark-core-devui` | `DevUI server` | `DEVUI_AUTH_TOKEN` | `my-devui-token` |
| `spark-core-foundry` | `FoundryChatClient` | `FOUNDRY_PROJECT_ENDPOINT` | `https://my-project.services.ai.azure.com/api/projects/my-project` |
| `spark-core-foundry` | `FoundryChatClient` | `FOUNDRY_MODEL` | `gpt-4o` |
| `spark-core-foundry` | `FoundryAgent` | `FOUNDRY_AGENT_NAME` | `travel-planner` |
| `spark-core-foundry` | `FoundryAgent` | `FOUNDRY_AGENT_VERSION` | `v1` |
| `spark-core-github-copilot` | `GitHubCopilotAgent` | `GITHUB_COPILOT_CLI_PATH` | `copilot` |
| `spark-core-github-copilot` | `GitHubCopilotAgent` | `GITHUB_COPILOT_MODEL` | `gpt-5` |
| `spark-core-github-copilot` | `GitHubCopilotAgent` | `GITHUB_COPILOT_TIMEOUT` | `60` |
| `spark-core-github-copilot` | `GitHubCopilotAgent` | `GITHUB_COPILOT_LOG_LEVEL` | `info` |
| `spark-core-mem0` | `spark_core_mem0 package import` | `MEM0_TELEMETRY` | `false` |
| `spark-core-ollama` | `OllamaChatClient` | `OLLAMA_HOST` | `http://localhost:11434` |
| `spark-core-ollama` | `OllamaChatClient` | `OLLAMA_MODEL` | `llama3.1:8b` |
| `spark-core-openai` | `OpenAIChatClient / OpenAIChatCompletionClient / OpenAIEmbeddingClient` | `OPENAI_API_KEY` | `sk-proj-...` |
| `spark-core-openai` | `OpenAIChatClient / OpenAIChatCompletionClient / OpenAIEmbeddingClient` | `OPENAI_MODEL` | `gpt-4o-mini` |
| `spark-core-openai` | `OpenAIChatClient` | `OPENAI_CHAT_MODEL` | `gpt-4.1-mini` |
| `spark-core-openai` | `OpenAIChatCompletionClient` | `OPENAI_CHAT_COMPLETION_MODEL` | `gpt-4o` |
| `spark-core-openai` | `OpenAIEmbeddingClient` | `OPENAI_EMBEDDING_MODEL` | `text-embedding-3-small` |
| `spark-core-openai` | `OpenAIChatClient / OpenAIChatCompletionClient / OpenAIEmbeddingClient` | `OPENAI_BASE_URL` | `https://api.openai.com/v1/` |
| `spark-core-openai` | `OpenAIChatClient / OpenAIChatCompletionClient / OpenAIEmbeddingClient` | `OPENAI_ORG_ID` | `org_123456789` |
| `spark-core-openai` | `OpenAIChatClient / OpenAIChatCompletionClient / OpenAIEmbeddingClient` | `AZURE_OPENAI_ENDPOINT` | `https://my-resource.openai.azure.com/` |
| `spark-core-openai` | `OpenAIChatClient / OpenAIChatCompletionClient / OpenAIEmbeddingClient` | `AZURE_OPENAI_API_KEY` | `sk-azure-...` |
| `spark-core-openai` | `OpenAIChatClient / OpenAIChatCompletionClient / OpenAIEmbeddingClient` | `AZURE_OPENAI_API_VERSION` | `2024-10-21` |
| `spark-core-openai` | `OpenAIChatClient / OpenAIChatCompletionClient / OpenAIEmbeddingClient` | `AZURE_OPENAI_BASE_URL` | `https://my-resource.openai.azure.com/openai/v1/` |
| `spark-core-openai` | `OpenAIChatClient / OpenAIChatCompletionClient / OpenAIEmbeddingClient` | `AZURE_OPENAI_MODEL` | `gpt-4o` |
| `spark-core-openai` | `OpenAIChatClient` | `AZURE_OPENAI_CHAT_MODEL` | `gpt-4.1` |
| `spark-core-openai` | `OpenAIChatCompletionClient` | `AZURE_OPENAI_CHAT_COMPLETION_MODEL` | `gpt-4o-mini` |
| `spark-core-openai` | `OpenAIEmbeddingClient` | `AZURE_OPENAI_EMBEDDING_MODEL` | `text-embedding-3-large` |
| `spark-core-openai` | `OpenAIChatClient / OpenAIChatCompletionClient / OpenAIEmbeddingClient` | `AZURE_OPENAI_RESOURCE_URL` | `https://cognitiveservices.azure.com/` |

`spark-core-openai` supports the Azure OpenAI client-specific deployment aliases listed above; keep
`packages/openai/README.md` as the authoritative reference for the exact fallback order and package-specific
behavior.

**Note for production**: In production environments, set environment variables through your deployment platform (e.g., Azure App Settings, Kubernetes ConfigMaps/Secrets) rather than using `.env` files. The `load_dotenv()` call in samples will have no effect when a `.env` file is not present, allowing environment variables to be loaded from the system.

For Azure authentication, run `az login` before running samples.

## Note on XML tags

Some sample files include XML-style snippet tags (for example `<snippet_name>` and `</snippet_name>`). These are used by our documentation tooling and can be ignored or removed when you use the samples outside this repository.

## Additional Resources

- [Spark Core Documentation](https://learn.microsoft.com/spark-core/)
- [AGENTS.md](./AGENTS.md) — Structure documentation for maintainers
- [SAMPLE_GUIDELINES.md](./SAMPLE_GUIDELINES.md) — Coding conventions for samples
