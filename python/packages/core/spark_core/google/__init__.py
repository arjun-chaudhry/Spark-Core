# Copyright (c) Microsoft. All rights reserved.

"""Google integration namespace for optional Spark Core connectors.

This module lazily re-exports Google-hosted Anthropic clients from:
- ``spark-core-anthropic``

Supported classes:
- AnthropicVertexClient
- RawAnthropicVertexClient
"""

import importlib
from typing import Any

_IMPORTS: dict[str, tuple[str, str]] = {
    "AnthropicVertexClient": ("spark_core_anthropic", "spark-core-anthropic"),
    "RawAnthropicVertexClient": ("spark_core_anthropic", "spark-core-anthropic"),
}


def __getattr__(name: str) -> Any:
    if name in _IMPORTS:
        import_path, package_name = _IMPORTS[name]
        try:
            return getattr(importlib.import_module(import_path), name)
        except ModuleNotFoundError as exc:
            raise ModuleNotFoundError(
                f"The '{package_name}' package is not installed, please do `pip install {package_name}`"
            ) from exc
    raise AttributeError(f"Module `google` has no attribute {name}.")


def __dir__() -> list[str]:
    return list(_IMPORTS.keys())
