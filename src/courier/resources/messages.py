# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import message_list_params, message_history_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.message_details import MessageDetails
from ..types.message_list_response import MessageListResponse
from ..types.message_content_response import MessageContentResponse
from ..types.message_history_response import MessageHistoryResponse
from ..types.message_retrieve_response import MessageRetrieveResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageRetrieveResponse:
        """
        Fetch the status of a message you've previously sent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get(
            f"/messages/{message_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageRetrieveResponse,
        )

    def list(
        self,
        *,
        archived: Optional[bool] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        enqueued_after: Optional[str] | Omit = omit,
        event: Optional[str] | Omit = omit,
        list: Optional[str] | Omit = omit,
        message_id: Optional[str] | Omit = omit,
        notification: Optional[str] | Omit = omit,
        provider: SequenceNotStr[Optional[str]] | Omit = omit,
        recipient: Optional[str] | Omit = omit,
        status: SequenceNotStr[Optional[str]] | Omit = omit,
        tag: SequenceNotStr[Optional[str]] | Omit = omit,
        tags: Optional[str] | Omit = omit,
        tenant_id: Optional[str] | Omit = omit,
        trace_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageListResponse:
        """
        Fetch the statuses of messages you've previously sent.

        Args:
          archived: A boolean value that indicates whether archived messages should be included in
              the response.

          cursor: A unique identifier that allows for fetching the next set of messages.

          enqueued_after: The enqueued datetime of a message to filter out messages received before.

          event: A unique identifier representing the event that was used to send the event.

          list: A unique identifier representing the list the message was sent to.

          message_id: A unique identifier representing the message_id returned from either /send or
              /send/list.

          notification: A unique identifier representing the notification that was used to send the
              event.

          provider: The key assocated to the provider you want to filter on. E.g., sendgrid, inbox,
              twilio, slack, msteams, etc. Allows multiple values to be set in query
              parameters.

          recipient: A unique identifier representing the recipient associated with the requested
              profile.

          status: An indicator of the current status of the message. Allows multiple values to be
              set in query parameters.

          tag: A tag placed in the metadata.tags during a notification send. Allows multiple
              values to be set in query parameters.

          tags: A comma delimited list of 'tags'. Messages will be returned if they match any of
              the tags passed in.

          tenant_id: Messages sent with the context of a Tenant

          trace_id: The unique identifier used to trace the requests

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/messages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "cursor": cursor,
                        "enqueued_after": enqueued_after,
                        "event": event,
                        "list": list,
                        "message_id": message_id,
                        "notification": notification,
                        "provider": provider,
                        "recipient": recipient,
                        "status": status,
                        "tag": tag,
                        "tags": tags,
                        "tenant_id": tenant_id,
                        "trace_id": trace_id,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            cast_to=MessageListResponse,
        )

    def cancel(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageDetails:
        """Cancel a message that is currently in the process of being delivered.

        A
        well-formatted API call to the cancel message API will return either `200`
        status code for a successful cancellation or `409` status code for an
        unsuccessful cancellation. Both cases will include the actual message record in
        the response body (see details below).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._post(
            f"/messages/{message_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageDetails,
        )

    def content(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageContentResponse:
        """
        Get message content

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get(
            f"/messages/{message_id}/output",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageContentResponse,
        )

    def history(
        self,
        message_id: str,
        *,
        type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageHistoryResponse:
        """
        Fetch the array of events of a message you've previously sent.

        Args:
          type: A supported Message History type that will filter the events returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get(
            f"/messages/{message_id}/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"type": type}, message_history_params.MessageHistoryParams),
            ),
            cast_to=MessageHistoryResponse,
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageRetrieveResponse:
        """
        Fetch the status of a message you've previously sent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._get(
            f"/messages/{message_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageRetrieveResponse,
        )

    async def list(
        self,
        *,
        archived: Optional[bool] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        enqueued_after: Optional[str] | Omit = omit,
        event: Optional[str] | Omit = omit,
        list: Optional[str] | Omit = omit,
        message_id: Optional[str] | Omit = omit,
        notification: Optional[str] | Omit = omit,
        provider: SequenceNotStr[Optional[str]] | Omit = omit,
        recipient: Optional[str] | Omit = omit,
        status: SequenceNotStr[Optional[str]] | Omit = omit,
        tag: SequenceNotStr[Optional[str]] | Omit = omit,
        tags: Optional[str] | Omit = omit,
        tenant_id: Optional[str] | Omit = omit,
        trace_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageListResponse:
        """
        Fetch the statuses of messages you've previously sent.

        Args:
          archived: A boolean value that indicates whether archived messages should be included in
              the response.

          cursor: A unique identifier that allows for fetching the next set of messages.

          enqueued_after: The enqueued datetime of a message to filter out messages received before.

          event: A unique identifier representing the event that was used to send the event.

          list: A unique identifier representing the list the message was sent to.

          message_id: A unique identifier representing the message_id returned from either /send or
              /send/list.

          notification: A unique identifier representing the notification that was used to send the
              event.

          provider: The key assocated to the provider you want to filter on. E.g., sendgrid, inbox,
              twilio, slack, msteams, etc. Allows multiple values to be set in query
              parameters.

          recipient: A unique identifier representing the recipient associated with the requested
              profile.

          status: An indicator of the current status of the message. Allows multiple values to be
              set in query parameters.

          tag: A tag placed in the metadata.tags during a notification send. Allows multiple
              values to be set in query parameters.

          tags: A comma delimited list of 'tags'. Messages will be returned if they match any of
              the tags passed in.

          tenant_id: Messages sent with the context of a Tenant

          trace_id: The unique identifier used to trace the requests

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/messages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "archived": archived,
                        "cursor": cursor,
                        "enqueued_after": enqueued_after,
                        "event": event,
                        "list": list,
                        "message_id": message_id,
                        "notification": notification,
                        "provider": provider,
                        "recipient": recipient,
                        "status": status,
                        "tag": tag,
                        "tags": tags,
                        "tenant_id": tenant_id,
                        "trace_id": trace_id,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            cast_to=MessageListResponse,
        )

    async def cancel(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageDetails:
        """Cancel a message that is currently in the process of being delivered.

        A
        well-formatted API call to the cancel message API will return either `200`
        status code for a successful cancellation or `409` status code for an
        unsuccessful cancellation. Both cases will include the actual message record in
        the response body (see details below).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._post(
            f"/messages/{message_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageDetails,
        )

    async def content(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageContentResponse:
        """
        Get message content

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._get(
            f"/messages/{message_id}/output",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageContentResponse,
        )

    async def history(
        self,
        message_id: str,
        *,
        type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageHistoryResponse:
        """
        Fetch the array of events of a message you've previously sent.

        Args:
          type: A supported Message History type that will filter the events returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._get(
            f"/messages/{message_id}/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"type": type}, message_history_params.MessageHistoryParams),
            ),
            cast_to=MessageHistoryResponse,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve = to_raw_response_wrapper(
            messages.retrieve,
        )
        self.list = to_raw_response_wrapper(
            messages.list,
        )
        self.cancel = to_raw_response_wrapper(
            messages.cancel,
        )
        self.content = to_raw_response_wrapper(
            messages.content,
        )
        self.history = to_raw_response_wrapper(
            messages.history,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve = async_to_raw_response_wrapper(
            messages.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            messages.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            messages.cancel,
        )
        self.content = async_to_raw_response_wrapper(
            messages.content,
        )
        self.history = async_to_raw_response_wrapper(
            messages.history,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve = to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            messages.list,
        )
        self.cancel = to_streamed_response_wrapper(
            messages.cancel,
        )
        self.content = to_streamed_response_wrapper(
            messages.content,
        )
        self.history = to_streamed_response_wrapper(
            messages.history,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve = async_to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            messages.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            messages.cancel,
        )
        self.content = async_to_streamed_response_wrapper(
            messages.content,
        )
        self.history = async_to_streamed_response_wrapper(
            messages.history,
        )
