# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._models import BaseModel

__all__ = ["AudienceUpdateResponse"]


class AudienceUpdateResponse(BaseModel):
    audience: "Audience"


from .audience import Audience
