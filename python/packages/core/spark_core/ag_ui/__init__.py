# Copyright (c) Microsoft. All rights reserved.

"""AG-UI integration namespace for optional Spark Core connectors.

This module lazily re-exports objects from:
- ``spark-core-ag-ui``

Supported classes and functions:
- SparkCoreAgent
- SparkCoreWorkflow
- AGUIChatClient
- AGUIEventConverter
- AGUIHttpService
- AGUIThreadSnapshot
- AGUIThreadSnapshotStore
- InMemoryAGUIThreadSnapshotStore
- SnapshotScopeResolver
- add_spark_core_fastapi_endpoint
- state_update
- __version__
"""

import importlib
from typing import Any

IMPORT_PATH = "spark_core_ag_ui"
PACKAGE_NAME = "spark-core-ag-ui"
_IMPORTS = [
    "SparkCoreAgent",
    "SparkCoreWorkflow",
    "add_spark_core_fastapi_endpoint",
    "AGUIChatClient",
    "AGUIEventConverter",
    "AGUIHttpService",
    "AGUIThreadSnapshot",
    "AGUIThreadSnapshotStore",
    "InMemoryAGUIThreadSnapshotStore",
    "SnapshotScopeResolver",
    "state_update",
    "__version__",
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
