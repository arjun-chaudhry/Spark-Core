# Copyright (c) Microsoft. All rights reserved.

"""GitHub integration namespace for optional Spark Core connectors.

This module lazily re-exports objects from:
- ``spark-core-github-copilot``

Supported classes:
- GitHubCopilotAgent
- GitHubCopilotOptions
- GitHubCopilotSettings
- RawGitHubCopilotAgent
"""

import importlib
from typing import Any

_IMPORTS: dict[str, tuple[str, str]] = {
    "GitHubCopilotAgent": ("spark_core_github_copilot", "spark-core-github-copilot"),
    "GitHubCopilotOptions": ("spark_core_github_copilot", "spark-core-github-copilot"),
    "GitHubCopilotSettings": ("spark_core_github_copilot", "spark-core-github-copilot"),
    "RawGitHubCopilotAgent": ("spark_core_github_copilot", "spark-core-github-copilot"),
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
    raise AttributeError(f"Module `spark_core.github` has no attribute {name}.")


def __dir__() -> list[str]:
    return list(_IMPORTS.keys())
