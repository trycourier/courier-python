# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types import DigestInstanceListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSchedules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_instances(self, client: Courier) -> None:
        schedule = client.digests.schedules.list_instances(
            schedule_id="schedule_id",
        )
        assert_matches_type(DigestInstanceListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_instances_with_all_params(self, client: Courier) -> None:
        schedule = client.digests.schedules.list_instances(
            schedule_id="schedule_id",
            cursor="cursor",
            limit=100,
        )
        assert_matches_type(DigestInstanceListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_instances(self, client: Courier) -> None:
        response = client.digests.schedules.with_raw_response.list_instances(
            schedule_id="schedule_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(DigestInstanceListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_instances(self, client: Courier) -> None:
        with client.digests.schedules.with_streaming_response.list_instances(
            schedule_id="schedule_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(DigestInstanceListResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_instances(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            client.digests.schedules.with_raw_response.list_instances(
                schedule_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_release(self, client: Courier) -> None:
        schedule = client.digests.schedules.release(
            "schedule_id",
        )
        assert schedule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_release(self, client: Courier) -> None:
        response = client.digests.schedules.with_raw_response.release(
            "schedule_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert schedule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_release(self, client: Courier) -> None:
        with client.digests.schedules.with_streaming_response.release(
            "schedule_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert schedule is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_release(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            client.digests.schedules.with_raw_response.release(
                "",
            )


class TestAsyncSchedules:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_instances(self, async_client: AsyncCourier) -> None:
        schedule = await async_client.digests.schedules.list_instances(
            schedule_id="schedule_id",
        )
        assert_matches_type(DigestInstanceListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_instances_with_all_params(self, async_client: AsyncCourier) -> None:
        schedule = await async_client.digests.schedules.list_instances(
            schedule_id="schedule_id",
            cursor="cursor",
            limit=100,
        )
        assert_matches_type(DigestInstanceListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_instances(self, async_client: AsyncCourier) -> None:
        response = await async_client.digests.schedules.with_raw_response.list_instances(
            schedule_id="schedule_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(DigestInstanceListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_instances(self, async_client: AsyncCourier) -> None:
        async with async_client.digests.schedules.with_streaming_response.list_instances(
            schedule_id="schedule_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(DigestInstanceListResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_instances(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            await async_client.digests.schedules.with_raw_response.list_instances(
                schedule_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_release(self, async_client: AsyncCourier) -> None:
        schedule = await async_client.digests.schedules.release(
            "schedule_id",
        )
        assert schedule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_release(self, async_client: AsyncCourier) -> None:
        response = await async_client.digests.schedules.with_raw_response.release(
            "schedule_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert schedule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_release(self, async_client: AsyncCourier) -> None:
        async with async_client.digests.schedules.with_streaming_response.release(
            "schedule_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert schedule is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_release(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `schedule_id` but received ''"):
            await async_client.digests.schedules.with_raw_response.release(
                "",
            )
