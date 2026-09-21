# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.preference_status import PreferenceStatus
from ..shared.channel_classification import ChannelClassification

__all__ = ["TopicPreference"]


class TopicPreference(BaseModel):
    default_status: PreferenceStatus
    """The topic's default status, returned on reads.

    It applies whenever the user has no override of their own (status equals this
    value).
    """

    status: PreferenceStatus
    """The user's subscription status for this topic.

    OPTED_IN or OPTED_OUT reflect the user's own choice; REQUIRED is a topic-level
    default set in the preferences editor, not a user choice.
    """

    topic_id: str
    """The unique identifier of the subscription topic this preference applies to."""

    topic_name: str
    """The display name of the subscription topic, returned on reads."""

    custom_routing: Optional[List[ChannelClassification]] = None
    """
    The channels the user has chosen to receive this topic on, present only when
    has_custom_routing is true. One or more of: direct_message, email, push, sms,
    webhook, inbox.
    """

    digest_schedule_id: Optional[str] = None
    """The digest schedule this recipient is on for the topic.

    Omitted rather than null when they have not chosen one, in which case the
    topic's default schedule applies. Ids come from the topic's digest
    configuration, returned on any read of the topic.

    Also omitted when the schedule they chose has since been deleted or disabled:
    the recipient is on the topic's default from that point on, which is how a send
    already resolves it, so the field reports what would actually be used rather
    than a dead id.
    """

    has_custom_routing: Optional[bool] = None
    """
    Whether the user has chosen specific delivery channels for this topic (listed in
    custom_routing) rather than the topic's default routing.
    """

    section_id: Optional[str] = None
    """The unique identifier of the section this topic belongs to.

    Always present when listing a user's preferences; omitted by the single-topic
    read when the topic has no resolvable section.
    """

    section_name: Optional[str] = None
    """The display name of the section this topic belongs to.

    Always present when listing a user's preferences; omitted by the single-topic
    read when the topic has no resolvable section.
    """
