# Copyright (c) Microsoft. All rights reserved.

"""Hyperlight CodeAct namespace for optional Spark Core connectors.

This module lazily re-exports objects from ``spark-core-hyperlight``.
"""

import importlib
from typing import Any

_IMPORTS: dict[str, tuple[str, str]] = {
    "AllowedDomain": ("spark_core_hyperlight", "spark-core-hyperlight"),
    "AllowedDomainInput": ("spark_core_hyperlight", "spark-core-hyperlight"),
    "FileMount": ("spark_core_hyperlight", "spark-core-hyperlight"),
    "FileMountInput": ("spark_core_hyperlight", "spark-core-hyperlight"),
    "HyperlightCodeActProvider": ("spark_core_hyperlight", "spark-core-hyperlight"),
    "HyperlightExecuteCodeTool": ("spark_core_hyperlight", "spark-core-hyperlight"),
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
    raise AttributeError(f"Module `hyperlight` has no attribute {name}.")


def __dir__() -> list[str]:
    return list(_IMPORTS.keys())
