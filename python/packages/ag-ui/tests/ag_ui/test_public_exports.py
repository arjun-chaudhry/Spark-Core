# Copyright (c) Microsoft. All rights reserved.

"""Public export coverage for AG-UI package surfaces."""


def test_spark_core_ag_ui_exports_workflow() -> None:
    """Runtime package should export SparkCoreWorkflow."""
    from spark_core_ag_ui import SparkCoreWorkflow

    assert SparkCoreWorkflow.__name__ == "SparkCoreWorkflow"


def test_core_ag_ui_lazy_exports_include_only_stable_api() -> None:
    """Core facade should expose only the stable high-level AG-UI API."""
    from spark_core import ag_ui

    assert hasattr(ag_ui, "SparkCoreWorkflow")
    assert hasattr(ag_ui, "SparkCoreAgent")
    assert hasattr(ag_ui, "AGUIChatClient")
    assert hasattr(ag_ui, "add_spark_core_fastapi_endpoint")
    assert hasattr(ag_ui, "state_update")

    assert not hasattr(ag_ui, "WorkflowFactory")
    assert not hasattr(ag_ui, "AGUIRequest")
    assert not hasattr(ag_ui, "RunMetadata")


def test_spark_core_ag_ui_exports_state_update() -> None:
    """Runtime package should export the ``state_update`` helper."""
    from spark_core_ag_ui import state_update

    assert callable(state_update)


def test_spark_core_ag_ui_exports_snapshot_primitives() -> None:
    """Runtime package should export AG-UI Thread Snapshot primitives."""
    from spark_core_ag_ui import (
        DEFAULT_MAX_THREAD_SNAPSHOTS,
        AGUIThreadSnapshot,
        AGUIThreadSnapshotStore,
        InMemoryAGUIThreadSnapshotStore,
    )

    assert AGUIThreadSnapshot.__name__ == "AGUIThreadSnapshot"
    assert AGUIThreadSnapshotStore.__name__ == "AGUIThreadSnapshotStore"
    assert InMemoryAGUIThreadSnapshotStore.__name__ == "InMemoryAGUIThreadSnapshotStore"
    assert DEFAULT_MAX_THREAD_SNAPSHOTS >= 1


def test_core_ag_ui_lazy_exports_include_event_converter_and_http_service() -> None:
    """Core facade must expose AGUIEventConverter, AGUIHttpService, and __version__."""
    from spark_core import ag_ui

    assert hasattr(ag_ui, "AGUIEventConverter")
    assert hasattr(ag_ui, "AGUIHttpService")
    assert hasattr(ag_ui, "__version__")


def test_core_ag_ui_lazy_exports_include_snapshot_primitives() -> None:
    """Core facade must expose snapshot primitives needed for endpoint configuration."""
    from spark_core import ag_ui

    assert hasattr(ag_ui, "AGUIThreadSnapshot")
    assert hasattr(ag_ui, "AGUIThreadSnapshotStore")
    assert hasattr(ag_ui, "InMemoryAGUIThreadSnapshotStore")
    assert hasattr(ag_ui, "SnapshotScopeResolver")
