# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Courier) -> None:
        item = client.tenants.preferences.items.update(
            topic_id="topic_id",
            tenant_id="tenant_id",
            status="OPTED_IN",
        )
        assert item is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Courier) -> None:
        item = client.tenants.preferences.items.update(
            topic_id="topic_id",
            tenant_id="tenant_id",
            status="OPTED_IN",
            custom_routing=["inbox"],
            has_custom_routing=True,
        )
        assert item is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Courier) -> None:
        response = client.tenants.preferences.items.with_raw_response.update(
            topic_id="topic_id",
            tenant_id="tenant_id",
            status="OPTED_IN",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert item is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Courier) -> None:
        with client.tenants.preferences.items.with_streaming_response.update(
            topic_id="topic_id",
            tenant_id="tenant_id",
            status="OPTED_IN",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert item is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.tenants.preferences.items.with_raw_response.update(
                topic_id="topic_id",
                tenant_id="",
                status="OPTED_IN",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `topic_id` but received ''"):
            client.tenants.preferences.items.with_raw_response.update(
                topic_id="",
                tenant_id="tenant_id",
                status="OPTED_IN",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Courier) -> None:
        item = client.tenants.preferences.items.delete(
            topic_id="topic_id",
            tenant_id="tenant_id",
        )
        assert item is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Courier) -> None:
        response = client.tenants.preferences.items.with_raw_response.delete(
            topic_id="topic_id",
            tenant_id="tenant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert item is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Courier) -> None:
        with client.tenants.preferences.items.with_streaming_response.delete(
            topic_id="topic_id",
            tenant_id="tenant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert item is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.tenants.preferences.items.with_raw_response.delete(
                topic_id="topic_id",
                tenant_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `topic_id` but received ''"):
            client.tenants.preferences.items.with_raw_response.delete(
                topic_id="",
                tenant_id="tenant_id",
            )


class TestAsyncItems:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCourier) -> None:
        item = await async_client.tenants.preferences.items.update(
            topic_id="topic_id",
            tenant_id="tenant_id",
            status="OPTED_IN",
        )
        assert item is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCourier) -> None:
        item = await async_client.tenants.preferences.items.update(
            topic_id="topic_id",
            tenant_id="tenant_id",
            status="OPTED_IN",
            custom_routing=["inbox"],
            has_custom_routing=True,
        )
        assert item is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCourier) -> None:
        response = await async_client.tenants.preferences.items.with_raw_response.update(
            topic_id="topic_id",
            tenant_id="tenant_id",
            status="OPTED_IN",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert item is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCourier) -> None:
        async with async_client.tenants.preferences.items.with_streaming_response.update(
            topic_id="topic_id",
            tenant_id="tenant_id",
            status="OPTED_IN",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert item is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.tenants.preferences.items.with_raw_response.update(
                topic_id="topic_id",
                tenant_id="",
                status="OPTED_IN",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `topic_id` but received ''"):
            await async_client.tenants.preferences.items.with_raw_response.update(
                topic_id="",
                tenant_id="tenant_id",
                status="OPTED_IN",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCourier) -> None:
        item = await async_client.tenants.preferences.items.delete(
            topic_id="topic_id",
            tenant_id="tenant_id",
        )
        assert item is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCourier) -> None:
        response = await async_client.tenants.preferences.items.with_raw_response.delete(
            topic_id="topic_id",
            tenant_id="tenant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert item is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCourier) -> None:
        async with async_client.tenants.preferences.items.with_streaming_response.delete(
            topic_id="topic_id",
            tenant_id="tenant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert item is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.tenants.preferences.items.with_raw_response.delete(
                topic_id="topic_id",
                tenant_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `topic_id` but received ''"):
            await async_client.tenants.preferences.items.with_raw_response.delete(
                topic_id="",
                tenant_id="tenant_id",
            )
