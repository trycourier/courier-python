# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types.profiles import (
    ListDeleteResponse,
    ListRetrieveResponse,
    ListSubscribeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLists:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Courier) -> None:
        list_ = client.profiles.lists.retrieve(
            user_id="user_id",
        )
        assert_matches_type(ListRetrieveResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Courier) -> None:
        list_ = client.profiles.lists.retrieve(
            user_id="user_id",
            cursor="cursor",
        )
        assert_matches_type(ListRetrieveResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Courier) -> None:
        response = client.profiles.lists.with_raw_response.retrieve(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListRetrieveResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Courier) -> None:
        with client.profiles.lists.with_streaming_response.retrieve(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListRetrieveResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.profiles.lists.with_raw_response.retrieve(
                user_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Courier) -> None:
        list_ = client.profiles.lists.delete(
            "user_id",
        )
        assert_matches_type(ListDeleteResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Courier) -> None:
        response = client.profiles.lists.with_raw_response.delete(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListDeleteResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Courier) -> None:
        with client.profiles.lists.with_streaming_response.delete(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListDeleteResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.profiles.lists.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_subscribe(self, client: Courier) -> None:
        list_ = client.profiles.lists.subscribe(
            user_id="user_id",
            lists=[{"list_id": "listId"}],
        )
        assert_matches_type(ListSubscribeResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_subscribe(self, client: Courier) -> None:
        response = client.profiles.lists.with_raw_response.subscribe(
            user_id="user_id",
            lists=[{"list_id": "listId"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListSubscribeResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_subscribe(self, client: Courier) -> None:
        with client.profiles.lists.with_streaming_response.subscribe(
            user_id="user_id",
            lists=[{"list_id": "listId"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListSubscribeResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_subscribe(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.profiles.lists.with_raw_response.subscribe(
                user_id="",
                lists=[{"list_id": "listId"}],
            )


class TestAsyncLists:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCourier) -> None:
        list_ = await async_client.profiles.lists.retrieve(
            user_id="user_id",
        )
        assert_matches_type(ListRetrieveResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncCourier) -> None:
        list_ = await async_client.profiles.lists.retrieve(
            user_id="user_id",
            cursor="cursor",
        )
        assert_matches_type(ListRetrieveResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCourier) -> None:
        response = await async_client.profiles.lists.with_raw_response.retrieve(
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListRetrieveResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCourier) -> None:
        async with async_client.profiles.lists.with_streaming_response.retrieve(
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListRetrieveResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.profiles.lists.with_raw_response.retrieve(
                user_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCourier) -> None:
        list_ = await async_client.profiles.lists.delete(
            "user_id",
        )
        assert_matches_type(ListDeleteResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCourier) -> None:
        response = await async_client.profiles.lists.with_raw_response.delete(
            "user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListDeleteResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCourier) -> None:
        async with async_client.profiles.lists.with_streaming_response.delete(
            "user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListDeleteResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.profiles.lists.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_subscribe(self, async_client: AsyncCourier) -> None:
        list_ = await async_client.profiles.lists.subscribe(
            user_id="user_id",
            lists=[{"list_id": "listId"}],
        )
        assert_matches_type(ListSubscribeResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_subscribe(self, async_client: AsyncCourier) -> None:
        response = await async_client.profiles.lists.with_raw_response.subscribe(
            user_id="user_id",
            lists=[{"list_id": "listId"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListSubscribeResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_subscribe(self, async_client: AsyncCourier) -> None:
        async with async_client.profiles.lists.with_streaming_response.subscribe(
            user_id="user_id",
            lists=[{"list_id": "listId"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListSubscribeResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_subscribe(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.profiles.lists.with_raw_response.subscribe(
                user_id="",
                lists=[{"list_id": "listId"}],
            )
