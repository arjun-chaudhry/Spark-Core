# Copyright (c) Microsoft. All rights reserved.

# Type stubs for the spark_core.foundry lazy-loading namespace.
# Install the relevant packages for full type support.

from spark_core_anthropic import AnthropicFoundryClient, RawAnthropicFoundryClient
from spark_core_azure_contentunderstanding import (
    AnalysisSection,
    ContentUnderstandingContextProvider,
    DocumentStatus,
    FileSearchBackend,
    FileSearchConfig,
)
from spark_core_foundry import (
    FoundryAgent,
    FoundryChatClient,
    FoundryChatOptions,
    FoundryEmbeddingClient,
    FoundryEmbeddingOptions,
    FoundryEmbeddingSettings,
    FoundryEvals,
    FoundryMemoryProvider,
    GeneratedEvaluatorRef,
    RawFoundryAgent,
    RawFoundryAgentChatClient,
    RawFoundryChatClient,
    RawFoundryEmbeddingClient,
    evaluate_foundry_target,
    evaluate_traces,
    to_prompt_agent,
)
from spark_core_foundry_hosting import FoundryToolbox, InvocationsHostServer, ResponsesHostServer
from spark_core_foundry_local import (
    FoundryLocalChatOptions,
    FoundryLocalClient,
    FoundryLocalSettings,
)

__all__ = [
    "AnalysisSection",
    "AnthropicFoundryClient",
    "ContentUnderstandingContextProvider",
    "DocumentStatus",
    "FileSearchBackend",
    "FileSearchConfig",
    "FoundryAgent",
    "FoundryChatClient",
    "FoundryChatOptions",
    "FoundryEmbeddingClient",
    "FoundryEmbeddingOptions",
    "FoundryEmbeddingSettings",
    "FoundryEvals",
    "FoundryLocalChatOptions",
    "FoundryLocalClient",
    "FoundryLocalSettings",
    "FoundryMemoryProvider",
    "FoundryToolbox",
    "GeneratedEvaluatorRef",
    "InvocationsHostServer",
    "RawAnthropicFoundryClient",
    "RawFoundryAgent",
    "RawFoundryAgentChatClient",
    "RawFoundryChatClient",
    "RawFoundryEmbeddingClient",
    "ResponsesHostServer",
    "evaluate_foundry_target",
    "evaluate_traces",
    "to_prompt_agent",
]
