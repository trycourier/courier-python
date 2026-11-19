# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["FeedbackCreateResponse"]


class FeedbackCreateResponse(BaseModel):
    feedback_id: str
    """The ID of the stored report, `fbk_` followed by a ULID."""
