# Copyright (c) Microsoft. All rights reserved.

# Type stubs for the spark_core.azure lazy-loading namespace.
# Install the relevant packages for full type support.

from spark_core_azure_ai_search import (
    AzureAISearchContextProvider,
    AzureAISearchSettings,
)
from spark_core_azure_cosmos import CosmosHistoryProvider
from spark_core_azurefunctions import AgentFunctionApp, WorkflowHitlContext
from spark_core_durabletask import (
    AgentCallbackContext,
    AgentResponseCallbackProtocol,
    DurableAIAgent,
    DurableAIAgentClient,
    DurableAIAgentOrchestrationContext,
    DurableAIAgentWorker,
    DurableWorkflowClient,
)

__all__ = [
    "AgentCallbackContext",
    "AgentFunctionApp",
    "AgentResponseCallbackProtocol",
    "AzureAISearchContextProvider",
    "AzureAISearchSettings",
    "CosmosHistoryProvider",
    "DurableAIAgent",
    "DurableAIAgentClient",
    "DurableAIAgentOrchestrationContext",
    "DurableAIAgentWorker",
    "DurableWorkflowClient",
    "WorkflowHitlContext",
]
