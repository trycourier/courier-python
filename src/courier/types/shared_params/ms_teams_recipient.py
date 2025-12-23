# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .ms_teams import MsTeams

__all__ = ["MsTeamsRecipient"]


class MsTeamsRecipient(TypedDict, total=False):
    """Send via Microsoft Teams"""

    ms_teams: Required[MsTeams]
