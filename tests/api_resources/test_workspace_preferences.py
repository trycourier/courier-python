# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types import (
    PublishPreferencesResponse,
    WorkspacePreferenceGetResponse,
    WorkspacePreferenceListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkspacePreferences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Courier) -> None:
        workspace_preference = client.workspace_preferences.create(
            name="Account Notifications",
        )
        assert_matches_type(WorkspacePreferenceGetResponse, workspace_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Courier) -> None:
        workspace_preference = client.workspace_preferences.create(
            name="Account Notifications",
            has_custom_routing=True,
            routing_options=["direct_message"],
        )
        assert_matches_type(WorkspacePreferenceGetResponse, workspace_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Courier) -> None:
        response = client.workspace_preferences.with_raw_response.create(
            name="Account Notifications",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace_preference = response.parse()
        assert_matches_type(WorkspacePreferenceGetResponse, workspace_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Courier) -> None:
        with client.workspace_preferences.with_streaming_response.create(
            name="Account Notifications",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace_preference = response.parse()
            assert_matches_type(WorkspacePreferenceGetResponse, workspace_preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Courier) -> None:
        workspace_preference = client.workspace_preferences.retrieve(
            "section_id",
        )
        assert_matches_type(WorkspacePreferenceGetResponse, workspace_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Courier) -> None:
        response = client.workspace_preferences.with_raw_response.retrieve(
            "section_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace_preference = response.parse()
        assert_matches_type(WorkspacePreferenceGetResponse, workspace_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Courier) -> None:
        with client.workspace_preferences.with_streaming_response.retrieve(
            "section_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace_preference = response.parse()
            assert_matches_type(WorkspacePreferenceGetResponse, workspace_preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `section_id` but received ''"):
            client.workspace_preferences.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Courier) -> None:
        workspace_preference = client.workspace_preferences.list()
        assert_matches_type(WorkspacePreferenceListResponse, workspace_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Courier) -> None:
        response = client.workspace_preferences.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace_preference = response.parse()
        assert_matches_type(WorkspacePreferenceListResponse, workspace_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Courier) -> None:
        with client.workspace_preferences.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace_preference = response.parse()
            assert_matches_type(WorkspacePreferenceListResponse, workspace_preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive(self, client: Courier) -> None:
        workspace_preference = client.workspace_preferences.archive(
            "section_id",
        )
        assert workspace_preference is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: Courier) -> None:
        response = client.workspace_preferences.with_raw_response.archive(
            "section_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace_preference = response.parse()
        assert workspace_preference is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: Courier) -> None:
        with client.workspace_preferences.with_streaming_response.archive(
            "section_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace_preference = response.parse()
            assert workspace_preference is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `section_id` but received ''"):
            client.workspace_preferences.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_publish(self, client: Courier) -> None:
        workspace_preference = client.workspace_preferences.publish()
        assert_matches_type(PublishPreferencesResponse, workspace_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_publish(self, client: Courier) -> None:
        response = client.workspace_preferences.with_raw_response.publish()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace_preference = response.parse()
        assert_matches_type(PublishPreferencesResponse, workspace_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_publish(self, client: Courier) -> None:
        with client.workspace_preferences.with_streaming_response.publish() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace_preference = response.parse()
            assert_matches_type(PublishPreferencesResponse, workspace_preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace(self, client: Courier) -> None:
        workspace_preference = client.workspace_preferences.replace(
            section_id="section_id",
            name="name",
        )
        assert_matches_type(WorkspacePreferenceGetResponse, workspace_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace_with_all_params(self, client: Courier) -> None:
        workspace_preference = client.workspace_preferences.replace(
            section_id="section_id",
            name="name",
            has_custom_routing=True,
            routing_options=["direct_message"],
        )
        assert_matches_type(WorkspacePreferenceGetResponse, workspace_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_replace(self, client: Courier) -> None:
        response = client.workspace_preferences.with_raw_response.replace(
            section_id="section_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace_preference = response.parse()
        assert_matches_type(WorkspacePreferenceGetResponse, workspace_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_replace(self, client: Courier) -> None:
        with client.workspace_preferences.with_streaming_response.replace(
            section_id="section_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace_preference = response.parse()
            assert_matches_type(WorkspacePreferenceGetResponse, workspace_preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_replace(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `section_id` but received ''"):
            client.workspace_preferences.with_raw_response.replace(
                section_id="",
                name="name",
            )


class TestAsyncWorkspacePreferences:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCourier) -> None:
        workspace_preference = await async_client.workspace_preferences.create(
            name="Account Notifications",
        )
        assert_matches_type(WorkspacePreferenceGetResponse, workspace_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCourier) -> None:
        workspace_preference = await async_client.workspace_preferences.create(
            name="Account Notifications",
            has_custom_routing=True,
            routing_options=["direct_message"],
        )
        assert_matches_type(WorkspacePreferenceGetResponse, workspace_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCourier) -> None:
        response = await async_client.workspace_preferences.with_raw_response.create(
            name="Account Notifications",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace_preference = await response.parse()
        assert_matches_type(WorkspacePreferenceGetResponse, workspace_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCourier) -> None:
        async with async_client.workspace_preferences.with_streaming_response.create(
            name="Account Notifications",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace_preference = await response.parse()
            assert_matches_type(WorkspacePreferenceGetResponse, workspace_preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCourier) -> None:
        workspace_preference = await async_client.workspace_preferences.retrieve(
            "section_id",
        )
        assert_matches_type(WorkspacePreferenceGetResponse, workspace_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCourier) -> None:
        response = await async_client.workspace_preferences.with_raw_response.retrieve(
            "section_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace_preference = await response.parse()
        assert_matches_type(WorkspacePreferenceGetResponse, workspace_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCourier) -> None:
        async with async_client.workspace_preferences.with_streaming_response.retrieve(
            "section_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace_preference = await response.parse()
            assert_matches_type(WorkspacePreferenceGetResponse, workspace_preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `section_id` but received ''"):
            await async_client.workspace_preferences.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCourier) -> None:
        workspace_preference = await async_client.workspace_preferences.list()
        assert_matches_type(WorkspacePreferenceListResponse, workspace_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCourier) -> None:
        response = await async_client.workspace_preferences.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace_preference = await response.parse()
        assert_matches_type(WorkspacePreferenceListResponse, workspace_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCourier) -> None:
        async with async_client.workspace_preferences.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace_preference = await response.parse()
            assert_matches_type(WorkspacePreferenceListResponse, workspace_preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncCourier) -> None:
        workspace_preference = await async_client.workspace_preferences.archive(
            "section_id",
        )
        assert workspace_preference is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncCourier) -> None:
        response = await async_client.workspace_preferences.with_raw_response.archive(
            "section_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace_preference = await response.parse()
        assert workspace_preference is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncCourier) -> None:
        async with async_client.workspace_preferences.with_streaming_response.archive(
            "section_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace_preference = await response.parse()
            assert workspace_preference is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `section_id` but received ''"):
            await async_client.workspace_preferences.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_publish(self, async_client: AsyncCourier) -> None:
        workspace_preference = await async_client.workspace_preferences.publish()
        assert_matches_type(PublishPreferencesResponse, workspace_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_publish(self, async_client: AsyncCourier) -> None:
        response = await async_client.workspace_preferences.with_raw_response.publish()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace_preference = await response.parse()
        assert_matches_type(PublishPreferencesResponse, workspace_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_publish(self, async_client: AsyncCourier) -> None:
        async with async_client.workspace_preferences.with_streaming_response.publish() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace_preference = await response.parse()
            assert_matches_type(PublishPreferencesResponse, workspace_preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace(self, async_client: AsyncCourier) -> None:
        workspace_preference = await async_client.workspace_preferences.replace(
            section_id="section_id",
            name="name",
        )
        assert_matches_type(WorkspacePreferenceGetResponse, workspace_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncCourier) -> None:
        workspace_preference = await async_client.workspace_preferences.replace(
            section_id="section_id",
            name="name",
            has_custom_routing=True,
            routing_options=["direct_message"],
        )
        assert_matches_type(WorkspacePreferenceGetResponse, workspace_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncCourier) -> None:
        response = await async_client.workspace_preferences.with_raw_response.replace(
            section_id="section_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace_preference = await response.parse()
        assert_matches_type(WorkspacePreferenceGetResponse, workspace_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncCourier) -> None:
        async with async_client.workspace_preferences.with_streaming_response.replace(
            section_id="section_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace_preference = await response.parse()
            assert_matches_type(WorkspacePreferenceGetResponse, workspace_preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_replace(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `section_id` but received ''"):
            await async_client.workspace_preferences.with_raw_response.replace(
                section_id="",
                name="name",
            )
