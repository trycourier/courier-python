# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["JourneysInvokeResponse"]


class JourneysInvokeResponse(BaseModel):
    run_id: str = FieldInfo(alias="runId")
    """A unique identifier for the journey run that was created."""
