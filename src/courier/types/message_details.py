# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MessageDetails"]


class MessageDetails(BaseModel):
    id: str
    """
    A unique identifier associated with the message you wish to retrieve (results
    from a send).
    """

    clicked: int
    """
    A UTC timestamp at which the recipient clicked on a tracked link for the first
    time. Stored as a millisecond representation of the Unix epoch.
    """

    delivered: int
    """A UTC timestamp at which the Integration provider delivered the message.

    Stored as a millisecond representation of the Unix epoch.
    """

    enqueued: int
    """A UTC timestamp at which Courier received the message request.

    Stored as a millisecond representation of the Unix epoch.
    """

    event: str
    """A unique identifier associated with the event of the delivered message."""

    notification: str
    """A unique identifier associated with the notification of the delivered message."""

    opened: int
    """A UTC timestamp at which the recipient opened a message for the first time.

    Stored as a millisecond representation of the Unix epoch.
    """

    recipient: str
    """A unique identifier associated with the recipient of the delivered message."""

    sent: int
    """A UTC timestamp at which Courier passed the message to the Integration provider.

    Stored as a millisecond representation of the Unix epoch.
    """

    status: Literal[
        "CANCELED",
        "CLICKED",
        "DELAYED",
        "DELIVERED",
        "DIGESTED",
        "ENQUEUED",
        "FILTERED",
        "OPENED",
        "ROUTED",
        "SENT",
        "SIMULATED",
        "THROTTLED",
        "UNDELIVERABLE",
        "UNMAPPED",
        "UNROUTABLE",
    ]
    """The current status of the message."""

    error: Optional[str] = None
    """A message describing the error that occurred."""

    reason: Optional[
        Literal[
            "BOUNCED",
            "FAILED",
            "FILTERED",
            "NO_CHANNELS",
            "NO_PROVIDERS",
            "OPT_IN_REQUIRED",
            "PROVIDER_ERROR",
            "UNPUBLISHED",
            "UNSUBSCRIBED",
        ]
    ] = None
    """The reason for the current status of the message."""
