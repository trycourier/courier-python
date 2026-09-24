# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.notifications.previews import run_list_params, run_create_params
from ....types.notifications.previews.preview_run import PreviewRun
from ....types.notifications.previews.preview_run_detail import PreviewRunDetail
from ....types.notifications.previews.preview_run_list_response import PreviewRunListResponse

__all__ = ["RunsResource", "AsyncRunsResource"]


class RunsResource(SyncAPIResource):
    """
    Render a template's email content on real email clients and read back the screenshots, so you can check how it looks before you send it.
    """

    @cached_property
    def with_raw_response(self) -> RunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return RunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return RunsResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        data: Dict[str, object] | Omit = omit,
        device_ids: SequenceNotStr[str] | Omit = omit,
        device_set_id: str | Omit = omit,
        locale: str | Omit = omit,
        template_version: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_idempotency_expiration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreviewRun:
        """
        Render this template's email content on each of the requested devices.

        Returns as soon as the run exists and its render is queued — the screenshots are
        produced asynchronously. Poll
        `GET /notifications/{id}/previews/runs/{previewRunId}` until every result
        reaches a terminal status.

        Name the devices either with `device_set_id`, for a saved set, or with
        `device_ids`, for a one-off list. Exactly one of the two is required. Inline
        `device_ids` must be ids listed by `GET /previews/devices`; any other id is a
        422, refused before the run exists or is billed.

        A template that does not exist is a 404. One that exists but cannot be previewed
        — not a Design Studio template, no email channel, or no such `template_version`
        — is a 422, also refused before the run exists or is billed.

        Preview runs are a metered add-on. A workspace without it, or with its billing
        suspended, receives a 402.

        Args:
          data: Template variables to render with, the same shape as the `data` object on a
              send.

          device_ids: The devices to render on, by `PreviewDevice.id`, for a one-off run. Mutually
              exclusive with `device_set_id`.

          device_set_id: A saved device set naming the devices to render on. Mutually exclusive with
              `device_ids`.

          locale: Render the template's content for this locale, e.g. "fr-FR".

          template_version: Which version of the template to render. Omit for the latest saved draft, which
              always exists and is what the editor shows. `published` renders the live
              version; a zero-padded `v002` renders that specific publish. Versions are
              1-based, so `v000` is not a version, and the unpadded `v2` is rejected — that
              spelling belongs to journeys' AutomationVersionId, a different scheme in which
              `v0` means published.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
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
            path_template("/notifications/{id}/previews/runs", id=id),
            body=maybe_transform(
                {
                    "data": data,
                    "device_ids": device_ids,
                    "device_set_id": device_set_id,
                    "locale": locale,
                    "template_version": template_version,
                },
                run_create_params.RunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreviewRun,
        )

    def retrieve(
        self,
        preview_run_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreviewRunDetail:
        """
        Retrieve one of this template's preview runs together with its per-device
        results.

        A run is only readable under the template it previewed: under any other template
        it is a 404, the same as a run that does not exist.

        `thumbnail_url` and `screenshot_url` are short-lived signed URLs, re-signed on
        every read. Fetch them now rather than storing them. Both are null until
        Courier's own copy of the image exists, which is what `status: COMPLETED` on a
        result means.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not preview_run_id:
            raise ValueError(f"Expected a non-empty value for `preview_run_id` but received {preview_run_id!r}")
        return self._get(
            path_template("/notifications/{id}/previews/runs/{preview_run_id}", id=id, preview_run_id=preview_run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreviewRunDetail,
        )

    def list(
        self,
        id: str,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreviewRunListResponse:
        """List this template's preview runs, newest first.

        Cursor-paginated.

        A template that does not exist is a 404, the same as every other
        `/notifications/{id}` route.

        Args:
          cursor: Opaque pagination cursor from a previous response. Omit for the first page.

          limit: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/notifications/{id}/previews/runs", id=id),
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
                    run_list_params.RunListParams,
                ),
            ),
            cast_to=PreviewRunListResponse,
        )


class AsyncRunsResource(AsyncAPIResource):
    """
    Render a template's email content on real email clients and read back the screenshots, so you can check how it looks before you send it.
    """

    @cached_property
    def with_raw_response(self) -> AsyncRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncRunsResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        data: Dict[str, object] | Omit = omit,
        device_ids: SequenceNotStr[str] | Omit = omit,
        device_set_id: str | Omit = omit,
        locale: str | Omit = omit,
        template_version: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_idempotency_expiration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreviewRun:
        """
        Render this template's email content on each of the requested devices.

        Returns as soon as the run exists and its render is queued — the screenshots are
        produced asynchronously. Poll
        `GET /notifications/{id}/previews/runs/{previewRunId}` until every result
        reaches a terminal status.

        Name the devices either with `device_set_id`, for a saved set, or with
        `device_ids`, for a one-off list. Exactly one of the two is required. Inline
        `device_ids` must be ids listed by `GET /previews/devices`; any other id is a
        422, refused before the run exists or is billed.

        A template that does not exist is a 404. One that exists but cannot be previewed
        — not a Design Studio template, no email channel, or no such `template_version`
        — is a 422, also refused before the run exists or is billed.

        Preview runs are a metered add-on. A workspace without it, or with its billing
        suspended, receives a 402.

        Args:
          data: Template variables to render with, the same shape as the `data` object on a
              send.

          device_ids: The devices to render on, by `PreviewDevice.id`, for a one-off run. Mutually
              exclusive with `device_set_id`.

          device_set_id: A saved device set naming the devices to render on. Mutually exclusive with
              `device_ids`.

          locale: Render the template's content for this locale, e.g. "fr-FR".

          template_version: Which version of the template to render. Omit for the latest saved draft, which
              always exists and is what the editor shows. `published` renders the live
              version; a zero-padded `v002` renders that specific publish. Versions are
              1-based, so `v000` is not a version, and the unpadded `v2` is rejected — that
              spelling belongs to journeys' AutomationVersionId, a different scheme in which
              `v0` means published.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
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
            path_template("/notifications/{id}/previews/runs", id=id),
            body=await async_maybe_transform(
                {
                    "data": data,
                    "device_ids": device_ids,
                    "device_set_id": device_set_id,
                    "locale": locale,
                    "template_version": template_version,
                },
                run_create_params.RunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreviewRun,
        )

    async def retrieve(
        self,
        preview_run_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreviewRunDetail:
        """
        Retrieve one of this template's preview runs together with its per-device
        results.

        A run is only readable under the template it previewed: under any other template
        it is a 404, the same as a run that does not exist.

        `thumbnail_url` and `screenshot_url` are short-lived signed URLs, re-signed on
        every read. Fetch them now rather than storing them. Both are null until
        Courier's own copy of the image exists, which is what `status: COMPLETED` on a
        result means.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not preview_run_id:
            raise ValueError(f"Expected a non-empty value for `preview_run_id` but received {preview_run_id!r}")
        return await self._get(
            path_template("/notifications/{id}/previews/runs/{preview_run_id}", id=id, preview_run_id=preview_run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreviewRunDetail,
        )

    async def list(
        self,
        id: str,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreviewRunListResponse:
        """List this template's preview runs, newest first.

        Cursor-paginated.

        A template that does not exist is a 404, the same as every other
        `/notifications/{id}` route.

        Args:
          cursor: Opaque pagination cursor from a previous response. Omit for the first page.

          limit: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/notifications/{id}/previews/runs", id=id),
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
                    run_list_params.RunListParams,
                ),
            ),
            cast_to=PreviewRunListResponse,
        )


class RunsResourceWithRawResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.create = to_raw_response_wrapper(
            runs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            runs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            runs.list,
        )


class AsyncRunsResourceWithRawResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.create = async_to_raw_response_wrapper(
            runs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            runs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            runs.list,
        )


class RunsResourceWithStreamingResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.create = to_streamed_response_wrapper(
            runs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            runs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            runs.list,
        )


class AsyncRunsResourceWithStreamingResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.create = async_to_streamed_response_wrapper(
            runs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            runs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            runs.list,
        )
