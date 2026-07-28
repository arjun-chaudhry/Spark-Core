# Copyright (c) Microsoft. All rights reserved.

"""OpenAI namespace for Spark Core clients.

This module lazily re-exports objects from the ``spark-core-openai`` package.
Install it with: ``pip install spark-core-openai``

Supported classes include:
- OpenAIChatClient (Responses API)
- OpenAIChatCompletionClient (Chat Completions API)
- OpenAIEmbeddingClient
"""

import importlib
from typing import Any

_IMPORTS: dict[str, tuple[str, str]] = {
    "OpenAIChatClient": ("spark_core_openai", "spark-core-openai"),
    "OpenAIChatOptions": ("spark_core_openai", "spark-core-openai"),
    "OpenAIContinuationToken": ("spark_core_openai", "spark-core-openai"),
    "RawOpenAIChatClient": ("spark_core_openai", "spark-core-openai"),
    "OpenAIChatCompletionClient": ("spark_core_openai", "spark-core-openai"),
    "OpenAIChatCompletionOptions": ("spark_core_openai", "spark-core-openai"),
    "RawOpenAIChatCompletionClient": ("spark_core_openai", "spark-core-openai"),
    "OpenAIEmbeddingClient": ("spark_core_openai", "spark-core-openai"),
    "OpenAIEmbeddingOptions": ("spark_core_openai", "spark-core-openai"),
    "OpenAISettings": ("spark_core_openai", "spark-core-openai"),
    "ContentFilterResultSeverity": ("spark_core_openai", "spark-core-openai"),
    "OpenAIContentFilterException": ("spark_core_openai", "spark-core-openai"),
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
    raise AttributeError(f"Module `openai` has no attribute {name}.")


def __dir__() -> list[str]:
    return list(_IMPORTS.keys())
