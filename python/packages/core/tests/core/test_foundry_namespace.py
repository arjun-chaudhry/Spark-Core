# Copyright (c) Microsoft. All rights reserved.

import pytest

import spark_core.azure as azure
import spark_core.foundry as foundry

_foundry = pytest.importorskip("spark_core_foundry")
_foundry_hosting = pytest.importorskip("spark_core_foundry_hosting")
_foundry_local = pytest.importorskip("spark_core_foundry_local")

FoundryChatClient = _foundry.FoundryChatClient
FoundryMemoryProvider = _foundry.FoundryMemoryProvider
ResponsesHostServer = _foundry_hosting.ResponsesHostServer
FoundryLocalClient = _foundry_local.FoundryLocalClient


def test_foundry_namespace_exposes_cloud_and_local_symbols() -> None:
    assert foundry.FoundryChatClient is FoundryChatClient
    assert foundry.FoundryMemoryProvider is FoundryMemoryProvider
    assert foundry.ResponsesHostServer is ResponsesHostServer
    assert foundry.FoundryLocalClient is FoundryLocalClient
    assert "FoundryChatClient" in dir(foundry)
    assert "FoundryLocalClient" in dir(foundry)
    assert "ResponsesHostServer" in dir(foundry)


def test_azure_namespace_no_longer_exposes_foundry_symbols() -> None:
    assert "FoundryChatClient" not in dir(azure)
    assert "FoundryLocalClient" not in dir(azure)

    with pytest.raises(AttributeError, match="Module `azure` has no attribute FoundryChatClient\\."):
        _ = azure.FoundryChatClient  # type: ignore[attr-defined]  # ty: ignore[unresolved-attribute]
