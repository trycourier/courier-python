# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.automations import run_list_params
from ...types.automation_run_list_response import AutomationRunListResponse
from ...types.automation_run_steps_response import AutomationRunStepsResponse

__all__ = ["RunsResource", "AsyncRunsResource"]


class RunsResource(SyncAPIResource):
    """
    Invoke a stored automation template or an ad hoc automation defined in the request.
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

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        end_date: str | Omit = omit,
        limit: str | Omit = omit,
        start_date: str | Omit = omit,
        status: str | Omit = omit,
        template_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutomationRunListResponse:
        """
        List runs of the workspace's v2 Automations, newest first, filtered by status,
        Template, or date range and paged by cursor. Journey (v3) runs are listed by
        `GET /journeys/runs` instead — the two surfaces never return each other's runs.
        Runs are retained for 95 days.

        Args:
          cursor: A cursor token for pagination. Use the `next_cursor` from the previous response
              to fetch the next page of results. Treat it as opaque.

          end_date: An inclusive upper bound on `created_at`, in the same format as `start_date`.

          limit: The number of runs to return per page, between `1` and `50`. Defaults to `20`.
              Values outside the range are clamped, and a non-numeric value falls back to
              `20`.

          start_date: An inclusive lower bound on `created_at`, as an ISO 8601 date or timestamp (e.g.
              `2026-08-18` or `2026-08-18T20:06:36.259Z`). Any other format returns `400`.

          status: A comma-separated list of run statuses to filter on, e.g. `PROCESSED,ERROR`.

          template_id: A comma-separated list of Automation Template ids to filter on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/automations/runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "end_date": end_date,
                        "limit": limit,
                        "start_date": start_date,
                        "status": status,
                        "template_id": template_id,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            cast_to=AutomationRunListResponse,
        )

    def list_steps(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutomationRunStepsResponse:
        """
        List the per-step state of one Automation run, in full — this endpoint is not
        paginated. `message_id` is present on send steps that produced a message; follow
        it to `GET /messages/{message_id}` for delivery status. A send to a List or an
        Audience yields one `message_id` for the request, not one per recipient.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/automations/runs/{id}/steps", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomationRunStepsResponse,
        )


class AsyncRunsResource(AsyncAPIResource):
    """
    Invoke a stored automation template or an ad hoc automation defined in the request.
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

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        end_date: str | Omit = omit,
        limit: str | Omit = omit,
        start_date: str | Omit = omit,
        status: str | Omit = omit,
        template_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutomationRunListResponse:
        """
        List runs of the workspace's v2 Automations, newest first, filtered by status,
        Template, or date range and paged by cursor. Journey (v3) runs are listed by
        `GET /journeys/runs` instead — the two surfaces never return each other's runs.
        Runs are retained for 95 days.

        Args:
          cursor: A cursor token for pagination. Use the `next_cursor` from the previous response
              to fetch the next page of results. Treat it as opaque.

          end_date: An inclusive upper bound on `created_at`, in the same format as `start_date`.

          limit: The number of runs to return per page, between `1` and `50`. Defaults to `20`.
              Values outside the range are clamped, and a non-numeric value falls back to
              `20`.

          start_date: An inclusive lower bound on `created_at`, as an ISO 8601 date or timestamp (e.g.
              `2026-08-18` or `2026-08-18T20:06:36.259Z`). Any other format returns `400`.

          status: A comma-separated list of run statuses to filter on, e.g. `PROCESSED,ERROR`.

          template_id: A comma-separated list of Automation Template ids to filter on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/automations/runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "end_date": end_date,
                        "limit": limit,
                        "start_date": start_date,
                        "status": status,
                        "template_id": template_id,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            cast_to=AutomationRunListResponse,
        )

    async def list_steps(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutomationRunStepsResponse:
        """
        List the per-step state of one Automation run, in full — this endpoint is not
        paginated. `message_id` is present on send steps that produced a message; follow
        it to `GET /messages/{message_id}` for delivery status. A send to a List or an
        Audience yields one `message_id` for the request, not one per recipient.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/automations/runs/{id}/steps", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomationRunStepsResponse,
        )


class RunsResourceWithRawResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.list = to_raw_response_wrapper(
            runs.list,
        )
        self.list_steps = to_raw_response_wrapper(
            runs.list_steps,
        )


class AsyncRunsResourceWithRawResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.list = async_to_raw_response_wrapper(
            runs.list,
        )
        self.list_steps = async_to_raw_response_wrapper(
            runs.list_steps,
        )


class RunsResourceWithStreamingResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.list = to_streamed_response_wrapper(
            runs.list,
        )
        self.list_steps = to_streamed_response_wrapper(
            runs.list_steps,
        )


class AsyncRunsResourceWithStreamingResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.list = async_to_streamed_response_wrapper(
            runs.list,
        )
        self.list_steps = async_to_streamed_response_wrapper(
            runs.list_steps,
        )
