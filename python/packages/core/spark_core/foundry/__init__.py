# Copyright (c) Microsoft. All rights reserved.

"""Foundry integration namespace for optional Spark Core connectors.

This module lazily re-exports objects from:
- ``spark-core-anthropic``
- ``spark-core-azure-contentunderstanding``
- ``spark-core-foundry``
- ``spark-core-foundry-hosting``
- ``spark-core-foundry-local``
"""

import importlib
from typing import Any

_IMPORTS: dict[str, tuple[str, str]] = {
    "AnalysisSection": ("spark_core_azure_contentunderstanding", "spark-core-azure-contentunderstanding"),
    "AnthropicFoundryClient": ("spark_core_anthropic", "spark-core-anthropic"),
    "ContentUnderstandingContextProvider": (
        "spark_core_azure_contentunderstanding",
        "spark-core-azure-contentunderstanding",
    ),
    "DocumentStatus": ("spark_core_azure_contentunderstanding", "spark-core-azure-contentunderstanding"),
    "FileSearchBackend": ("spark_core_azure_contentunderstanding", "spark-core-azure-contentunderstanding"),
    "FileSearchConfig": ("spark_core_azure_contentunderstanding", "spark-core-azure-contentunderstanding"),
    "FoundryAgent": ("spark_core_foundry", "spark-core-foundry"),
    "FoundryAgentOptions": ("spark_core_foundry", "spark-core-foundry"),
    "FoundryChatClient": ("spark_core_foundry", "spark-core-foundry"),
    "FoundryChatOptions": ("spark_core_foundry", "spark-core-foundry"),
    "FoundryEmbeddingClient": ("spark_core_foundry", "spark-core-foundry"),
    "FoundryEmbeddingOptions": ("spark_core_foundry", "spark-core-foundry"),
    "FoundryEmbeddingSettings": ("spark_core_foundry", "spark-core-foundry"),
    "FoundryEvals": ("spark_core_foundry", "spark-core-foundry"),
    "FoundryMemoryProvider": ("spark_core_foundry", "spark-core-foundry"),
    "FoundryToolbox": ("spark_core_foundry_hosting", "spark-core-foundry-hosting"),
    "FoundryLocalChatOptions": ("spark_core_foundry_local", "spark-core-foundry-local"),
    "FoundryLocalClient": ("spark_core_foundry_local", "spark-core-foundry-local"),
    "FoundryLocalSettings": ("spark_core_foundry_local", "spark-core-foundry-local"),
    "GeneratedEvaluatorRef": ("spark_core_foundry", "spark-core-foundry"),
    "RawAnthropicFoundryClient": ("spark_core_anthropic", "spark-core-anthropic"),
    "RawFoundryAgent": ("spark_core_foundry", "spark-core-foundry"),
    "RawFoundryAgentChatClient": ("spark_core_foundry", "spark-core-foundry"),
    "RawFoundryChatClient": ("spark_core_foundry", "spark-core-foundry"),
    "RawFoundryEmbeddingClient": ("spark_core_foundry", "spark-core-foundry"),
    "InvocationsHostServer": ("spark_core_foundry_hosting", "spark-core-foundry-hosting"),
    "ResponsesHostServer": ("spark_core_foundry_hosting", "spark-core-foundry-hosting"),
    "evaluate_foundry_target": ("spark_core_foundry", "spark-core-foundry"),
    "evaluate_traces": ("spark_core_foundry", "spark-core-foundry"),
    "to_prompt_agent": ("spark_core_foundry", "spark-core-foundry"),
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
    raise AttributeError(f"Module `foundry` has no attribute {name}.")


def __dir__() -> list[str]:
    return list(_IMPORTS.keys())
