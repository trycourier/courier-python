# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.users import (
    preference_retrieve_params,
    preference_bulk_update_params,
    preference_bulk_replace_params,
    preference_delete_topic_params,
    preference_retrieve_topic_params,
    preference_update_or_create_topic_params,
)
from ..._base_client import make_request_options
from ...types.users.preference_retrieve_response import PreferenceRetrieveResponse
from ...types.users.preference_bulk_update_response import PreferenceBulkUpdateResponse
from ...types.users.preference_bulk_replace_response import PreferenceBulkReplaceResponse
from ...types.users.preference_retrieve_topic_response import PreferenceRetrieveTopicResponse
from ...types.users.preference_update_or_create_topic_response import PreferenceUpdateOrCreateTopicResponse

__all__ = ["PreferencesResource", "AsyncPreferencesResource"]


class PreferencesResource(SyncAPIResource):
    """
    Read and write a single user's notification preferences, per topic and per channel.
    """

    @cached_property
    def with_raw_response(self) -> PreferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return PreferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PreferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return PreferencesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        user_id: str,
        *,
        tenant_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceRetrieveResponse:
        """
        Returns a user's preference overrides with paging, one entry per subscription
        topic they have set a choice for.

        Args:
          tenant_id: Query the preferences of a user for this specific tenant context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            path_template("/users/{user_id}/preferences", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"tenant_id": tenant_id}, preference_retrieve_params.PreferenceRetrieveParams),
            ),
            cast_to=PreferenceRetrieveResponse,
        )

    def bulk_replace(
        self,
        user_id: str,
        *,
        topics: Iterable[preference_bulk_replace_params.Topic],
        tenant_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceBulkReplaceResponse:
        """Replaces a user's entire set of preference overrides.

        Any topic you leave out is
        reset to its default, so send the full set rather than a subset.

        Args:
          topics: The complete set of topic overrides for the user. Up to 50 topics may be
              provided. Any existing override not listed here is reset to its topic default;
              an empty array resets every existing override.

          tenant_id: Replace the preferences of a user for this specific tenant context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._put(
            path_template("/users/{user_id}/preferences", user_id=user_id),
            body=maybe_transform({"topics": topics}, preference_bulk_replace_params.PreferenceBulkReplaceParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"tenant_id": tenant_id}, preference_bulk_replace_params.PreferenceBulkReplaceParams
                ),
            ),
            cast_to=PreferenceBulkReplaceResponse,
        )

    def bulk_update(
        self,
        user_id: str,
        *,
        topics: Iterable[preference_bulk_update_params.Topic],
        tenant_id: Optional[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_idempotency_expiration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceBulkUpdateResponse:
        """
        Adds or updates a user's preferences for several subscription topics at once.
        Topics you leave out keep whatever they were set to before.

        Args:
          topics: The topics to create or update. Between 1 and 50 topics may be provided in a
              single request.

          tenant_id: Update the preferences of a user for this specific tenant context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
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
            path_template("/users/{user_id}/preferences", user_id=user_id),
            body=maybe_transform({"topics": topics}, preference_bulk_update_params.PreferenceBulkUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"tenant_id": tenant_id}, preference_bulk_update_params.PreferenceBulkUpdateParams
                ),
            ),
            cast_to=PreferenceBulkUpdateResponse,
        )

    def delete_topic(
        self,
        topic_id: str,
        *,
        user_id: str,
        tenant_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes a user's override for one subscription topic, resetting it to the
        effective default from the tenant or workspace.

        Args:
          tenant_id: Delete the preferences of a user for this specific tenant context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not topic_id:
            raise ValueError(f"Expected a non-empty value for `topic_id` but received {topic_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/users/{user_id}/preferences/{topic_id}", user_id=user_id, topic_id=topic_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"tenant_id": tenant_id}, preference_delete_topic_params.PreferenceDeleteTopicParams
                ),
            ),
            cast_to=NoneType,
        )

    def retrieve_topic(
        self,
        topic_id: str,
        *,
        user_id: str,
        tenant_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceRetrieveTopicResponse:
        """
        Returns a user's opt-in status and channel choices for one subscription topic,
        or the effective default if they have set no override.

        Args:
          tenant_id: Query the preferences of a user for this specific tenant context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not topic_id:
            raise ValueError(f"Expected a non-empty value for `topic_id` but received {topic_id!r}")
        return self._get(
            path_template("/users/{user_id}/preferences/{topic_id}", user_id=user_id, topic_id=topic_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"tenant_id": tenant_id}, preference_retrieve_topic_params.PreferenceRetrieveTopicParams
                ),
            ),
            cast_to=PreferenceRetrieveTopicResponse,
        )

    def update_or_create_topic(
        self,
        topic_id: str,
        *,
        user_id: str,
        topic: preference_update_or_create_topic_params.Topic,
        tenant_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceUpdateOrCreateTopicResponse:
        """
        Sets a user's opt-in status and channel choices for one subscription topic,
        overriding the tenant default for that topic only.

        Args:
          tenant_id: Update the preferences of a user for this specific tenant context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not topic_id:
            raise ValueError(f"Expected a non-empty value for `topic_id` but received {topic_id!r}")
        return self._put(
            path_template("/users/{user_id}/preferences/{topic_id}", user_id=user_id, topic_id=topic_id),
            body=maybe_transform(
                {"topic": topic}, preference_update_or_create_topic_params.PreferenceUpdateOrCreateTopicParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"tenant_id": tenant_id},
                    preference_update_or_create_topic_params.PreferenceUpdateOrCreateTopicParams,
                ),
            ),
            cast_to=PreferenceUpdateOrCreateTopicResponse,
        )


class AsyncPreferencesResource(AsyncAPIResource):
    """
    Read and write a single user's notification preferences, per topic and per channel.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPreferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPreferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPreferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncPreferencesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        user_id: str,
        *,
        tenant_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceRetrieveResponse:
        """
        Returns a user's preference overrides with paging, one entry per subscription
        topic they have set a choice for.

        Args:
          tenant_id: Query the preferences of a user for this specific tenant context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            path_template("/users/{user_id}/preferences", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"tenant_id": tenant_id}, preference_retrieve_params.PreferenceRetrieveParams
                ),
            ),
            cast_to=PreferenceRetrieveResponse,
        )

    async def bulk_replace(
        self,
        user_id: str,
        *,
        topics: Iterable[preference_bulk_replace_params.Topic],
        tenant_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceBulkReplaceResponse:
        """Replaces a user's entire set of preference overrides.

        Any topic you leave out is
        reset to its default, so send the full set rather than a subset.

        Args:
          topics: The complete set of topic overrides for the user. Up to 50 topics may be
              provided. Any existing override not listed here is reset to its topic default;
              an empty array resets every existing override.

          tenant_id: Replace the preferences of a user for this specific tenant context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._put(
            path_template("/users/{user_id}/preferences", user_id=user_id),
            body=await async_maybe_transform(
                {"topics": topics}, preference_bulk_replace_params.PreferenceBulkReplaceParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"tenant_id": tenant_id}, preference_bulk_replace_params.PreferenceBulkReplaceParams
                ),
            ),
            cast_to=PreferenceBulkReplaceResponse,
        )

    async def bulk_update(
        self,
        user_id: str,
        *,
        topics: Iterable[preference_bulk_update_params.Topic],
        tenant_id: Optional[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_idempotency_expiration: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceBulkUpdateResponse:
        """
        Adds or updates a user's preferences for several subscription topics at once.
        Topics you leave out keep whatever they were set to before.

        Args:
          topics: The topics to create or update. Between 1 and 50 topics may be provided in a
              single request.

          tenant_id: Update the preferences of a user for this specific tenant context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
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
            path_template("/users/{user_id}/preferences", user_id=user_id),
            body=await async_maybe_transform(
                {"topics": topics}, preference_bulk_update_params.PreferenceBulkUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"tenant_id": tenant_id}, preference_bulk_update_params.PreferenceBulkUpdateParams
                ),
            ),
            cast_to=PreferenceBulkUpdateResponse,
        )

    async def delete_topic(
        self,
        topic_id: str,
        *,
        user_id: str,
        tenant_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes a user's override for one subscription topic, resetting it to the
        effective default from the tenant or workspace.

        Args:
          tenant_id: Delete the preferences of a user for this specific tenant context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not topic_id:
            raise ValueError(f"Expected a non-empty value for `topic_id` but received {topic_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/users/{user_id}/preferences/{topic_id}", user_id=user_id, topic_id=topic_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"tenant_id": tenant_id}, preference_delete_topic_params.PreferenceDeleteTopicParams
                ),
            ),
            cast_to=NoneType,
        )

    async def retrieve_topic(
        self,
        topic_id: str,
        *,
        user_id: str,
        tenant_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceRetrieveTopicResponse:
        """
        Returns a user's opt-in status and channel choices for one subscription topic,
        or the effective default if they have set no override.

        Args:
          tenant_id: Query the preferences of a user for this specific tenant context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not topic_id:
            raise ValueError(f"Expected a non-empty value for `topic_id` but received {topic_id!r}")
        return await self._get(
            path_template("/users/{user_id}/preferences/{topic_id}", user_id=user_id, topic_id=topic_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"tenant_id": tenant_id}, preference_retrieve_topic_params.PreferenceRetrieveTopicParams
                ),
            ),
            cast_to=PreferenceRetrieveTopicResponse,
        )

    async def update_or_create_topic(
        self,
        topic_id: str,
        *,
        user_id: str,
        topic: preference_update_or_create_topic_params.Topic,
        tenant_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceUpdateOrCreateTopicResponse:
        """
        Sets a user's opt-in status and channel choices for one subscription topic,
        overriding the tenant default for that topic only.

        Args:
          tenant_id: Update the preferences of a user for this specific tenant context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not topic_id:
            raise ValueError(f"Expected a non-empty value for `topic_id` but received {topic_id!r}")
        return await self._put(
            path_template("/users/{user_id}/preferences/{topic_id}", user_id=user_id, topic_id=topic_id),
            body=await async_maybe_transform(
                {"topic": topic}, preference_update_or_create_topic_params.PreferenceUpdateOrCreateTopicParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"tenant_id": tenant_id},
                    preference_update_or_create_topic_params.PreferenceUpdateOrCreateTopicParams,
                ),
            ),
            cast_to=PreferenceUpdateOrCreateTopicResponse,
        )


class PreferencesResourceWithRawResponse:
    def __init__(self, preferences: PreferencesResource) -> None:
        self._preferences = preferences

        self.retrieve = to_raw_response_wrapper(
            preferences.retrieve,
        )
        self.bulk_replace = to_raw_response_wrapper(
            preferences.bulk_replace,
        )
        self.bulk_update = to_raw_response_wrapper(
            preferences.bulk_update,
        )
        self.delete_topic = to_raw_response_wrapper(
            preferences.delete_topic,
        )
        self.retrieve_topic = to_raw_response_wrapper(
            preferences.retrieve_topic,
        )
        self.update_or_create_topic = to_raw_response_wrapper(
            preferences.update_or_create_topic,
        )


class AsyncPreferencesResourceWithRawResponse:
    def __init__(self, preferences: AsyncPreferencesResource) -> None:
        self._preferences = preferences

        self.retrieve = async_to_raw_response_wrapper(
            preferences.retrieve,
        )
        self.bulk_replace = async_to_raw_response_wrapper(
            preferences.bulk_replace,
        )
        self.bulk_update = async_to_raw_response_wrapper(
            preferences.bulk_update,
        )
        self.delete_topic = async_to_raw_response_wrapper(
            preferences.delete_topic,
        )
        self.retrieve_topic = async_to_raw_response_wrapper(
            preferences.retrieve_topic,
        )
        self.update_or_create_topic = async_to_raw_response_wrapper(
            preferences.update_or_create_topic,
        )


class PreferencesResourceWithStreamingResponse:
    def __init__(self, preferences: PreferencesResource) -> None:
        self._preferences = preferences

        self.retrieve = to_streamed_response_wrapper(
            preferences.retrieve,
        )
        self.bulk_replace = to_streamed_response_wrapper(
            preferences.bulk_replace,
        )
        self.bulk_update = to_streamed_response_wrapper(
            preferences.bulk_update,
        )
        self.delete_topic = to_streamed_response_wrapper(
            preferences.delete_topic,
        )
        self.retrieve_topic = to_streamed_response_wrapper(
            preferences.retrieve_topic,
        )
        self.update_or_create_topic = to_streamed_response_wrapper(
            preferences.update_or_create_topic,
        )


class AsyncPreferencesResourceWithStreamingResponse:
    def __init__(self, preferences: AsyncPreferencesResource) -> None:
        self._preferences = preferences

        self.retrieve = async_to_streamed_response_wrapper(
            preferences.retrieve,
        )
        self.bulk_replace = async_to_streamed_response_wrapper(
            preferences.bulk_replace,
        )
        self.bulk_update = async_to_streamed_response_wrapper(
            preferences.bulk_update,
        )
        self.delete_topic = async_to_streamed_response_wrapper(
            preferences.delete_topic,
        )
        self.retrieve_topic = async_to_streamed_response_wrapper(
            preferences.retrieve_topic,
        )
        self.update_or_create_topic = async_to_streamed_response_wrapper(
            preferences.update_or_create_topic,
        )
