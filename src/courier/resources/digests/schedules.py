# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.digests import schedule_list_instances_params
from ...types.digest_instance_list_response import DigestInstanceListResponse

__all__ = ["SchedulesResource", "AsyncSchedulesResource"]


class SchedulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SchedulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return SchedulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchedulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return SchedulesResourceWithStreamingResponse(self)

    def list_instances(
        self,
        schedule_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DigestInstanceListResponse:
        """List the digest instances for a schedule.

        Each instance represents the events
        accumulated for a single user against the schedule, and can be used to monitor
        digest accumulation before the digest is released.

        Args:
          cursor: A cursor token from a previous response, used to fetch the next page of results.

          limit: The maximum number of digest instances to return. Defaults to 20, with a maximum
              of 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return self._get(
            path_template("/digests/schedules/{schedule_id}/instances", schedule_id=schedule_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    schedule_list_instances_params.ScheduleListInstancesParams,
                ),
            ),
            cast_to=DigestInstanceListResponse,
        )

    def release(
        self,
        schedule_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Send a digest now instead of waiting for its scheduled time, so your users get
        what they have collected so far right away.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/digests/schedules/{schedule_id}/trigger", schedule_id=schedule_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSchedulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSchedulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSchedulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchedulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncSchedulesResourceWithStreamingResponse(self)

    async def list_instances(
        self,
        schedule_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DigestInstanceListResponse:
        """List the digest instances for a schedule.

        Each instance represents the events
        accumulated for a single user against the schedule, and can be used to monitor
        digest accumulation before the digest is released.

        Args:
          cursor: A cursor token from a previous response, used to fetch the next page of results.

          limit: The maximum number of digest instances to return. Defaults to 20, with a maximum
              of 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        return await self._get(
            path_template("/digests/schedules/{schedule_id}/instances", schedule_id=schedule_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    schedule_list_instances_params.ScheduleListInstancesParams,
                ),
            ),
            cast_to=DigestInstanceListResponse,
        )

    async def release(
        self,
        schedule_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Send a digest now instead of waiting for its scheduled time, so your users get
        what they have collected so far right away.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not schedule_id:
            raise ValueError(f"Expected a non-empty value for `schedule_id` but received {schedule_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/digests/schedules/{schedule_id}/trigger", schedule_id=schedule_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SchedulesResourceWithRawResponse:
    def __init__(self, schedules: SchedulesResource) -> None:
        self._schedules = schedules

        self.list_instances = to_raw_response_wrapper(
            schedules.list_instances,
        )
        self.release = to_raw_response_wrapper(
            schedules.release,
        )


class AsyncSchedulesResourceWithRawResponse:
    def __init__(self, schedules: AsyncSchedulesResource) -> None:
        self._schedules = schedules

        self.list_instances = async_to_raw_response_wrapper(
            schedules.list_instances,
        )
        self.release = async_to_raw_response_wrapper(
            schedules.release,
        )


class SchedulesResourceWithStreamingResponse:
    def __init__(self, schedules: SchedulesResource) -> None:
        self._schedules = schedules

        self.list_instances = to_streamed_response_wrapper(
            schedules.list_instances,
        )
        self.release = to_streamed_response_wrapper(
            schedules.release,
        )


class AsyncSchedulesResourceWithStreamingResponse:
    def __init__(self, schedules: AsyncSchedulesResource) -> None:
        self._schedules = schedules

        self.list_instances = async_to_streamed_response_wrapper(
            schedules.list_instances,
        )
        self.release = async_to_streamed_response_wrapper(
            schedules.release,
        )
