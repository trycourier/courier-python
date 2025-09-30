# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types import (
    Audience,
    AudienceListResponse,
    AudienceUpdateResponse,
    AudienceListMembersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAudiences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Courier) -> None:
        audience = client.audiences.retrieve(
            "audience_id",
        )
        assert_matches_type(Audience, audience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Courier) -> None:
        response = client.audiences.with_raw_response.retrieve(
            "audience_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = response.parse()
        assert_matches_type(Audience, audience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Courier) -> None:
        with client.audiences.with_streaming_response.retrieve(
            "audience_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = response.parse()
            assert_matches_type(Audience, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audience_id` but received ''"):
            client.audiences.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Courier) -> None:
        audience = client.audiences.update(
            audience_id="audience_id",
        )
        assert_matches_type(AudienceUpdateResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Courier) -> None:
        audience = client.audiences.update(
            audience_id="audience_id",
            description="description",
            filter={
                "operator": "ENDS_WITH",
                "path": "path",
                "value": "value",
            },
            name="name",
        )
        assert_matches_type(AudienceUpdateResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Courier) -> None:
        response = client.audiences.with_raw_response.update(
            audience_id="audience_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = response.parse()
        assert_matches_type(AudienceUpdateResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Courier) -> None:
        with client.audiences.with_streaming_response.update(
            audience_id="audience_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = response.parse()
            assert_matches_type(AudienceUpdateResponse, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audience_id` but received ''"):
            client.audiences.with_raw_response.update(
                audience_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Courier) -> None:
        audience = client.audiences.list()
        assert_matches_type(AudienceListResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Courier) -> None:
        audience = client.audiences.list(
            cursor="cursor",
        )
        assert_matches_type(AudienceListResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Courier) -> None:
        response = client.audiences.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = response.parse()
        assert_matches_type(AudienceListResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Courier) -> None:
        with client.audiences.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = response.parse()
            assert_matches_type(AudienceListResponse, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Courier) -> None:
        audience = client.audiences.delete(
            "audience_id",
        )
        assert audience is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Courier) -> None:
        response = client.audiences.with_raw_response.delete(
            "audience_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = response.parse()
        assert audience is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Courier) -> None:
        with client.audiences.with_streaming_response.delete(
            "audience_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = response.parse()
            assert audience is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audience_id` but received ''"):
            client.audiences.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_members(self, client: Courier) -> None:
        audience = client.audiences.list_members(
            audience_id="audience_id",
        )
        assert_matches_type(AudienceListMembersResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_members_with_all_params(self, client: Courier) -> None:
        audience = client.audiences.list_members(
            audience_id="audience_id",
            cursor="cursor",
        )
        assert_matches_type(AudienceListMembersResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_members(self, client: Courier) -> None:
        response = client.audiences.with_raw_response.list_members(
            audience_id="audience_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = response.parse()
        assert_matches_type(AudienceListMembersResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_members(self, client: Courier) -> None:
        with client.audiences.with_streaming_response.list_members(
            audience_id="audience_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = response.parse()
            assert_matches_type(AudienceListMembersResponse, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_members(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audience_id` but received ''"):
            client.audiences.with_raw_response.list_members(
                audience_id="",
            )


class TestAsyncAudiences:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCourier) -> None:
        audience = await async_client.audiences.retrieve(
            "audience_id",
        )
        assert_matches_type(Audience, audience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCourier) -> None:
        response = await async_client.audiences.with_raw_response.retrieve(
            "audience_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = await response.parse()
        assert_matches_type(Audience, audience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCourier) -> None:
        async with async_client.audiences.with_streaming_response.retrieve(
            "audience_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = await response.parse()
            assert_matches_type(Audience, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audience_id` but received ''"):
            await async_client.audiences.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCourier) -> None:
        audience = await async_client.audiences.update(
            audience_id="audience_id",
        )
        assert_matches_type(AudienceUpdateResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCourier) -> None:
        audience = await async_client.audiences.update(
            audience_id="audience_id",
            description="description",
            filter={
                "operator": "ENDS_WITH",
                "path": "path",
                "value": "value",
            },
            name="name",
        )
        assert_matches_type(AudienceUpdateResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCourier) -> None:
        response = await async_client.audiences.with_raw_response.update(
            audience_id="audience_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = await response.parse()
        assert_matches_type(AudienceUpdateResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCourier) -> None:
        async with async_client.audiences.with_streaming_response.update(
            audience_id="audience_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = await response.parse()
            assert_matches_type(AudienceUpdateResponse, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audience_id` but received ''"):
            await async_client.audiences.with_raw_response.update(
                audience_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCourier) -> None:
        audience = await async_client.audiences.list()
        assert_matches_type(AudienceListResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCourier) -> None:
        audience = await async_client.audiences.list(
            cursor="cursor",
        )
        assert_matches_type(AudienceListResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCourier) -> None:
        response = await async_client.audiences.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = await response.parse()
        assert_matches_type(AudienceListResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCourier) -> None:
        async with async_client.audiences.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = await response.parse()
            assert_matches_type(AudienceListResponse, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCourier) -> None:
        audience = await async_client.audiences.delete(
            "audience_id",
        )
        assert audience is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCourier) -> None:
        response = await async_client.audiences.with_raw_response.delete(
            "audience_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = await response.parse()
        assert audience is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCourier) -> None:
        async with async_client.audiences.with_streaming_response.delete(
            "audience_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = await response.parse()
            assert audience is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audience_id` but received ''"):
            await async_client.audiences.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_members(self, async_client: AsyncCourier) -> None:
        audience = await async_client.audiences.list_members(
            audience_id="audience_id",
        )
        assert_matches_type(AudienceListMembersResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_members_with_all_params(self, async_client: AsyncCourier) -> None:
        audience = await async_client.audiences.list_members(
            audience_id="audience_id",
            cursor="cursor",
        )
        assert_matches_type(AudienceListMembersResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_members(self, async_client: AsyncCourier) -> None:
        response = await async_client.audiences.with_raw_response.list_members(
            audience_id="audience_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audience = await response.parse()
        assert_matches_type(AudienceListMembersResponse, audience, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_members(self, async_client: AsyncCourier) -> None:
        async with async_client.audiences.with_streaming_response.list_members(
            audience_id="audience_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audience = await response.parse()
            assert_matches_type(AudienceListMembersResponse, audience, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_members(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audience_id` but received ''"):
            await async_client.audiences.with_raw_response.list_members(
                audience_id="",
            )
