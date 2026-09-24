# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["DeviceSet"]


class DeviceSet(BaseModel):
    """A named, reusable list of preview devices."""

    id: str
    """Unique identifier for the device set."""

    created_at: str
    """ISO-8601 timestamp of when the set was created."""

    device_ids: List[str]
    """The devices in this set, by `PreviewDevice.id`."""

    name: str
    """Human-readable name."""

    updated_at: str
    """ISO-8601 timestamp of when the set was last written."""

    archived_at: Optional[str] = None
    """ISO-8601 timestamp of when the set was archived.

    Present only on the archive response, which is the one place the state is
    observable.
    """
