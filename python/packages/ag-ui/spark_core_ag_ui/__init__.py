# Copyright (c) Microsoft. All rights reserved.

"""AG-UI protocol integration for Spark Core."""

import importlib.metadata

from ._agent import SparkCoreAgent
from ._client import AGUIChatClient
from ._endpoint import add_spark_core_fastapi_endpoint
from ._event_converters import AGUIEventConverter
from ._http_service import AGUIHttpService
from ._snapshots import (
    DEFAULT_MAX_THREAD_SNAPSHOTS,
    AGUIThreadID,
    AGUIThreadSnapshot,
    AGUIThreadSnapshotStore,
    InMemoryAGUIThreadSnapshotStore,
    SnapshotScope,
    SnapshotScopeResolver,
)
from ._state import state_update
from ._types import AgentState, AGUIChatOptions, AGUIRequest, PredictStateConfig, RunMetadata
from ._workflow import SparkCoreWorkflow, WorkflowFactory

try:
    __version__ = importlib.metadata.version(__name__)
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0"

# Default OpenAPI tags for AG-UI endpoints
DEFAULT_TAGS = ["AG-UI"]

__all__ = [
    "SparkCoreAgent",
    "SparkCoreWorkflow",
    "WorkflowFactory",
    "add_spark_core_fastapi_endpoint",
    "AGUIChatClient",
    "AGUIChatOptions",
    "AGUIEventConverter",
    "AGUIHttpService",
    "AGUIRequest",
    "AGUIThreadID",
    "AGUIThreadSnapshot",
    "AGUIThreadSnapshotStore",
    "AgentState",
    "InMemoryAGUIThreadSnapshotStore",
    "PredictStateConfig",
    "RunMetadata",
    "SnapshotScope",
    "SnapshotScopeResolver",
    "DEFAULT_MAX_THREAD_SNAPSHOTS",
    "DEFAULT_TAGS",
    "state_update",
    "__version__",
]
