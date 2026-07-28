# Copyright (c) Microsoft. All rights reserved.

"""Built-in tools namespace for optional Spark Core connectors.

This module lazily re-exports objects from ``spark-core-tools``.
"""

import importlib
from typing import Any

_IMPORTS: dict[str, tuple[str, str]] = {
    "DOCKER_DEFAULT_IMAGE": ("spark_core_tools.shell", "spark-core-tools"),
    "DockerNotAvailableError": ("spark_core_tools.shell", "spark-core-tools"),
    "DockerShellTool": ("spark_core_tools.shell", "spark-core-tools"),
    "LocalShellTool": ("spark_core_tools.shell", "spark-core-tools"),
    "ShellCommandError": ("spark_core_tools.shell", "spark-core-tools"),
    "ShellDecision": ("spark_core_tools.shell", "spark-core-tools"),
    "ShellEnvironmentProvider": ("spark_core_tools.shell", "spark-core-tools"),
    "ShellEnvironmentProviderOptions": ("spark_core_tools.shell", "spark-core-tools"),
    "ShellEnvironmentSnapshot": ("spark_core_tools.shell", "spark-core-tools"),
    "ShellExecutionError": ("spark_core_tools.shell", "spark-core-tools"),
    "ShellExecutor": ("spark_core_tools.shell", "spark-core-tools"),
    "ShellFamily": ("spark_core_tools.shell", "spark-core-tools"),
    "ShellMode": ("spark_core_tools.shell", "spark-core-tools"),
    "ShellPolicy": ("spark_core_tools.shell", "spark-core-tools"),
    "ShellRequest": ("spark_core_tools.shell", "spark-core-tools"),
    "ShellResult": ("spark_core_tools.shell", "spark-core-tools"),
    "ShellTimeoutError": ("spark_core_tools.shell", "spark-core-tools"),
    "default_instructions_formatter": ("spark_core_tools.shell", "spark-core-tools"),
    "is_docker_available": ("spark_core_tools.shell", "spark-core-tools"),
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
    raise AttributeError(f"Module `tools` has no attribute {name}.")


def __dir__() -> list[str]:
    return list(_IMPORTS.keys())
