# Copyright (c) Microsoft. All rights reserved.

"""Monty CodeAct namespace for optional Spark Core connectors.

This module lazily re-exports objects from ``spark-core-monty``.
"""

import importlib
from typing import Any

_IMPORTS: dict[str, tuple[str, str]] = {
    "FileMount": ("spark_core_monty", "spark-core-monty"),
    "FileMountInput": ("spark_core_monty", "spark-core-monty"),
    "MontyCodeActProvider": ("spark_core_monty", "spark-core-monty"),
    "MontyExecuteCodeTool": ("spark_core_monty", "spark-core-monty"),
    "MountMode": ("spark_core_monty", "spark-core-monty"),
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
    raise AttributeError(f"Module `monty` has no attribute {name}.")


def __dir__() -> list[str]:
    return list(_IMPORTS.keys())
