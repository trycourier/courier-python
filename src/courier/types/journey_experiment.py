# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .journey_experiment_variant import JourneyExperimentVariant

__all__ = ["JourneyExperiment"]


class JourneyExperiment(BaseModel):
    """A/B experiment config for a send node.

    The recipient is deterministically bucketed by `bucketingKey` and routed to one of the `variants` in proportion to its `weight`. Present on a send node INSTEAD OF `message.template`.
    """

    bucketing_key: str = FieldInfo(alias="bucketingKey")
    """The value used to deterministically assign a recipient to a variant.

    Must be non-empty with no leading or trailing whitespace.
    """

    variants: List[JourneyExperimentVariant]
    """Between 2 and 10 weighted template variants."""

    id: Optional[str] = None
    """Unique experiment id (prefixed `exp_`).

    Omit to have one generated automatically; when supplied it must be a valid
    `exp_` id.
    """

    name: Optional[str] = None
    """Optional display name for the experiment."""
