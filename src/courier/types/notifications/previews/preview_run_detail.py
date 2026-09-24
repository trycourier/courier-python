# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .preview_result import PreviewResult
from .preview_run_status import PreviewRunStatus
from .preview_run_failure_reason import PreviewRunFailureReason

__all__ = ["PreviewRunDetail"]


class PreviewRunDetail(BaseModel):
    """A preview run together with its per-device results."""

    id: str
    """Unique identifier for the preview run."""

    created_at: str
    """ISO-8601 timestamp of when the run was created."""

    device_ids: List[str]
    """The devices this run was submitted for, snapshotted when the run was created."""

    results: List[PreviewResult]
    """One entry per device in `device_ids`."""

    status: PreviewRunStatus
    """Where the run itself has got to.

    `PENDING` and `RENDERED` mean Courier is still preparing the email, `SUBMITTED`
    means it is with the rendering service, and `COMPLETED` means every device has
    reported. `FAILED` is the run as a whole failing — an individual device failing
    never fails the run.
    """

    template_id: str
    """The template that was rendered."""

    failure_reason: Optional[PreviewRunFailureReason] = None
    """Why the run failed, when `status` is `FAILED`.

    `NO_EMAIL_CHANNEL` and `TEMPLATE_NOT_SUPPORTED` mean there was nothing to
    render; `ALL_DEVICES_UNSUPPORTED` means every requested device has been retired
    and the request can be fixed by choosing others.
    """

    template_version: Optional[str] = None
    """
    The version of the template that was rendered — `draft`, or a zero-padded
    published version such as `v002`. Absent until the render settles.
    """
