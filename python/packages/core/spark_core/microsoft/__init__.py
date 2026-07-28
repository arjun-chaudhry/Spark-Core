# Copyright (c) Microsoft. All rights reserved.

"""Microsoft integration namespace for optional Spark Core connectors.

This module lazily re-exports objects from:
- ``spark-core-copilotstudio``
- ``spark-core-purview``

Supported classes:
- CopilotStudioAgent
- PurviewPolicyMiddleware
- PurviewChatPolicyMiddleware
- PurviewSettings
- PurviewAppLocation
- PurviewLocationType
- PurviewAuthenticationError
- PurviewPaymentRequiredError
- PurviewRateLimitError
- PurviewRequestError
- PurviewServiceError
- CacheProvider

"""

import importlib
from typing import Any

_IMPORTS: dict[str, tuple[str, str]] = {
    "CopilotStudioAgent": ("spark_core_copilotstudio", "spark-core-copilotstudio"),
    "acquire_token": ("spark_core_copilotstudio", "spark-core-copilotstudio"),
    "PurviewPolicyMiddleware": ("spark_core_purview", "spark-core-purview"),
    "PurviewChatPolicyMiddleware": ("spark_core_purview", "spark-core-purview"),
    "PurviewSettings": ("spark_core_purview", "spark-core-purview"),
    "PurviewAppLocation": ("spark_core_purview", "spark-core-purview"),
    "PurviewLocationType": ("spark_core_purview", "spark-core-purview"),
    "PurviewAuthenticationError": ("spark_core_purview", "spark-core-purview"),
    "PurviewPaymentRequiredError": ("spark_core_purview", "spark-core-purview"),
    "PurviewRateLimitError": ("spark_core_purview", "spark-core-purview"),
    "PurviewRequestError": ("spark_core_purview", "spark-core-purview"),
    "PurviewServiceError": ("spark_core_purview", "spark-core-purview"),
    "CacheProvider": ("spark_core_purview", "spark-core-purview"),
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
    raise AttributeError(f"Module `microsoft` has no attribute {name}.")


def __dir__() -> list[str]:
    return list(_IMPORTS.keys())
