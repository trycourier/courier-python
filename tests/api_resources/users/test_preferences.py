# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types.users import (
    PreferenceRetrieveResponse,
    PreferenceRetrieveTopicResponse,
    PreferenceUpdateOrCreateTopicResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPreferences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Courier) -> None:
        preference = client.users.preferences.retrieve(
            user_id="user_id",
        )
        assert_matches_type(PreferenceRetrieveResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Courier) -> None:
        preference = client.users.preferences.retrieve(
            user_id="user_id",
            tenant_id="tenant_id",
        )
        assert_matches_type(PreferenceRetrieveResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Courier) -> None:
        response = client.users.preferences.with_raw_response.retrieve(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = response.parse()
        assert_matches_type(PreferenceRetrieveResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Courier) -> None:
        with client.users.preferences.with_streaming_response.retrieve(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = response.parse()
            assert_matches_type(PreferenceRetrieveResponse, preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.preferences.with_raw_response.retrieve(
                user_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_topic(self, client: Courier) -> None:
        preference = client.users.preferences.retrieve_topic(
            topic_id="topic_id",
            user_id="user_id",
        )
        assert_matches_type(PreferenceRetrieveTopicResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_topic_with_all_params(self, client: Courier) -> None:
        preference = client.users.preferences.retrieve_topic(
            topic_id="topic_id",
            user_id="user_id",
            tenant_id="tenant_id",
        )
        assert_matches_type(PreferenceRetrieveTopicResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_topic(self, client: Courier) -> None:
        response = client.users.preferences.with_raw_response.retrieve_topic(
            topic_id="topic_id",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = response.parse()
        assert_matches_type(PreferenceRetrieveTopicResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_topic(self, client: Courier) -> None:
        with client.users.preferences.with_streaming_response.retrieve_topic(
            topic_id="topic_id",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = response.parse()
            assert_matches_type(PreferenceRetrieveTopicResponse, preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_topic(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.preferences.with_raw_response.retrieve_topic(
                topic_id="topic_id",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `topic_id` but received ''"):
            client.users.preferences.with_raw_response.retrieve_topic(
                topic_id="",
                user_id="user_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_or_create_topic(self, client: Courier) -> None:
        preference = client.users.preferences.update_or_create_topic(
            topic_id="topic_id",
            user_id="user_id",
            topic={"status": "OPTED_IN"},
        )
        assert_matches_type(PreferenceUpdateOrCreateTopicResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_or_create_topic_with_all_params(self, client: Courier) -> None:
        preference = client.users.preferences.update_or_create_topic(
            topic_id="topic_id",
            user_id="user_id",
            topic={
                "status": "OPTED_IN",
                "custom_routing": ["inbox", "email"],
                "has_custom_routing": True,
            },
            tenant_id="tenant_id",
        )
        assert_matches_type(PreferenceUpdateOrCreateTopicResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_or_create_topic(self, client: Courier) -> None:
        response = client.users.preferences.with_raw_response.update_or_create_topic(
            topic_id="topic_id",
            user_id="user_id",
            topic={"status": "OPTED_IN"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = response.parse()
        assert_matches_type(PreferenceUpdateOrCreateTopicResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_or_create_topic(self, client: Courier) -> None:
        with client.users.preferences.with_streaming_response.update_or_create_topic(
            topic_id="topic_id",
            user_id="user_id",
            topic={"status": "OPTED_IN"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = response.parse()
            assert_matches_type(PreferenceUpdateOrCreateTopicResponse, preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_or_create_topic(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.preferences.with_raw_response.update_or_create_topic(
                topic_id="topic_id",
                user_id="",
                topic={"status": "OPTED_IN"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `topic_id` but received ''"):
            client.users.preferences.with_raw_response.update_or_create_topic(
                topic_id="",
                user_id="user_id",
                topic={"status": "OPTED_IN"},
            )


class TestAsyncPreferences:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCourier) -> None:
        preference = await async_client.users.preferences.retrieve(
            user_id="user_id",
        )
        assert_matches_type(PreferenceRetrieveResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncCourier) -> None:
        preference = await async_client.users.preferences.retrieve(
            user_id="user_id",
            tenant_id="tenant_id",
        )
        assert_matches_type(PreferenceRetrieveResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCourier) -> None:
        response = await async_client.users.preferences.with_raw_response.retrieve(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = await response.parse()
        assert_matches_type(PreferenceRetrieveResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCourier) -> None:
        async with async_client.users.preferences.with_streaming_response.retrieve(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = await response.parse()
            assert_matches_type(PreferenceRetrieveResponse, preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.preferences.with_raw_response.retrieve(
                user_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_topic(self, async_client: AsyncCourier) -> None:
        preference = await async_client.users.preferences.retrieve_topic(
            topic_id="topic_id",
            user_id="user_id",
        )
        assert_matches_type(PreferenceRetrieveTopicResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_topic_with_all_params(self, async_client: AsyncCourier) -> None:
        preference = await async_client.users.preferences.retrieve_topic(
            topic_id="topic_id",
            user_id="user_id",
            tenant_id="tenant_id",
        )
        assert_matches_type(PreferenceRetrieveTopicResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_topic(self, async_client: AsyncCourier) -> None:
        response = await async_client.users.preferences.with_raw_response.retrieve_topic(
            topic_id="topic_id",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = await response.parse()
        assert_matches_type(PreferenceRetrieveTopicResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_topic(self, async_client: AsyncCourier) -> None:
        async with async_client.users.preferences.with_streaming_response.retrieve_topic(
            topic_id="topic_id",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = await response.parse()
            assert_matches_type(PreferenceRetrieveTopicResponse, preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_topic(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.preferences.with_raw_response.retrieve_topic(
                topic_id="topic_id",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `topic_id` but received ''"):
            await async_client.users.preferences.with_raw_response.retrieve_topic(
                topic_id="",
                user_id="user_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_or_create_topic(self, async_client: AsyncCourier) -> None:
        preference = await async_client.users.preferences.update_or_create_topic(
            topic_id="topic_id",
            user_id="user_id",
            topic={"status": "OPTED_IN"},
        )
        assert_matches_type(PreferenceUpdateOrCreateTopicResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_or_create_topic_with_all_params(self, async_client: AsyncCourier) -> None:
        preference = await async_client.users.preferences.update_or_create_topic(
            topic_id="topic_id",
            user_id="user_id",
            topic={
                "status": "OPTED_IN",
                "custom_routing": ["inbox", "email"],
                "has_custom_routing": True,
            },
            tenant_id="tenant_id",
        )
        assert_matches_type(PreferenceUpdateOrCreateTopicResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_or_create_topic(self, async_client: AsyncCourier) -> None:
        response = await async_client.users.preferences.with_raw_response.update_or_create_topic(
            topic_id="topic_id",
            user_id="user_id",
            topic={"status": "OPTED_IN"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = await response.parse()
        assert_matches_type(PreferenceUpdateOrCreateTopicResponse, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_or_create_topic(self, async_client: AsyncCourier) -> None:
        async with async_client.users.preferences.with_streaming_response.update_or_create_topic(
            topic_id="topic_id",
            user_id="user_id",
            topic={"status": "OPTED_IN"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = await response.parse()
            assert_matches_type(PreferenceUpdateOrCreateTopicResponse, preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_or_create_topic(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.preferences.with_raw_response.update_or_create_topic(
                topic_id="topic_id",
                user_id="",
                topic={"status": "OPTED_IN"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `topic_id` but received ''"):
            await async_client.users.preferences.with_raw_response.update_or_create_topic(
                topic_id="",
                user_id="user_id",
                topic={"status": "OPTED_IN"},
            )
