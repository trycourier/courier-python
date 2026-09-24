# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import preview_create_device_set_params, preview_update_device_set_params
from .._types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.device_set import DeviceSet
from ..types.device_set_list_response import DeviceSetListResponse
from ..types.preview_device_list_response import PreviewDeviceListResponse

__all__ = ["PreviewsResource", "AsyncPreviewsResource"]


class PreviewsResource(SyncAPIResource):
    """
    Render a template's email content on real email clients and read back the screenshots, so you can check how it looks before you send it.
    """

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

    def archive_device_set(
        self,
        device_set_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceSet:
        """Archive a device set.

        This is a soft delete — the archived set is returned and
        no longer appears in list results. Runs already created against it keep their
        own copy of the device list and are unaffected. The Courier-provided default set
        cannot be archived and returns 409.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_set_id:
            raise ValueError(f"Expected a non-empty value for `device_set_id` but received {device_set_id!r}")
        return self._delete(
            path_template("/previews/device-sets/{device_set_id}", device_set_id=device_set_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceSet,
        )

    def create_device_set(
        self,
        *,
        device_ids: SequenceNotStr[str],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceSet:
        """Create a named, reusable set of preview devices.

        Every id must be one listed by
        `GET /previews/devices`; any other is a 422.

        Args:
          device_ids: The devices the set contains, by `PreviewDevice.id`. At least one is required.

          name: Human-readable name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/previews/device-sets",
            body=maybe_transform(
                {
                    "device_ids": device_ids,
                    "name": name,
                },
                preview_create_device_set_params.PreviewCreateDeviceSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceSet,
        )

    def list_device_sets(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceSetListResponse:
        """List the workspace's preview sets. Archived sets are not returned."""
        return self._get(
            "/previews/device-sets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceSetListResponse,
        )

    def list_devices(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreviewDeviceListResponse:
        """List the devices a preview can be rendered on.

        Reference data, identical for
        every workspace — these ids are what a device set is built from and what a run
        reports results for.
        """
        return self._get(
            "/previews/devices",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreviewDeviceListResponse,
        )

    def retrieve_device_set(
        self,
        device_set_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceSet:
        """Retrieve a preview set by ID.

        Archived sets return 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_set_id:
            raise ValueError(f"Expected a non-empty value for `device_set_id` but received {device_set_id!r}")
        return self._get(
            path_template("/previews/device-sets/{device_set_id}", device_set_id=device_set_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceSet,
        )

    def update_device_set(
        self,
        device_set_id: str,
        *,
        device_ids: SequenceNotStr[str],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceSet:
        """Replace a device set.

        This is a full replace, not a patch — both the name and
        the device list are always written. The Courier-provided default set cannot be
        changed and returns 409.

        Args:
          device_ids: The devices the set contains, by `PreviewDevice.id`. At least one is required.

          name: Human-readable name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_set_id:
            raise ValueError(f"Expected a non-empty value for `device_set_id` but received {device_set_id!r}")
        return self._put(
            path_template("/previews/device-sets/{device_set_id}", device_set_id=device_set_id),
            body=maybe_transform(
                {
                    "device_ids": device_ids,
                    "name": name,
                },
                preview_update_device_set_params.PreviewUpdateDeviceSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceSet,
        )


class AsyncPreviewsResource(AsyncAPIResource):
    """
    Render a template's email content on real email clients and read back the screenshots, so you can check how it looks before you send it.
    """

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

    async def archive_device_set(
        self,
        device_set_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceSet:
        """Archive a device set.

        This is a soft delete — the archived set is returned and
        no longer appears in list results. Runs already created against it keep their
        own copy of the device list and are unaffected. The Courier-provided default set
        cannot be archived and returns 409.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_set_id:
            raise ValueError(f"Expected a non-empty value for `device_set_id` but received {device_set_id!r}")
        return await self._delete(
            path_template("/previews/device-sets/{device_set_id}", device_set_id=device_set_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceSet,
        )

    async def create_device_set(
        self,
        *,
        device_ids: SequenceNotStr[str],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceSet:
        """Create a named, reusable set of preview devices.

        Every id must be one listed by
        `GET /previews/devices`; any other is a 422.

        Args:
          device_ids: The devices the set contains, by `PreviewDevice.id`. At least one is required.

          name: Human-readable name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/previews/device-sets",
            body=await async_maybe_transform(
                {
                    "device_ids": device_ids,
                    "name": name,
                },
                preview_create_device_set_params.PreviewCreateDeviceSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceSet,
        )

    async def list_device_sets(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceSetListResponse:
        """List the workspace's preview sets. Archived sets are not returned."""
        return await self._get(
            "/previews/device-sets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceSetListResponse,
        )

    async def list_devices(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreviewDeviceListResponse:
        """List the devices a preview can be rendered on.

        Reference data, identical for
        every workspace — these ids are what a device set is built from and what a run
        reports results for.
        """
        return await self._get(
            "/previews/devices",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreviewDeviceListResponse,
        )

    async def retrieve_device_set(
        self,
        device_set_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceSet:
        """Retrieve a preview set by ID.

        Archived sets return 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_set_id:
            raise ValueError(f"Expected a non-empty value for `device_set_id` but received {device_set_id!r}")
        return await self._get(
            path_template("/previews/device-sets/{device_set_id}", device_set_id=device_set_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceSet,
        )

    async def update_device_set(
        self,
        device_set_id: str,
        *,
        device_ids: SequenceNotStr[str],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceSet:
        """Replace a device set.

        This is a full replace, not a patch — both the name and
        the device list are always written. The Courier-provided default set cannot be
        changed and returns 409.

        Args:
          device_ids: The devices the set contains, by `PreviewDevice.id`. At least one is required.

          name: Human-readable name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_set_id:
            raise ValueError(f"Expected a non-empty value for `device_set_id` but received {device_set_id!r}")
        return await self._put(
            path_template("/previews/device-sets/{device_set_id}", device_set_id=device_set_id),
            body=await async_maybe_transform(
                {
                    "device_ids": device_ids,
                    "name": name,
                },
                preview_update_device_set_params.PreviewUpdateDeviceSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceSet,
        )


class PreviewsResourceWithRawResponse:
    def __init__(self, previews: PreviewsResource) -> None:
        self._previews = previews

        self.archive_device_set = to_raw_response_wrapper(
            previews.archive_device_set,
        )
        self.create_device_set = to_raw_response_wrapper(
            previews.create_device_set,
        )
        self.list_device_sets = to_raw_response_wrapper(
            previews.list_device_sets,
        )
        self.list_devices = to_raw_response_wrapper(
            previews.list_devices,
        )
        self.retrieve_device_set = to_raw_response_wrapper(
            previews.retrieve_device_set,
        )
        self.update_device_set = to_raw_response_wrapper(
            previews.update_device_set,
        )


class AsyncPreviewsResourceWithRawResponse:
    def __init__(self, previews: AsyncPreviewsResource) -> None:
        self._previews = previews

        self.archive_device_set = async_to_raw_response_wrapper(
            previews.archive_device_set,
        )
        self.create_device_set = async_to_raw_response_wrapper(
            previews.create_device_set,
        )
        self.list_device_sets = async_to_raw_response_wrapper(
            previews.list_device_sets,
        )
        self.list_devices = async_to_raw_response_wrapper(
            previews.list_devices,
        )
        self.retrieve_device_set = async_to_raw_response_wrapper(
            previews.retrieve_device_set,
        )
        self.update_device_set = async_to_raw_response_wrapper(
            previews.update_device_set,
        )


class PreviewsResourceWithStreamingResponse:
    def __init__(self, previews: PreviewsResource) -> None:
        self._previews = previews

        self.archive_device_set = to_streamed_response_wrapper(
            previews.archive_device_set,
        )
        self.create_device_set = to_streamed_response_wrapper(
            previews.create_device_set,
        )
        self.list_device_sets = to_streamed_response_wrapper(
            previews.list_device_sets,
        )
        self.list_devices = to_streamed_response_wrapper(
            previews.list_devices,
        )
        self.retrieve_device_set = to_streamed_response_wrapper(
            previews.retrieve_device_set,
        )
        self.update_device_set = to_streamed_response_wrapper(
            previews.update_device_set,
        )


class AsyncPreviewsResourceWithStreamingResponse:
    def __init__(self, previews: AsyncPreviewsResource) -> None:
        self._previews = previews

        self.archive_device_set = async_to_streamed_response_wrapper(
            previews.archive_device_set,
        )
        self.create_device_set = async_to_streamed_response_wrapper(
            previews.create_device_set,
        )
        self.list_device_sets = async_to_streamed_response_wrapper(
            previews.list_device_sets,
        )
        self.list_devices = async_to_streamed_response_wrapper(
            previews.list_devices,
        )
        self.retrieve_device_set = async_to_streamed_response_wrapper(
            previews.retrieve_device_set,
        )
        self.update_device_set = async_to_streamed_response_wrapper(
            previews.update_device_set,
        )
