# Copyright (c) Microsoft. All rights reserved.

"""Anthropic integration namespace for optional Spark Core connectors.

This module lazily re-exports objects from:
- ``spark-core-anthropic``
- ``spark-core-claude``

Supported classes:
- AnthropicBedrockClient
- AnthropicClient
- AnthropicChatOptions
- AnthropicFoundryClient
- AnthropicVertexClient
- ClaudeAgent
- ClaudeAgentOptions
- RawAnthropicBedrockClient
- RawAnthropicClient
- RawAnthropicFoundryClient
- RawClaudeAgent
- RawAnthropicVertexClient
"""

import importlib
from typing import Any

_IMPORTS: dict[str, tuple[str, str]] = {
    "AnthropicBedrockClient": ("spark_core_anthropic", "spark-core-anthropic"),
    "AnthropicClient": ("spark_core_anthropic", "spark-core-anthropic"),
    "AnthropicChatOptions": ("spark_core_anthropic", "spark-core-anthropic"),
    "AnthropicFoundryClient": ("spark_core_anthropic", "spark-core-anthropic"),
    "AnthropicVertexClient": ("spark_core_anthropic", "spark-core-anthropic"),
    "ClaudeAgent": ("spark_core_claude", "spark-core-claude"),
    "ClaudeAgentOptions": ("spark_core_claude", "spark-core-claude"),
    "RawAnthropicBedrockClient": ("spark_core_anthropic", "spark-core-anthropic"),
    "RawAnthropicClient": ("spark_core_anthropic", "spark-core-anthropic"),
    "RawAnthropicFoundryClient": ("spark_core_anthropic", "spark-core-anthropic"),
    "RawClaudeAgent": ("spark_core_claude", "spark-core-claude"),
    "RawAnthropicVertexClient": ("spark_core_anthropic", "spark-core-anthropic"),
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
    raise AttributeError(f"Module `anthropic` has no attribute {name}.")


def __dir__() -> list[str]:
    return list(_IMPORTS.keys())
