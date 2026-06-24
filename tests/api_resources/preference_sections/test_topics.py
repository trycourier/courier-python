# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types import PreferenceTopicGetResponse, PreferenceTopicListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTopics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Courier) -> None:
        topic = client.preference_sections.topics.create(
            section_id="section_id",
            default_status="OPTED_OUT",
            name="Marketing",
        )
        assert_matches_type(PreferenceTopicGetResponse, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Courier) -> None:
        topic = client.preference_sections.topics.create(
            section_id="section_id",
            default_status="OPTED_OUT",
            name="Marketing",
            allowed_preferences=["snooze"],
            include_unsubscribe_header=True,
            routing_options=["direct_message"],
            topic_data={"foo": "bar"},
        )
        assert_matches_type(PreferenceTopicGetResponse, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Courier) -> None:
        response = client.preference_sections.topics.with_raw_response.create(
            section_id="section_id",
            default_status="OPTED_OUT",
            name="Marketing",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        topic = response.parse()
        assert_matches_type(PreferenceTopicGetResponse, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Courier) -> None:
        with client.preference_sections.topics.with_streaming_response.create(
            section_id="section_id",
            default_status="OPTED_OUT",
            name="Marketing",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            topic = response.parse()
            assert_matches_type(PreferenceTopicGetResponse, topic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `section_id` but received ''"):
            client.preference_sections.topics.with_raw_response.create(
                section_id="",
                default_status="OPTED_OUT",
                name="Marketing",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Courier) -> None:
        topic = client.preference_sections.topics.retrieve(
            topic_id="topic_id",
            section_id="section_id",
        )
        assert_matches_type(PreferenceTopicGetResponse, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Courier) -> None:
        response = client.preference_sections.topics.with_raw_response.retrieve(
            topic_id="topic_id",
            section_id="section_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        topic = response.parse()
        assert_matches_type(PreferenceTopicGetResponse, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Courier) -> None:
        with client.preference_sections.topics.with_streaming_response.retrieve(
            topic_id="topic_id",
            section_id="section_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            topic = response.parse()
            assert_matches_type(PreferenceTopicGetResponse, topic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `section_id` but received ''"):
            client.preference_sections.topics.with_raw_response.retrieve(
                topic_id="topic_id",
                section_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `topic_id` but received ''"):
            client.preference_sections.topics.with_raw_response.retrieve(
                topic_id="",
                section_id="section_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Courier) -> None:
        topic = client.preference_sections.topics.list(
            "section_id",
        )
        assert_matches_type(PreferenceTopicListResponse, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Courier) -> None:
        response = client.preference_sections.topics.with_raw_response.list(
            "section_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        topic = response.parse()
        assert_matches_type(PreferenceTopicListResponse, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Courier) -> None:
        with client.preference_sections.topics.with_streaming_response.list(
            "section_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            topic = response.parse()
            assert_matches_type(PreferenceTopicListResponse, topic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `section_id` but received ''"):
            client.preference_sections.topics.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive(self, client: Courier) -> None:
        topic = client.preference_sections.topics.archive(
            topic_id="topic_id",
            section_id="section_id",
        )
        assert topic is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: Courier) -> None:
        response = client.preference_sections.topics.with_raw_response.archive(
            topic_id="topic_id",
            section_id="section_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        topic = response.parse()
        assert topic is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: Courier) -> None:
        with client.preference_sections.topics.with_streaming_response.archive(
            topic_id="topic_id",
            section_id="section_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            topic = response.parse()
            assert topic is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `section_id` but received ''"):
            client.preference_sections.topics.with_raw_response.archive(
                topic_id="topic_id",
                section_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `topic_id` but received ''"):
            client.preference_sections.topics.with_raw_response.archive(
                topic_id="",
                section_id="section_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace(self, client: Courier) -> None:
        topic = client.preference_sections.topics.replace(
            topic_id="topic_id",
            section_id="section_id",
            default_status="OPTED_OUT",
            name="name",
        )
        assert_matches_type(PreferenceTopicGetResponse, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace_with_all_params(self, client: Courier) -> None:
        topic = client.preference_sections.topics.replace(
            topic_id="topic_id",
            section_id="section_id",
            default_status="OPTED_OUT",
            name="name",
            allowed_preferences=["snooze"],
            include_unsubscribe_header=True,
            routing_options=["direct_message"],
            topic_data={"foo": "bar"},
        )
        assert_matches_type(PreferenceTopicGetResponse, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_replace(self, client: Courier) -> None:
        response = client.preference_sections.topics.with_raw_response.replace(
            topic_id="topic_id",
            section_id="section_id",
            default_status="OPTED_OUT",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        topic = response.parse()
        assert_matches_type(PreferenceTopicGetResponse, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_replace(self, client: Courier) -> None:
        with client.preference_sections.topics.with_streaming_response.replace(
            topic_id="topic_id",
            section_id="section_id",
            default_status="OPTED_OUT",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            topic = response.parse()
            assert_matches_type(PreferenceTopicGetResponse, topic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_replace(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `section_id` but received ''"):
            client.preference_sections.topics.with_raw_response.replace(
                topic_id="topic_id",
                section_id="",
                default_status="OPTED_OUT",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `topic_id` but received ''"):
            client.preference_sections.topics.with_raw_response.replace(
                topic_id="",
                section_id="section_id",
                default_status="OPTED_OUT",
                name="name",
            )


class TestAsyncTopics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCourier) -> None:
        topic = await async_client.preference_sections.topics.create(
            section_id="section_id",
            default_status="OPTED_OUT",
            name="Marketing",
        )
        assert_matches_type(PreferenceTopicGetResponse, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCourier) -> None:
        topic = await async_client.preference_sections.topics.create(
            section_id="section_id",
            default_status="OPTED_OUT",
            name="Marketing",
            allowed_preferences=["snooze"],
            include_unsubscribe_header=True,
            routing_options=["direct_message"],
            topic_data={"foo": "bar"},
        )
        assert_matches_type(PreferenceTopicGetResponse, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCourier) -> None:
        response = await async_client.preference_sections.topics.with_raw_response.create(
            section_id="section_id",
            default_status="OPTED_OUT",
            name="Marketing",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        topic = await response.parse()
        assert_matches_type(PreferenceTopicGetResponse, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCourier) -> None:
        async with async_client.preference_sections.topics.with_streaming_response.create(
            section_id="section_id",
            default_status="OPTED_OUT",
            name="Marketing",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            topic = await response.parse()
            assert_matches_type(PreferenceTopicGetResponse, topic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `section_id` but received ''"):
            await async_client.preference_sections.topics.with_raw_response.create(
                section_id="",
                default_status="OPTED_OUT",
                name="Marketing",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCourier) -> None:
        topic = await async_client.preference_sections.topics.retrieve(
            topic_id="topic_id",
            section_id="section_id",
        )
        assert_matches_type(PreferenceTopicGetResponse, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCourier) -> None:
        response = await async_client.preference_sections.topics.with_raw_response.retrieve(
            topic_id="topic_id",
            section_id="section_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        topic = await response.parse()
        assert_matches_type(PreferenceTopicGetResponse, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCourier) -> None:
        async with async_client.preference_sections.topics.with_streaming_response.retrieve(
            topic_id="topic_id",
            section_id="section_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            topic = await response.parse()
            assert_matches_type(PreferenceTopicGetResponse, topic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `section_id` but received ''"):
            await async_client.preference_sections.topics.with_raw_response.retrieve(
                topic_id="topic_id",
                section_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `topic_id` but received ''"):
            await async_client.preference_sections.topics.with_raw_response.retrieve(
                topic_id="",
                section_id="section_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCourier) -> None:
        topic = await async_client.preference_sections.topics.list(
            "section_id",
        )
        assert_matches_type(PreferenceTopicListResponse, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCourier) -> None:
        response = await async_client.preference_sections.topics.with_raw_response.list(
            "section_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        topic = await response.parse()
        assert_matches_type(PreferenceTopicListResponse, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCourier) -> None:
        async with async_client.preference_sections.topics.with_streaming_response.list(
            "section_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            topic = await response.parse()
            assert_matches_type(PreferenceTopicListResponse, topic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `section_id` but received ''"):
            await async_client.preference_sections.topics.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncCourier) -> None:
        topic = await async_client.preference_sections.topics.archive(
            topic_id="topic_id",
            section_id="section_id",
        )
        assert topic is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncCourier) -> None:
        response = await async_client.preference_sections.topics.with_raw_response.archive(
            topic_id="topic_id",
            section_id="section_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        topic = await response.parse()
        assert topic is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncCourier) -> None:
        async with async_client.preference_sections.topics.with_streaming_response.archive(
            topic_id="topic_id",
            section_id="section_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            topic = await response.parse()
            assert topic is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `section_id` but received ''"):
            await async_client.preference_sections.topics.with_raw_response.archive(
                topic_id="topic_id",
                section_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `topic_id` but received ''"):
            await async_client.preference_sections.topics.with_raw_response.archive(
                topic_id="",
                section_id="section_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace(self, async_client: AsyncCourier) -> None:
        topic = await async_client.preference_sections.topics.replace(
            topic_id="topic_id",
            section_id="section_id",
            default_status="OPTED_OUT",
            name="name",
        )
        assert_matches_type(PreferenceTopicGetResponse, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncCourier) -> None:
        topic = await async_client.preference_sections.topics.replace(
            topic_id="topic_id",
            section_id="section_id",
            default_status="OPTED_OUT",
            name="name",
            allowed_preferences=["snooze"],
            include_unsubscribe_header=True,
            routing_options=["direct_message"],
            topic_data={"foo": "bar"},
        )
        assert_matches_type(PreferenceTopicGetResponse, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncCourier) -> None:
        response = await async_client.preference_sections.topics.with_raw_response.replace(
            topic_id="topic_id",
            section_id="section_id",
            default_status="OPTED_OUT",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        topic = await response.parse()
        assert_matches_type(PreferenceTopicGetResponse, topic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncCourier) -> None:
        async with async_client.preference_sections.topics.with_streaming_response.replace(
            topic_id="topic_id",
            section_id="section_id",
            default_status="OPTED_OUT",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            topic = await response.parse()
            assert_matches_type(PreferenceTopicGetResponse, topic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_replace(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `section_id` but received ''"):
            await async_client.preference_sections.topics.with_raw_response.replace(
                topic_id="topic_id",
                section_id="",
                default_status="OPTED_OUT",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `topic_id` but received ''"):
            await async_client.preference_sections.topics.with_raw_response.replace(
                topic_id="",
                section_id="section_id",
                default_status="OPTED_OUT",
                name="name",
            )
