# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .schedules import (
    SchedulesResource,
    AsyncSchedulesResource,
    SchedulesResourceWithRawResponse,
    AsyncSchedulesResourceWithRawResponse,
    SchedulesResourceWithStreamingResponse,
    AsyncSchedulesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["DigestsResource", "AsyncDigestsResource"]


class DigestsResource(SyncAPIResource):
    @cached_property
    def schedules(self) -> SchedulesResource:
        """
        Inspect what has accumulated in a digest schedule and release a digest ahead of its next scheduled delivery.
        """
        return SchedulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DigestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return DigestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DigestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return DigestsResourceWithStreamingResponse(self)


class AsyncDigestsResource(AsyncAPIResource):
    @cached_property
    def schedules(self) -> AsyncSchedulesResource:
        """
        Inspect what has accumulated in a digest schedule and release a digest ahead of its next scheduled delivery.
        """
        return AsyncSchedulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDigestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDigestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDigestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncDigestsResourceWithStreamingResponse(self)


class DigestsResourceWithRawResponse:
    def __init__(self, digests: DigestsResource) -> None:
        self._digests = digests

    @cached_property
    def schedules(self) -> SchedulesResourceWithRawResponse:
        """
        Inspect what has accumulated in a digest schedule and release a digest ahead of its next scheduled delivery.
        """
        return SchedulesResourceWithRawResponse(self._digests.schedules)


class AsyncDigestsResourceWithRawResponse:
    def __init__(self, digests: AsyncDigestsResource) -> None:
        self._digests = digests

    @cached_property
    def schedules(self) -> AsyncSchedulesResourceWithRawResponse:
        """
        Inspect what has accumulated in a digest schedule and release a digest ahead of its next scheduled delivery.
        """
        return AsyncSchedulesResourceWithRawResponse(self._digests.schedules)


class DigestsResourceWithStreamingResponse:
    def __init__(self, digests: DigestsResource) -> None:
        self._digests = digests

    @cached_property
    def schedules(self) -> SchedulesResourceWithStreamingResponse:
        """
        Inspect what has accumulated in a digest schedule and release a digest ahead of its next scheduled delivery.
        """
        return SchedulesResourceWithStreamingResponse(self._digests.schedules)


class AsyncDigestsResourceWithStreamingResponse:
    def __init__(self, digests: AsyncDigestsResource) -> None:
        self._digests = digests

    @cached_property
    def schedules(self) -> AsyncSchedulesResourceWithStreamingResponse:
        """
        Inspect what has accumulated in a digest schedule and release a digest ahead of its next scheduled delivery.
        """
        return AsyncSchedulesResourceWithStreamingResponse(self._digests.schedules)
