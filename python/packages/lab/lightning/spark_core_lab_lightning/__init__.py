# Copyright (c) Microsoft. All rights reserved.

"""RL Module for Spark Core."""

from __future__ import annotations

import importlib.metadata

from spark_core.observability import enable_instrumentation
from agentlightning.tracer import (
    AgentOpsTracer,
)

try:
    __version__ = importlib.metadata.version(__name__)
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0"  # Fallback for development mode


class SparkCoreTracer(AgentOpsTracer):
    """Tracer for Spark-Core.

    Tracer that enables OpenTelemetry observability for the Spark-Core,
    so that the traces are visible to Agent-lightning.
    """

    def init(self) -> None:
        """Initialize the spark-core-lab-lightning for training."""
        enable_instrumentation()
        super().init()

    def teardown(self) -> None:
        """Teardown the spark-core-lab-lightning for training."""
        super().teardown()


__all__: list[str] = ["SparkCoreTracer"]
