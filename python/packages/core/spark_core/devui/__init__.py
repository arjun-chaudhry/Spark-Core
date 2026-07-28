# Copyright (c) Microsoft. All rights reserved.

"""DevUI integration namespace for optional Spark Core connectors.

This module lazily re-exports objects from:
- ``spark-core-devui``

Supported classes and functions include:
- DevServer
- SparkCoreRequest
- DiscoveryResponse
- ResponseStreamEvent
- serve
- main
"""

import importlib
from typing import Any

IMPORT_PATH = "spark_core_devui"
PACKAGE_NAME = "spark-core-devui"
_IMPORTS = [
    "SparkCoreRequest",
    "DevServer",
    "DiscoveryResponse",
    "EntityInfo",
    "OpenAIError",
    "OpenAIResponse",
    "ResponseStreamEvent",
    "main",
    "register_cleanup",
    "serve",
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
