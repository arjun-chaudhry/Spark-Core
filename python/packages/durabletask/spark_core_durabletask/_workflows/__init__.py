# Copyright (c) Microsoft. All rights reserved.

"""Durable hosting of Spark Core workflows.

This subpackage turns a Spark Core :class:`~spark_core.Workflow` into durable
primitives -- a single orchestrator, agent entities, and non-agent executor
activities -- that run on either a standalone Durable Task worker or Azure
Functions. The host-agnostic engine lives here; each host programs against the
:class:`~.context.WorkflowOrchestrationContext` protocol.
"""
