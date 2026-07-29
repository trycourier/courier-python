# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["InboxResource", "AsyncInboxResource"]


class InboxResource(SyncAPIResource):
    @cached_property
    def messages(self) -> MessagesResource:
        """Manage the messages in a user's in-app inbox."""
        return MessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> InboxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return InboxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return InboxResourceWithStreamingResponse(self)


class AsyncInboxResource(AsyncAPIResource):
    @cached_property
    def messages(self) -> AsyncMessagesResource:
        """Manage the messages in a user's in-app inbox."""
        return AsyncMessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInboxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInboxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncInboxResourceWithStreamingResponse(self)


class InboxResourceWithRawResponse:
    def __init__(self, inbox: InboxResource) -> None:
        self._inbox = inbox

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        """Manage the messages in a user's in-app inbox."""
        return MessagesResourceWithRawResponse(self._inbox.messages)


class AsyncInboxResourceWithRawResponse:
    def __init__(self, inbox: AsyncInboxResource) -> None:
        self._inbox = inbox

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        """Manage the messages in a user's in-app inbox."""
        return AsyncMessagesResourceWithRawResponse(self._inbox.messages)


class InboxResourceWithStreamingResponse:
    def __init__(self, inbox: InboxResource) -> None:
        self._inbox = inbox

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        """Manage the messages in a user's in-app inbox."""
        return MessagesResourceWithStreamingResponse(self._inbox.messages)


class AsyncInboxResourceWithStreamingResponse:
    def __init__(self, inbox: AsyncInboxResource) -> None:
        self._inbox = inbox

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        """Manage the messages in a user's in-app inbox."""
        return AsyncMessagesResourceWithStreamingResponse(self._inbox.messages)
