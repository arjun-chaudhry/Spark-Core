# Copyright (c) Microsoft. All rights reserved.

"""Azure integration namespace for optional Spark Core connectors.

This module lazily re-exports objects from optional Azure connector packages.
"""

import importlib
from typing import Any

_IMPORTS: dict[str, tuple[str, str]] = {
    "AgentCallbackContext": ("spark_core_durabletask", "spark-core-durabletask"),
    "AgentFunctionApp": ("spark_core_azurefunctions", "spark-core-azurefunctions"),
    "AgentResponseCallbackProtocol": ("spark_core_durabletask", "spark-core-durabletask"),
    "AzureAISearchContextProvider": ("spark_core_azure_ai_search", "spark-core-azure-ai-search"),
    "AzureAISearchSettings": ("spark_core_azure_ai_search", "spark-core-azure-ai-search"),
    "CosmosHistoryProvider": ("spark_core_azure_cosmos", "spark-core-azure-cosmos"),
    "DurableAIAgent": ("spark_core_durabletask", "spark-core-durabletask"),
    "DurableAIAgentClient": ("spark_core_durabletask", "spark-core-durabletask"),
    "DurableAIAgentOrchestrationContext": ("spark_core_durabletask", "spark-core-durabletask"),
    "DurableAIAgentWorker": ("spark_core_durabletask", "spark-core-durabletask"),
    "DurableWorkflowClient": ("spark_core_durabletask", "spark-core-durabletask"),
    "WorkflowHitlContext": ("spark_core_azurefunctions", "spark-core-azurefunctions"),
}


def __getattr__(name: str) -> Any:
    if name in _IMPORTS:
        import_path, package_name = _IMPORTS[name]
        try:
            return getattr(importlib.import_module(import_path), name)
        except ModuleNotFoundError as exc:
            raise ModuleNotFoundError(
                f"The package {package_name} is required to use `{name}`. "
                f"Please use `pip install {package_name}`, or update your requirements.txt or pyproject.toml file."
            ) from exc
    raise AttributeError(f"Module `azure` has no attribute {name}.")


def __dir__() -> list[str]:
    return list(_IMPORTS.keys())
