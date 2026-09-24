# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .preview_result_status import PreviewResultStatus
from .preview_result_failure_reason import PreviewResultFailureReason

__all__ = ["PreviewResult"]


class PreviewResult(BaseModel):
    """One device's result within a preview run."""

    device_id: str
    """The device this result is for, by `PreviewDevice.id`."""

    screenshot_url: Optional[str] = None
    """Short-lived signed URL for the full-sized image.

    Null until the screenshot exists. Re-signed on every read, so fetch it rather
    than storing it.
    """

    status: PreviewResultStatus
    """One device's outcome.

    `COMPLETED` means the screenshot exists and its URLs are populated.
    `UNSUPPORTED`, `TIMED_OUT` and `FAILED` are all terminal, and none stands in for
    another — `UNSUPPORTED` means the device was retired at the vendor, `TIMED_OUT`
    means it did not report in time.
    """

    thumbnail_url: Optional[str] = None
    """Short-lived signed URL for the grid-sized image.

    Null until the screenshot exists. Re-signed on every read, so fetch it rather
    than storing it.
    """

    failure_reason: Optional[PreviewResultFailureReason] = None
    """
    Why one device's render failed, when its `status` is `FAILED` and the cause has
    a public name. `DELIVERY_FAILED` means the rendering service could not deliver
    the message to its own capture mailbox — infrastructure, not anything wrong with
    the template.
    """
