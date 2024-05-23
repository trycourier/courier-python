# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....commons.types.channel_classification import ChannelClassification
from ....commons.types.preference_status import PreferenceStatus
from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from ....core.unchecked_base_model import UncheckedBaseModel


class TopicPreferenceUpdate(UncheckedBaseModel):
    status: PreferenceStatus
    custom_routing: typing.Optional[typing.List[ChannelClassification]] = pydantic_v1.Field(default=None)
    """
    The Channels a user has chosen to receive notifications through for this topic
    """

    has_custom_routing: typing.Optional[bool] = None

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
