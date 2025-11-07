# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.tenants.preferences import item_update_params
from ....types.shared.channel_classification import ChannelClassification

__all__ = ["ItemsResource", "AsyncItemsResource"]


class ItemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return ItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return ItemsResourceWithStreamingResponse(self)

    def update(
        self,
        topic_id: str,
        *,
        tenant_id: str,
        status: Literal["OPTED_OUT", "OPTED_IN", "REQUIRED"],
        custom_routing: Optional[List[ChannelClassification]] | Omit = omit,
        has_custom_routing: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create or Replace Default Preferences For Topic

        Args:
          custom_routing: The default channels to send to this tenant when has_custom_routing is enabled

          has_custom_routing: Override channel routing with custom preferences. This will override any
              template prefernces that are set, but a user can still customize their
              preferences

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        if not topic_id:
            raise ValueError(f"Expected a non-empty value for `topic_id` but received {topic_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/tenants/{tenant_id}/default_preferences/items/{topic_id}",
            body=maybe_transform(
                {
                    "status": status,
                    "custom_routing": custom_routing,
                    "has_custom_routing": has_custom_routing,
                },
                item_update_params.ItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete(
        self,
        topic_id: str,
        *,
        tenant_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove Default Preferences For Topic

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        if not topic_id:
            raise ValueError(f"Expected a non-empty value for `topic_id` but received {topic_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/tenants/{tenant_id}/default_preferences/items/{topic_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncItemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncItemsResourceWithStreamingResponse(self)

    async def update(
        self,
        topic_id: str,
        *,
        tenant_id: str,
        status: Literal["OPTED_OUT", "OPTED_IN", "REQUIRED"],
        custom_routing: Optional[List[ChannelClassification]] | Omit = omit,
        has_custom_routing: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create or Replace Default Preferences For Topic

        Args:
          custom_routing: The default channels to send to this tenant when has_custom_routing is enabled

          has_custom_routing: Override channel routing with custom preferences. This will override any
              template prefernces that are set, but a user can still customize their
              preferences

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        if not topic_id:
            raise ValueError(f"Expected a non-empty value for `topic_id` but received {topic_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/tenants/{tenant_id}/default_preferences/items/{topic_id}",
            body=await async_maybe_transform(
                {
                    "status": status,
                    "custom_routing": custom_routing,
                    "has_custom_routing": has_custom_routing,
                },
                item_update_params.ItemUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete(
        self,
        topic_id: str,
        *,
        tenant_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove Default Preferences For Topic

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        if not topic_id:
            raise ValueError(f"Expected a non-empty value for `topic_id` but received {topic_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/tenants/{tenant_id}/default_preferences/items/{topic_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ItemsResourceWithRawResponse:
    def __init__(self, items: ItemsResource) -> None:
        self._items = items

        self.update = to_raw_response_wrapper(
            items.update,
        )
        self.delete = to_raw_response_wrapper(
            items.delete,
        )


class AsyncItemsResourceWithRawResponse:
    def __init__(self, items: AsyncItemsResource) -> None:
        self._items = items

        self.update = async_to_raw_response_wrapper(
            items.update,
        )
        self.delete = async_to_raw_response_wrapper(
            items.delete,
        )


class ItemsResourceWithStreamingResponse:
    def __init__(self, items: ItemsResource) -> None:
        self._items = items

        self.update = to_streamed_response_wrapper(
            items.update,
        )
        self.delete = to_streamed_response_wrapper(
            items.delete,
        )


class AsyncItemsResourceWithStreamingResponse:
    def __init__(self, items: AsyncItemsResource) -> None:
        self._items = items

        self.update = async_to_streamed_response_wrapper(
            items.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            items.delete,
        )
