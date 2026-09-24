# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .runs import (
    RunsResource,
    AsyncRunsResource,
    RunsResourceWithRawResponse,
    AsyncRunsResourceWithRawResponse,
    RunsResourceWithStreamingResponse,
    AsyncRunsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["PreviewsResource", "AsyncPreviewsResource"]


class PreviewsResource(SyncAPIResource):
    @cached_property
    def runs(self) -> RunsResource:
        """
        Render a template's email content on real email clients and read back the screenshots, so you can check how it looks before you send it.
        """
        return RunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PreviewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return PreviewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PreviewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return PreviewsResourceWithStreamingResponse(self)


class AsyncPreviewsResource(AsyncAPIResource):
    @cached_property
    def runs(self) -> AsyncRunsResource:
        """
        Render a template's email content on real email clients and read back the screenshots, so you can check how it looks before you send it.
        """
        return AsyncRunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPreviewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPreviewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPreviewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncPreviewsResourceWithStreamingResponse(self)


class PreviewsResourceWithRawResponse:
    def __init__(self, previews: PreviewsResource) -> None:
        self._previews = previews

    @cached_property
    def runs(self) -> RunsResourceWithRawResponse:
        """
        Render a template's email content on real email clients and read back the screenshots, so you can check how it looks before you send it.
        """
        return RunsResourceWithRawResponse(self._previews.runs)


class AsyncPreviewsResourceWithRawResponse:
    def __init__(self, previews: AsyncPreviewsResource) -> None:
        self._previews = previews

    @cached_property
    def runs(self) -> AsyncRunsResourceWithRawResponse:
        """
        Render a template's email content on real email clients and read back the screenshots, so you can check how it looks before you send it.
        """
        return AsyncRunsResourceWithRawResponse(self._previews.runs)


class PreviewsResourceWithStreamingResponse:
    def __init__(self, previews: PreviewsResource) -> None:
        self._previews = previews

    @cached_property
    def runs(self) -> RunsResourceWithStreamingResponse:
        """
        Render a template's email content on real email clients and read back the screenshots, so you can check how it looks before you send it.
        """
        return RunsResourceWithStreamingResponse(self._previews.runs)


class AsyncPreviewsResourceWithStreamingResponse:
    def __init__(self, previews: AsyncPreviewsResource) -> None:
        self._previews = previews

    @cached_property
    def runs(self) -> AsyncRunsResourceWithStreamingResponse:
        """
        Render a template's email content on real email clients and read back the screenshots, so you can check how it looks before you send it.
        """
        return AsyncRunsResourceWithStreamingResponse(self._previews.runs)
