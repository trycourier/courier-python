# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import send_message_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.send_message_response import SendMessageResponse

__all__ = ["SendResource", "AsyncSendResource"]


class SendResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SendResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return SendResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SendResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return SendResourceWithStreamingResponse(self)

    def message(
        self,
        *,
        message: send_message_params.Message,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SendMessageResponse:
        """
        Send a message to one or more recipients.

        Args:
          message: The message property has the following primary top-level properties. They define
              the destination and content of the message.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/send",
            body=maybe_transform({"message": message}, send_message_params.SendMessageParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SendMessageResponse,
        )


class AsyncSendResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSendResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSendResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSendResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncSendResourceWithStreamingResponse(self)

    async def message(
        self,
        *,
        message: send_message_params.Message,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SendMessageResponse:
        """
        Send a message to one or more recipients.

        Args:
          message: The message property has the following primary top-level properties. They define
              the destination and content of the message.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/send",
            body=await async_maybe_transform({"message": message}, send_message_params.SendMessageParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SendMessageResponse,
        )


class SendResourceWithRawResponse:
    def __init__(self, send: SendResource) -> None:
        self._send = send

        self.message = to_raw_response_wrapper(
            send.message,
        )


class AsyncSendResourceWithRawResponse:
    def __init__(self, send: AsyncSendResource) -> None:
        self._send = send

        self.message = async_to_raw_response_wrapper(
            send.message,
        )


class SendResourceWithStreamingResponse:
    def __init__(self, send: SendResource) -> None:
        self._send = send

        self.message = to_streamed_response_wrapper(
            send.message,
        )


class AsyncSendResourceWithStreamingResponse:
    def __init__(self, send: AsyncSendResource) -> None:
        self._send = send

        self.message = async_to_streamed_response_wrapper(
            send.message,
        )
