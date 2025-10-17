# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "NotificationGetContent",
    "Block",
    "BlockContent",
    "BlockContentNotificationContentHierarchy",
    "BlockLocales",
    "BlockLocalesNotificationContentHierarchy",
    "Channel",
    "ChannelContent",
    "ChannelLocales",
]


class BlockContentNotificationContentHierarchy(BaseModel):
    children: Optional[str] = None

    parent: Optional[str] = None


BlockContent: TypeAlias = Union[str, BlockContentNotificationContentHierarchy, None]


class BlockLocalesNotificationContentHierarchy(BaseModel):
    children: Optional[str] = None

    parent: Optional[str] = None


BlockLocales: TypeAlias = Union[str, BlockLocalesNotificationContentHierarchy]


class Block(BaseModel):
    id: str

    type: Literal["action", "divider", "image", "jsonnet", "list", "markdown", "quote", "template", "text"]

    alias: Optional[str] = None

    checksum: Optional[str] = None

    content: Optional[BlockContent] = None

    context: Optional[str] = None

    locales: Optional[Dict[str, BlockLocales]] = None


class ChannelContent(BaseModel):
    subject: Optional[str] = None

    title: Optional[str] = None


class ChannelLocales(BaseModel):
    subject: Optional[str] = None

    title: Optional[str] = None


class Channel(BaseModel):
    id: str

    checksum: Optional[str] = None

    content: Optional[ChannelContent] = None

    locales: Optional[Dict[str, ChannelLocales]] = None

    type: Optional[str] = None


class NotificationGetContent(BaseModel):
    blocks: Optional[List[Block]] = None

    channels: Optional[List[Channel]] = None

    checksum: Optional[str] = None
