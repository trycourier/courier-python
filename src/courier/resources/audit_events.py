# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import audit_event_list_params
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
from ..types.audit_event import AuditEvent
from ..types.audit_event_list_response import AuditEventListResponse

__all__ = ["AuditEventsResource", "AsyncAuditEventsResource"]


class AuditEventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuditEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AuditEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuditEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AuditEventsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        audit_event_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuditEvent:
        """
        Fetch a specific audit event by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audit_event_id:
            raise ValueError(f"Expected a non-empty value for `audit_event_id` but received {audit_event_id!r}")
        return self._get(
            f"/audit-events/{audit_event_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuditEvent,
        )

    def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuditEventListResponse:
        """
        Fetch the list of audit events

        Args:
          cursor: A unique identifier that allows for fetching the next set of audit events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/audit-events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cursor": cursor}, audit_event_list_params.AuditEventListParams),
            ),
            cast_to=AuditEventListResponse,
        )


class AsyncAuditEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuditEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuditEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuditEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncAuditEventsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        audit_event_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuditEvent:
        """
        Fetch a specific audit event by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audit_event_id:
            raise ValueError(f"Expected a non-empty value for `audit_event_id` but received {audit_event_id!r}")
        return await self._get(
            f"/audit-events/{audit_event_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuditEvent,
        )

    async def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuditEventListResponse:
        """
        Fetch the list of audit events

        Args:
          cursor: A unique identifier that allows for fetching the next set of audit events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/audit-events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"cursor": cursor}, audit_event_list_params.AuditEventListParams),
            ),
            cast_to=AuditEventListResponse,
        )


class AuditEventsResourceWithRawResponse:
    def __init__(self, audit_events: AuditEventsResource) -> None:
        self._audit_events = audit_events

        self.retrieve = to_raw_response_wrapper(
            audit_events.retrieve,
        )
        self.list = to_raw_response_wrapper(
            audit_events.list,
        )


class AsyncAuditEventsResourceWithRawResponse:
    def __init__(self, audit_events: AsyncAuditEventsResource) -> None:
        self._audit_events = audit_events

        self.retrieve = async_to_raw_response_wrapper(
            audit_events.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            audit_events.list,
        )


class AuditEventsResourceWithStreamingResponse:
    def __init__(self, audit_events: AuditEventsResource) -> None:
        self._audit_events = audit_events

        self.retrieve = to_streamed_response_wrapper(
            audit_events.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            audit_events.list,
        )


class AsyncAuditEventsResourceWithStreamingResponse:
    def __init__(self, audit_events: AsyncAuditEventsResource) -> None:
        self._audit_events = audit_events

        self.retrieve = async_to_streamed_response_wrapper(
            audit_events.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            audit_events.list,
        )
