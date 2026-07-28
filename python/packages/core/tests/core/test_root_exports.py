# Copyright (c) Microsoft. All rights reserved.

from __future__ import annotations

import ast
from pathlib import Path

import spark_core


def _stub_all() -> set[str]:
    stub_path = Path(spark_core.__file__).with_suffix(".pyi")
    module = ast.parse(stub_path.read_text(encoding="utf-8"))
    for node in module.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__all__":
                    return set(ast.literal_eval(node.value))
    raise AssertionError("__all__ not found in spark_core root stub")


def test_root_all_matches_stub_all() -> None:
    assert set(spark_core.__all__) == _stub_all()


def test_root_star_import_loads_representative_symbols() -> None:
    namespace: dict[str, object] = {}
    exec("from spark_core import *", namespace)

    assert namespace["Agent"] is spark_core.Agent
    assert namespace["Message"] is spark_core.Message
    assert namespace["tool"] is spark_core.tool
    assert namespace["FileStoreEntry"] is spark_core.FileStoreEntry
    assert namespace["SkillsSourceContext"] is spark_core.SkillsSourceContext


def test_root_from_import_representative_symbols() -> None:
    from spark_core import Agent, FileStoreEntry, Message, SkillsSourceContext, tool

    assert Agent is spark_core.Agent
    assert Message is spark_core.Message
    assert tool is spark_core.tool
    assert FileStoreEntry is spark_core.FileStoreEntry
    assert SkillsSourceContext is spark_core.SkillsSourceContext
