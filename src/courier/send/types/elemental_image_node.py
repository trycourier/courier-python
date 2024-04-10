# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from .elemental_base_node import ElementalBaseNode
from .i_alignment import IAlignment


class ElementalImageNode(ElementalBaseNode):
    """
    Used to embed an image into the notification.
    """

    src: str = pydantic_v1.Field()
    """
    The source of the image.
    """

    href: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    A URL to link to when the image is clicked.
    """

    align: typing.Optional[IAlignment] = pydantic_v1.Field(default=None)
    """
    The alignment of the image.
    """

    alt_text: typing.Optional[str] = pydantic_v1.Field(alias="altText", default=None)
    """
    Alternate text for the image.
    """

    width: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    CSS width properties to apply to the image. For example, 50px
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
