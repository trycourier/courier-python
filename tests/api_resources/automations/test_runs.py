# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types import AutomationRunListResponse, AutomationRunStepsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Courier) -> None:
        run = client.automations.runs.list()
        assert_matches_type(AutomationRunListResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Courier) -> None:
        run = client.automations.runs.list(
            cursor="cursor",
            end_date="end_date",
            limit="321669910225",
            start_date="start_date",
            status="status",
            template_id="template_id",
        )
        assert_matches_type(AutomationRunListResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Courier) -> None:
        response = client.automations.runs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(AutomationRunListResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Courier) -> None:
        with client.automations.runs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(AutomationRunListResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_steps(self, client: Courier) -> None:
        run = client.automations.runs.list_steps(
            "x",
        )
        assert_matches_type(AutomationRunStepsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_steps(self, client: Courier) -> None:
        response = client.automations.runs.with_raw_response.list_steps(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(AutomationRunStepsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_steps(self, client: Courier) -> None:
        with client.automations.runs.with_streaming_response.list_steps(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(AutomationRunStepsResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_steps(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.automations.runs.with_raw_response.list_steps(
                "",
            )


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCourier) -> None:
        run = await async_client.automations.runs.list()
        assert_matches_type(AutomationRunListResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCourier) -> None:
        run = await async_client.automations.runs.list(
            cursor="cursor",
            end_date="end_date",
            limit="321669910225",
            start_date="start_date",
            status="status",
            template_id="template_id",
        )
        assert_matches_type(AutomationRunListResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCourier) -> None:
        response = await async_client.automations.runs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(AutomationRunListResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCourier) -> None:
        async with async_client.automations.runs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(AutomationRunListResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_steps(self, async_client: AsyncCourier) -> None:
        run = await async_client.automations.runs.list_steps(
            "x",
        )
        assert_matches_type(AutomationRunStepsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_steps(self, async_client: AsyncCourier) -> None:
        response = await async_client.automations.runs.with_raw_response.list_steps(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(AutomationRunStepsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_steps(self, async_client: AsyncCourier) -> None:
        async with async_client.automations.runs.with_streaming_response.list_steps(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(AutomationRunStepsResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_steps(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.automations.runs.with_raw_response.list_steps(
                "",
            )
