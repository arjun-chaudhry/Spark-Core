# Copyright (c) Microsoft. All rights reserved.

"""A2A integration namespace for optional Spark Core connectors.

This module lazily re-exports objects from:
- ``spark-core-a2a``

Supported classes:
- A2AAgent
- A2AAgentSession
- A2AServiceSessionId
- A2AExecutor
"""

import importlib
from typing import Any

IMPORT_PATH = "spark_core_a2a"
PACKAGE_NAME = "spark-core-a2a"
_IMPORTS = ["A2AAgent", "A2AAgentSession", "A2AServiceSessionId", "A2AExecutor"]


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
