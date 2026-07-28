# Copyright (c) Microsoft. All rights reserved.

"""ChatKit integration namespace for optional Spark Core connectors.

This module lazily re-exports objects from:
- ``spark-core-chatkit``

Supported classes and functions:
- ThreadItemConverter
- simple_to_agent_input
- stream_agent_response
"""

import importlib
from typing import Any

IMPORT_PATH = "spark_core_chatkit"
PACKAGE_NAME = "spark-core-chatkit"
_IMPORTS = ["ThreadItemConverter", "simple_to_agent_input", "stream_agent_response"]


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
