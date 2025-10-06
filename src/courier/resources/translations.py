# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import translation_update_params
from .._types import Body, Query, Headers, NoneType, NotGiven, not_given
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

__all__ = ["TranslationsResource", "AsyncTranslationsResource"]


class TranslationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TranslationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return TranslationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TranslationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return TranslationsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        locale: str,
        *,
        domain: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Get translations by locale

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain:
            raise ValueError(f"Expected a non-empty value for `domain` but received {domain!r}")
        if not locale:
            raise ValueError(f"Expected a non-empty value for `locale` but received {locale!r}")
        return self._get(
            f"/translations/{domain}/{locale}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def update(
        self,
        locale: str,
        *,
        domain: str,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update a translation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain:
            raise ValueError(f"Expected a non-empty value for `domain` but received {domain!r}")
        if not locale:
            raise ValueError(f"Expected a non-empty value for `locale` but received {locale!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/translations/{domain}/{locale}",
            body=maybe_transform(body, translation_update_params.TranslationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTranslationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTranslationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTranslationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTranslationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncTranslationsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        locale: str,
        *,
        domain: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Get translations by locale

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain:
            raise ValueError(f"Expected a non-empty value for `domain` but received {domain!r}")
        if not locale:
            raise ValueError(f"Expected a non-empty value for `locale` but received {locale!r}")
        return await self._get(
            f"/translations/{domain}/{locale}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def update(
        self,
        locale: str,
        *,
        domain: str,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update a translation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain:
            raise ValueError(f"Expected a non-empty value for `domain` but received {domain!r}")
        if not locale:
            raise ValueError(f"Expected a non-empty value for `locale` but received {locale!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/translations/{domain}/{locale}",
            body=await async_maybe_transform(body, translation_update_params.TranslationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TranslationsResourceWithRawResponse:
    def __init__(self, translations: TranslationsResource) -> None:
        self._translations = translations

        self.retrieve = to_raw_response_wrapper(
            translations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            translations.update,
        )


class AsyncTranslationsResourceWithRawResponse:
    def __init__(self, translations: AsyncTranslationsResource) -> None:
        self._translations = translations

        self.retrieve = async_to_raw_response_wrapper(
            translations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            translations.update,
        )


class TranslationsResourceWithStreamingResponse:
    def __init__(self, translations: TranslationsResource) -> None:
        self._translations = translations

        self.retrieve = to_streamed_response_wrapper(
            translations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            translations.update,
        )


class AsyncTranslationsResourceWithStreamingResponse:
    def __init__(self, translations: AsyncTranslationsResource) -> None:
        self._translations = translations

        self.retrieve = async_to_streamed_response_wrapper(
            translations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            translations.update,
        )
