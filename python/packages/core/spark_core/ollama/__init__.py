# Copyright (c) Microsoft. All rights reserved.

"""Ollama integration namespace for optional Spark Core connectors.

This module lazily re-exports objects from:
- ``spark-core-ollama``

Supported classes:
- OllamaChatClient
- OllamaChatOptions
- OllamaEmbeddingClient
- OllamaEmbeddingOptions
- OllamaEmbeddingSettings
- OllamaSettings
"""

import importlib
from typing import Any

IMPORT_PATH = "spark_core_ollama"
PACKAGE_NAME = "spark-core-ollama"
_IMPORTS = [
    "OllamaChatClient",
    "OllamaChatOptions",
    "OllamaEmbeddingClient",
    "OllamaEmbeddingOptions",
    "OllamaEmbeddingSettings",
    "OllamaSettings",
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
