# Copyright (c) Microsoft. All rights reserved.

"""Amazon Bedrock integration namespace for optional Spark Core connectors.

This module lazily re-exports objects from:
- ``spark-core-anthropic``
- ``spark-core-bedrock``

Supported classes:
- AnthropicBedrockClient
- BedrockChatClient
- BedrockChatOptions
- BedrockEmbeddingClient
- BedrockEmbeddingOptions
- BedrockEmbeddingSettings
- BedrockGuardrailConfig
- BedrockSettings
- RawAnthropicBedrockClient
"""

import importlib
from typing import Any

_IMPORTS: dict[str, tuple[str, str]] = {
    "AnthropicBedrockClient": ("spark_core_anthropic", "spark-core-anthropic"),
    "BedrockChatClient": ("spark_core_bedrock", "spark-core-bedrock"),
    "BedrockChatOptions": ("spark_core_bedrock", "spark-core-bedrock"),
    "BedrockEmbeddingClient": ("spark_core_bedrock", "spark-core-bedrock"),
    "BedrockEmbeddingOptions": ("spark_core_bedrock", "spark-core-bedrock"),
    "BedrockEmbeddingSettings": ("spark_core_bedrock", "spark-core-bedrock"),
    "BedrockGuardrailConfig": ("spark_core_bedrock", "spark-core-bedrock"),
    "BedrockSettings": ("spark_core_bedrock", "spark-core-bedrock"),
    "RawAnthropicBedrockClient": ("spark_core_anthropic", "spark-core-anthropic"),
}


def __getattr__(name: str) -> Any:
    if name in _IMPORTS:
        import_path, package_name = _IMPORTS[name]
        try:
            return getattr(importlib.import_module(import_path), name)
        except ModuleNotFoundError as exc:
            raise ModuleNotFoundError(
                f"The '{package_name}' package is not installed, please do `pip install {package_name}`"
            ) from exc
    raise AttributeError(f"Module `amazon` has no attribute {name}.")


def __dir__() -> list[str]:
    return list(_IMPORTS.keys())
