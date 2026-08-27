# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .ms_teams import MsTeams
from ..._models import BaseModel

__all__ = ["MsTeamsRecipient"]


class MsTeamsRecipient(BaseModel):
    """Send via Microsoft Teams"""

    ms_teams: MsTeams
    """Provide at least one of `tenant_id` or `service_url`.

    If you provide both, they must agree.
    """
