# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...commons.types.recipient_preferences import RecipientPreferences
from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from ...core.unchecked_base_model import UncheckedBaseModel


class GetListSubscriptionsList(UncheckedBaseModel):
    id: str
    name: str = pydantic_v1.Field()
    """
    List name
    """

    created: str = pydantic_v1.Field()
    """
    The date/time of when the list was created. Represented as a string in ISO format.
    """

    updated: str = pydantic_v1.Field()
    """
    The date/time of when the list was updated. Represented as a string in ISO format.
    """

    preferences: typing.Optional[RecipientPreferences] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
