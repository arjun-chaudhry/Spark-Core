# Copyright (c) Microsoft. All rights reserved.

"""Backend tool rendering endpoint."""

from typing import Any, cast

from spark_core._clients import SupportsChatGetResponse
from spark_core.ag_ui import add_spark_core_fastapi_endpoint
from spark_core.openai import OpenAIChatCompletionClient
from fastapi import FastAPI

from ...agents.weather_agent import weather_agent


def register_backend_tool_rendering(app: FastAPI) -> None:
    """Register the backend tool rendering endpoint.

    Args:
        app: The FastAPI application.
    """
    # Create a chat client and call the factory function
    client = cast(SupportsChatGetResponse[Any], OpenAIChatCompletionClient())

    add_spark_core_fastapi_endpoint(
        app,
        weather_agent(client),
        "/backend_tool_rendering",
    )
