# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types import (
    PublishPreferencesResponse,
    PreferenceSectionGetResponse,
    PreferenceSectionListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPreferenceSections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Courier) -> None:
        preference_section = client.preference_sections.create(
            name="Account Notifications",
        )
        assert_matches_type(PreferenceSectionGetResponse, preference_section, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Courier) -> None:
        preference_section = client.preference_sections.create(
            name="Account Notifications",
            has_custom_routing=True,
            routing_options=["direct_message"],
        )
        assert_matches_type(PreferenceSectionGetResponse, preference_section, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Courier) -> None:
        response = client.preference_sections.with_raw_response.create(
            name="Account Notifications",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference_section = response.parse()
        assert_matches_type(PreferenceSectionGetResponse, preference_section, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Courier) -> None:
        with client.preference_sections.with_streaming_response.create(
            name="Account Notifications",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference_section = response.parse()
            assert_matches_type(PreferenceSectionGetResponse, preference_section, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Courier) -> None:
        preference_section = client.preference_sections.retrieve(
            "section_id",
        )
        assert_matches_type(PreferenceSectionGetResponse, preference_section, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Courier) -> None:
        response = client.preference_sections.with_raw_response.retrieve(
            "section_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference_section = response.parse()
        assert_matches_type(PreferenceSectionGetResponse, preference_section, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Courier) -> None:
        with client.preference_sections.with_streaming_response.retrieve(
            "section_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference_section = response.parse()
            assert_matches_type(PreferenceSectionGetResponse, preference_section, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `section_id` but received ''"):
            client.preference_sections.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Courier) -> None:
        preference_section = client.preference_sections.list()
        assert_matches_type(PreferenceSectionListResponse, preference_section, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Courier) -> None:
        response = client.preference_sections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference_section = response.parse()
        assert_matches_type(PreferenceSectionListResponse, preference_section, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Courier) -> None:
        with client.preference_sections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference_section = response.parse()
            assert_matches_type(PreferenceSectionListResponse, preference_section, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive(self, client: Courier) -> None:
        preference_section = client.preference_sections.archive(
            "section_id",
        )
        assert preference_section is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: Courier) -> None:
        response = client.preference_sections.with_raw_response.archive(
            "section_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference_section = response.parse()
        assert preference_section is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: Courier) -> None:
        with client.preference_sections.with_streaming_response.archive(
            "section_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference_section = response.parse()
            assert preference_section is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `section_id` but received ''"):
            client.preference_sections.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_publish(self, client: Courier) -> None:
        preference_section = client.preference_sections.publish()
        assert_matches_type(PublishPreferencesResponse, preference_section, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_publish(self, client: Courier) -> None:
        response = client.preference_sections.with_raw_response.publish()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference_section = response.parse()
        assert_matches_type(PublishPreferencesResponse, preference_section, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_publish(self, client: Courier) -> None:
        with client.preference_sections.with_streaming_response.publish() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference_section = response.parse()
            assert_matches_type(PublishPreferencesResponse, preference_section, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace(self, client: Courier) -> None:
        preference_section = client.preference_sections.replace(
            section_id="section_id",
            name="name",
        )
        assert_matches_type(PreferenceSectionGetResponse, preference_section, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace_with_all_params(self, client: Courier) -> None:
        preference_section = client.preference_sections.replace(
            section_id="section_id",
            name="name",
            has_custom_routing=True,
            routing_options=["direct_message"],
        )
        assert_matches_type(PreferenceSectionGetResponse, preference_section, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_replace(self, client: Courier) -> None:
        response = client.preference_sections.with_raw_response.replace(
            section_id="section_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference_section = response.parse()
        assert_matches_type(PreferenceSectionGetResponse, preference_section, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_replace(self, client: Courier) -> None:
        with client.preference_sections.with_streaming_response.replace(
            section_id="section_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference_section = response.parse()
            assert_matches_type(PreferenceSectionGetResponse, preference_section, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_replace(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `section_id` but received ''"):
            client.preference_sections.with_raw_response.replace(
                section_id="",
                name="name",
            )


class TestAsyncPreferenceSections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCourier) -> None:
        preference_section = await async_client.preference_sections.create(
            name="Account Notifications",
        )
        assert_matches_type(PreferenceSectionGetResponse, preference_section, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCourier) -> None:
        preference_section = await async_client.preference_sections.create(
            name="Account Notifications",
            has_custom_routing=True,
            routing_options=["direct_message"],
        )
        assert_matches_type(PreferenceSectionGetResponse, preference_section, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCourier) -> None:
        response = await async_client.preference_sections.with_raw_response.create(
            name="Account Notifications",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference_section = await response.parse()
        assert_matches_type(PreferenceSectionGetResponse, preference_section, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCourier) -> None:
        async with async_client.preference_sections.with_streaming_response.create(
            name="Account Notifications",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference_section = await response.parse()
            assert_matches_type(PreferenceSectionGetResponse, preference_section, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCourier) -> None:
        preference_section = await async_client.preference_sections.retrieve(
            "section_id",
        )
        assert_matches_type(PreferenceSectionGetResponse, preference_section, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCourier) -> None:
        response = await async_client.preference_sections.with_raw_response.retrieve(
            "section_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference_section = await response.parse()
        assert_matches_type(PreferenceSectionGetResponse, preference_section, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCourier) -> None:
        async with async_client.preference_sections.with_streaming_response.retrieve(
            "section_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference_section = await response.parse()
            assert_matches_type(PreferenceSectionGetResponse, preference_section, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `section_id` but received ''"):
            await async_client.preference_sections.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCourier) -> None:
        preference_section = await async_client.preference_sections.list()
        assert_matches_type(PreferenceSectionListResponse, preference_section, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCourier) -> None:
        response = await async_client.preference_sections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference_section = await response.parse()
        assert_matches_type(PreferenceSectionListResponse, preference_section, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCourier) -> None:
        async with async_client.preference_sections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference_section = await response.parse()
            assert_matches_type(PreferenceSectionListResponse, preference_section, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncCourier) -> None:
        preference_section = await async_client.preference_sections.archive(
            "section_id",
        )
        assert preference_section is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncCourier) -> None:
        response = await async_client.preference_sections.with_raw_response.archive(
            "section_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference_section = await response.parse()
        assert preference_section is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncCourier) -> None:
        async with async_client.preference_sections.with_streaming_response.archive(
            "section_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference_section = await response.parse()
            assert preference_section is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `section_id` but received ''"):
            await async_client.preference_sections.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_publish(self, async_client: AsyncCourier) -> None:
        preference_section = await async_client.preference_sections.publish()
        assert_matches_type(PublishPreferencesResponse, preference_section, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_publish(self, async_client: AsyncCourier) -> None:
        response = await async_client.preference_sections.with_raw_response.publish()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference_section = await response.parse()
        assert_matches_type(PublishPreferencesResponse, preference_section, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_publish(self, async_client: AsyncCourier) -> None:
        async with async_client.preference_sections.with_streaming_response.publish() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference_section = await response.parse()
            assert_matches_type(PublishPreferencesResponse, preference_section, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace(self, async_client: AsyncCourier) -> None:
        preference_section = await async_client.preference_sections.replace(
            section_id="section_id",
            name="name",
        )
        assert_matches_type(PreferenceSectionGetResponse, preference_section, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncCourier) -> None:
        preference_section = await async_client.preference_sections.replace(
            section_id="section_id",
            name="name",
            has_custom_routing=True,
            routing_options=["direct_message"],
        )
        assert_matches_type(PreferenceSectionGetResponse, preference_section, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncCourier) -> None:
        response = await async_client.preference_sections.with_raw_response.replace(
            section_id="section_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference_section = await response.parse()
        assert_matches_type(PreferenceSectionGetResponse, preference_section, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncCourier) -> None:
        async with async_client.preference_sections.with_streaming_response.replace(
            section_id="section_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference_section = await response.parse()
            assert_matches_type(PreferenceSectionGetResponse, preference_section, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_replace(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `section_id` but received ''"):
            await async_client.preference_sections.with_raw_response.replace(
                section_id="",
                name="name",
            )
