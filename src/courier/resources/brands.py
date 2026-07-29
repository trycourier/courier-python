# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import brand_list_params, brand_create_params, brand_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.brand import Brand
from .._base_client import make_request_options
from ..types.brand_list_response import BrandListResponse
from ..types.brand_settings_param import BrandSettingsParam
from ..types.brand_snippets_param import BrandSnippetsParam

__all__ = ["BrandsResource", "AsyncBrandsResource"]


class BrandsResource(SyncAPIResource):
    """
    Manage the logos, colors, and layout that give the templates you send a consistent look.
    """

    @cached_property
    def with_raw_response(self) -> BrandsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return BrandsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrandsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return BrandsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        settings: BrandSettingsParam,
        id: Optional[str] | Omit = omit,
        snippets: Optional[BrandSnippetsParam] | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_idempotency_expiration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Brand:
        """Creates a brand from a name and settings, including primary and secondary
        colors.

        Brands supply the logo, colors, and styling that templates render with.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Idempotency-Key": idempotency_key,
                    "x-idempotency-expiration": x_idempotency_expiration,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/brands",
            body=maybe_transform(
                {
                    "name": name,
                    "settings": settings,
                    "id": id,
                    "snippets": snippets,
                },
                brand_create_params.BrandCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Brand,
        )

    def retrieve(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Brand:
        """
        Returns one brand by id, including its colors, logo and styling settings,
        Handlebars snippets, and published version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return self._get(
            path_template("/brands/{brand_id}", brand_id=brand_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Brand,
        )

    def update(
        self,
        brand_id: str,
        *,
        name: str,
        settings: Optional[BrandSettingsParam] | Omit = omit,
        snippets: Optional[BrandSnippetsParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Brand:
        """
        Replaces a brand with the values you supply, so send the complete settings and
        snippets rather than only the fields you want changed.

        Args:
          name: The name of the brand.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return self._put(
            path_template("/brands/{brand_id}", brand_id=brand_id),
            body=maybe_transform(
                {
                    "name": name,
                    "settings": settings,
                    "snippets": snippets,
                },
                brand_update_params.BrandUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Brand,
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
    ) -> BrandListResponse:
        """Lists the workspace's brands.

        Every entry carries its name, styling settings,
        snippets, and published version.

        Args:
          cursor: A unique identifier that allows for fetching the next set of brands.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/brands",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cursor": cursor}, brand_list_params.BrandListParams),
            ),
            cast_to=BrandListResponse,
        )

    def delete(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deletes a brand by id.

        Reassign any template or tenant that references it before
        deleting to keep their styling intact.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/brands/{brand_id}", brand_id=brand_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncBrandsResource(AsyncAPIResource):
    """
    Manage the logos, colors, and layout that give the templates you send a consistent look.
    """

    @cached_property
    def with_raw_response(self) -> AsyncBrandsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBrandsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrandsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncBrandsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        settings: BrandSettingsParam,
        id: Optional[str] | Omit = omit,
        snippets: Optional[BrandSnippetsParam] | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_idempotency_expiration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Brand:
        """Creates a brand from a name and settings, including primary and secondary
        colors.

        Brands supply the logo, colors, and styling that templates render with.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Idempotency-Key": idempotency_key,
                    "x-idempotency-expiration": x_idempotency_expiration,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/brands",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "settings": settings,
                    "id": id,
                    "snippets": snippets,
                },
                brand_create_params.BrandCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Brand,
        )

    async def retrieve(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Brand:
        """
        Returns one brand by id, including its colors, logo and styling settings,
        Handlebars snippets, and published version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return await self._get(
            path_template("/brands/{brand_id}", brand_id=brand_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Brand,
        )

    async def update(
        self,
        brand_id: str,
        *,
        name: str,
        settings: Optional[BrandSettingsParam] | Omit = omit,
        snippets: Optional[BrandSnippetsParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Brand:
        """
        Replaces a brand with the values you supply, so send the complete settings and
        snippets rather than only the fields you want changed.

        Args:
          name: The name of the brand.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return await self._put(
            path_template("/brands/{brand_id}", brand_id=brand_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "settings": settings,
                    "snippets": snippets,
                },
                brand_update_params.BrandUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Brand,
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
    ) -> BrandListResponse:
        """Lists the workspace's brands.

        Every entry carries its name, styling settings,
        snippets, and published version.

        Args:
          cursor: A unique identifier that allows for fetching the next set of brands.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/brands",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"cursor": cursor}, brand_list_params.BrandListParams),
            ),
            cast_to=BrandListResponse,
        )

    async def delete(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deletes a brand by id.

        Reassign any template or tenant that references it before
        deleting to keep their styling intact.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/brands/{brand_id}", brand_id=brand_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class BrandsResourceWithRawResponse:
    def __init__(self, brands: BrandsResource) -> None:
        self._brands = brands

        self.create = to_raw_response_wrapper(
            brands.create,
        )
        self.retrieve = to_raw_response_wrapper(
            brands.retrieve,
        )
        self.update = to_raw_response_wrapper(
            brands.update,
        )
        self.list = to_raw_response_wrapper(
            brands.list,
        )
        self.delete = to_raw_response_wrapper(
            brands.delete,
        )


class AsyncBrandsResourceWithRawResponse:
    def __init__(self, brands: AsyncBrandsResource) -> None:
        self._brands = brands

        self.create = async_to_raw_response_wrapper(
            brands.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            brands.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            brands.update,
        )
        self.list = async_to_raw_response_wrapper(
            brands.list,
        )
        self.delete = async_to_raw_response_wrapper(
            brands.delete,
        )


class BrandsResourceWithStreamingResponse:
    def __init__(self, brands: BrandsResource) -> None:
        self._brands = brands

        self.create = to_streamed_response_wrapper(
            brands.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            brands.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            brands.update,
        )
        self.list = to_streamed_response_wrapper(
            brands.list,
        )
        self.delete = to_streamed_response_wrapper(
            brands.delete,
        )


class AsyncBrandsResourceWithStreamingResponse:
    def __init__(self, brands: AsyncBrandsResource) -> None:
        self._brands = brands

        self.create = async_to_streamed_response_wrapper(
            brands.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            brands.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            brands.update,
        )
        self.list = async_to_streamed_response_wrapper(
            brands.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            brands.delete,
        )
