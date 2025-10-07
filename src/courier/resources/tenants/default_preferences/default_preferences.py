# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .items import (
    ItemsResource,
    AsyncItemsResource,
    ItemsResourceWithRawResponse,
    AsyncItemsResourceWithRawResponse,
    ItemsResourceWithStreamingResponse,
    AsyncItemsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["DefaultPreferencesResource", "AsyncDefaultPreferencesResource"]


class DefaultPreferencesResource(SyncAPIResource):
    @cached_property
    def items(self) -> ItemsResource:
        return ItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DefaultPreferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return DefaultPreferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DefaultPreferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return DefaultPreferencesResourceWithStreamingResponse(self)


class AsyncDefaultPreferencesResource(AsyncAPIResource):
    @cached_property
    def items(self) -> AsyncItemsResource:
        return AsyncItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDefaultPreferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDefaultPreferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDefaultPreferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncDefaultPreferencesResourceWithStreamingResponse(self)


class DefaultPreferencesResourceWithRawResponse:
    def __init__(self, default_preferences: DefaultPreferencesResource) -> None:
        self._default_preferences = default_preferences

    @cached_property
    def items(self) -> ItemsResourceWithRawResponse:
        return ItemsResourceWithRawResponse(self._default_preferences.items)


class AsyncDefaultPreferencesResourceWithRawResponse:
    def __init__(self, default_preferences: AsyncDefaultPreferencesResource) -> None:
        self._default_preferences = default_preferences

    @cached_property
    def items(self) -> AsyncItemsResourceWithRawResponse:
        return AsyncItemsResourceWithRawResponse(self._default_preferences.items)


class DefaultPreferencesResourceWithStreamingResponse:
    def __init__(self, default_preferences: DefaultPreferencesResource) -> None:
        self._default_preferences = default_preferences

    @cached_property
    def items(self) -> ItemsResourceWithStreamingResponse:
        return ItemsResourceWithStreamingResponse(self._default_preferences.items)


class AsyncDefaultPreferencesResourceWithStreamingResponse:
    def __init__(self, default_preferences: AsyncDefaultPreferencesResource) -> None:
        self._default_preferences = default_preferences

    @cached_property
    def items(self) -> AsyncItemsResourceWithStreamingResponse:
        return AsyncItemsResourceWithStreamingResponse(self._default_preferences.items)
