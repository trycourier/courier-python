# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["JourneyRunStep"]


class JourneyRunStep(BaseModel):
    """One executed node of a Journey run.

    `node_id` is the id of the node in the published Journey, so a step maps directly onto the Journey graph.
    """

    action: str
    """The kind of node that ran, e.g. `send`, `delay`, or `exit`."""

    status: str
    """The state of the step: the seven run statuses, plus `SKIPPED` and `COMPUTING`.

    Not an enum — new values have been added before.
    """

    created_at: Optional[str] = None
    """When the step started, as an ISO 8601 timestamp."""

    message_id: Optional[str] = None
    """The message this step produced, present on send steps.

    Pass it to `GET /messages/{message_id}` for delivery status. A send to a List or
    an Audience yields one id for the request, not one per recipient.
    """

    node_id: Optional[str] = None
    """The id of the node in the published Journey that this step executed."""

    updated_at: Optional[str] = None
    """When the step last changed state, as an ISO 8601 timestamp."""
