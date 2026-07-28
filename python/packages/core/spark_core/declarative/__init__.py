# Copyright (c) Microsoft. All rights reserved.

"""Declarative integration namespace for optional Spark Core connectors.

This module lazily re-exports objects from:
- ``spark-core-declarative``

Supported classes include:
- AgentFactory
- WorkflowFactory
- ExternalInputRequest
- ExternalInputResponse
"""

import importlib
from typing import Any

IMPORT_PATH = "spark_core_declarative"
PACKAGE_NAME = "spark-core-declarative"
_IMPORTS = [
    "AgentFactory",
    "AgentExternalInputRequest",
    "AgentExternalInputResponse",
    "DeclarativeActionError",
    "DeclarativeLoaderError",
    "DeclarativeWorkflowError",
    "DefaultHttpRequestHandler",
    "DefaultMCPToolHandler",
    "ExternalInputRequest",
    "ExternalInputResponse",
    "HttpRequestHandler",
    "HttpRequestInfo",
    "HttpRequestResult",
    "MCPToolApprovalRequest",
    "MCPToolHandler",
    "MCPToolInvocation",
    "MCPToolResult",
    "ProviderLookupError",
    "ProviderTypeMapping",
    "ToolApprovalRequest",
    "ToolApprovalResponse",
    "WorkflowFactory",
    "WorkflowState",
]


def __getattr__(name: str) -> Any:
    if name in _IMPORTS:
        try:
            return getattr(importlib.import_module(IMPORT_PATH), name)
        except ModuleNotFoundError as exc:
            raise ModuleNotFoundError(
                f"The '{PACKAGE_NAME}' package is not installed, please do `pip install {PACKAGE_NAME}`"
            ) from exc
    raise AttributeError(f"Module {IMPORT_PATH} has no attribute {name}.")


def __dir__() -> list[str]:
    return _IMPORTS
