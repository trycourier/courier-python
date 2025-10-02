# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ..types import inbound_track_event_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.inbound_track_event_response import InboundTrackEventResponse

__all__ = ["InboundResource", "AsyncInboundResource"]


class InboundResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboundResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return InboundResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboundResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return InboundResourceWithStreamingResponse(self)

    def track_event(
        self,
        *,
        event: str,
        message_id: str,
        properties: Dict[str, object],
        type: Literal["track"],
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InboundTrackEventResponse:
        """Courier Track Event

        Args:
          event: A descriptive name of the event.

        This name will appear as a trigger in the
              Courier Automation Trigger node.

          message_id: A required unique identifier that will be used to de-duplicate requests. If not
              unique, will respond with 409 Conflict status

          user_id: The user id associatiated with the track

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/inbound/courier",
            body=maybe_transform(
                {
                    "event": event,
                    "message_id": message_id,
                    "properties": properties,
                    "type": type,
                    "user_id": user_id,
                },
                inbound_track_event_params.InboundTrackEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundTrackEventResponse,
        )


class AsyncInboundResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboundResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInboundResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboundResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncInboundResourceWithStreamingResponse(self)

    async def track_event(
        self,
        *,
        event: str,
        message_id: str,
        properties: Dict[str, object],
        type: Literal["track"],
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InboundTrackEventResponse:
        """Courier Track Event

        Args:
          event: A descriptive name of the event.

        This name will appear as a trigger in the
              Courier Automation Trigger node.

          message_id: A required unique identifier that will be used to de-duplicate requests. If not
              unique, will respond with 409 Conflict status

          user_id: The user id associatiated with the track

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/inbound/courier",
            body=await async_maybe_transform(
                {
                    "event": event,
                    "message_id": message_id,
                    "properties": properties,
                    "type": type,
                    "user_id": user_id,
                },
                inbound_track_event_params.InboundTrackEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundTrackEventResponse,
        )


class InboundResourceWithRawResponse:
    def __init__(self, inbound: InboundResource) -> None:
        self._inbound = inbound

        self.track_event = to_raw_response_wrapper(
            inbound.track_event,
        )


class AsyncInboundResourceWithRawResponse:
    def __init__(self, inbound: AsyncInboundResource) -> None:
        self._inbound = inbound

        self.track_event = async_to_raw_response_wrapper(
            inbound.track_event,
        )


class InboundResourceWithStreamingResponse:
    def __init__(self, inbound: InboundResource) -> None:
        self._inbound = inbound

        self.track_event = to_streamed_response_wrapper(
            inbound.track_event,
        )


class AsyncInboundResourceWithStreamingResponse:
    def __init__(self, inbound: AsyncInboundResource) -> None:
        self._inbound = inbound

        self.track_event = async_to_streamed_response_wrapper(
            inbound.track_event,
        )
