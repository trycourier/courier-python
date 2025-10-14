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

__all__ = ["TenantDefaultPreferencesResource", "AsyncTenantDefaultPreferencesResource"]


class TenantDefaultPreferencesResource(SyncAPIResource):
    @cached_property
    def items(self) -> ItemsResource:
        return ItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TenantDefaultPreferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return TenantDefaultPreferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TenantDefaultPreferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return TenantDefaultPreferencesResourceWithStreamingResponse(self)


class AsyncTenantDefaultPreferencesResource(AsyncAPIResource):
    @cached_property
    def items(self) -> AsyncItemsResource:
        return AsyncItemsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTenantDefaultPreferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTenantDefaultPreferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTenantDefaultPreferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncTenantDefaultPreferencesResourceWithStreamingResponse(self)


class TenantDefaultPreferencesResourceWithRawResponse:
    def __init__(self, tenant_default_preferences: TenantDefaultPreferencesResource) -> None:
        self._tenant_default_preferences = tenant_default_preferences

    @cached_property
    def items(self) -> ItemsResourceWithRawResponse:
        return ItemsResourceWithRawResponse(self._tenant_default_preferences.items)


class AsyncTenantDefaultPreferencesResourceWithRawResponse:
    def __init__(self, tenant_default_preferences: AsyncTenantDefaultPreferencesResource) -> None:
        self._tenant_default_preferences = tenant_default_preferences

    @cached_property
    def items(self) -> AsyncItemsResourceWithRawResponse:
        return AsyncItemsResourceWithRawResponse(self._tenant_default_preferences.items)


class TenantDefaultPreferencesResourceWithStreamingResponse:
    def __init__(self, tenant_default_preferences: TenantDefaultPreferencesResource) -> None:
        self._tenant_default_preferences = tenant_default_preferences

    @cached_property
    def items(self) -> ItemsResourceWithStreamingResponse:
        return ItemsResourceWithStreamingResponse(self._tenant_default_preferences.items)


class AsyncTenantDefaultPreferencesResourceWithStreamingResponse:
    def __init__(self, tenant_default_preferences: AsyncTenantDefaultPreferencesResource) -> None:
        self._tenant_default_preferences = tenant_default_preferences

    @cached_property
    def items(self) -> AsyncItemsResourceWithStreamingResponse:
        return AsyncItemsResourceWithStreamingResponse(self._tenant_default_preferences.items)
