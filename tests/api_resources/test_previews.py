# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types import (
    DeviceSet,
    DeviceSetListResponse,
    PreviewDeviceListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPreviews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive_device_set(self, client: Courier) -> None:
        preview = client.previews.archive_device_set(
            "deviceSetId",
        )
        assert_matches_type(DeviceSet, preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_archive_device_set(self, client: Courier) -> None:
        response = client.previews.with_raw_response.archive_device_set(
            "deviceSetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = response.parse()
        assert_matches_type(DeviceSet, preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_archive_device_set(self, client: Courier) -> None:
        with client.previews.with_streaming_response.archive_device_set(
            "deviceSetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = response.parse()
            assert_matches_type(DeviceSet, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_archive_device_set(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_set_id` but received ''"):
            client.previews.with_raw_response.archive_device_set(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_device_set(self, client: Courier) -> None:
        preview = client.previews.create_device_set(
            device_ids=["pvd_1w6dgafr3aaycvv9a8bm996pkc"],
            name="Mobile",
        )
        assert_matches_type(DeviceSet, preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_device_set(self, client: Courier) -> None:
        response = client.previews.with_raw_response.create_device_set(
            device_ids=["pvd_1w6dgafr3aaycvv9a8bm996pkc"],
            name="Mobile",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = response.parse()
        assert_matches_type(DeviceSet, preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_device_set(self, client: Courier) -> None:
        with client.previews.with_streaming_response.create_device_set(
            device_ids=["pvd_1w6dgafr3aaycvv9a8bm996pkc"],
            name="Mobile",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = response.parse()
            assert_matches_type(DeviceSet, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_device_sets(self, client: Courier) -> None:
        preview = client.previews.list_device_sets()
        assert_matches_type(DeviceSetListResponse, preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_device_sets(self, client: Courier) -> None:
        response = client.previews.with_raw_response.list_device_sets()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = response.parse()
        assert_matches_type(DeviceSetListResponse, preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_device_sets(self, client: Courier) -> None:
        with client.previews.with_streaming_response.list_device_sets() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = response.parse()
            assert_matches_type(DeviceSetListResponse, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_devices(self, client: Courier) -> None:
        preview = client.previews.list_devices()
        assert_matches_type(PreviewDeviceListResponse, preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_devices(self, client: Courier) -> None:
        response = client.previews.with_raw_response.list_devices()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = response.parse()
        assert_matches_type(PreviewDeviceListResponse, preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_devices(self, client: Courier) -> None:
        with client.previews.with_streaming_response.list_devices() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = response.parse()
            assert_matches_type(PreviewDeviceListResponse, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_device_set(self, client: Courier) -> None:
        preview = client.previews.retrieve_device_set(
            "deviceSetId",
        )
        assert_matches_type(DeviceSet, preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_device_set(self, client: Courier) -> None:
        response = client.previews.with_raw_response.retrieve_device_set(
            "deviceSetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = response.parse()
        assert_matches_type(DeviceSet, preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_device_set(self, client: Courier) -> None:
        with client.previews.with_streaming_response.retrieve_device_set(
            "deviceSetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = response.parse()
            assert_matches_type(DeviceSet, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_device_set(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_set_id` but received ''"):
            client.previews.with_raw_response.retrieve_device_set(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_device_set(self, client: Courier) -> None:
        preview = client.previews.update_device_set(
            device_set_id="deviceSetId",
            device_ids=["pvd_1w6dgafr3aaycvv9a8bm996pkc", "pvd_34qvmj6p4dbqaa5mpys1ekt9jx"],
            name="Mobile and desktop",
        )
        assert_matches_type(DeviceSet, preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_device_set(self, client: Courier) -> None:
        response = client.previews.with_raw_response.update_device_set(
            device_set_id="deviceSetId",
            device_ids=["pvd_1w6dgafr3aaycvv9a8bm996pkc", "pvd_34qvmj6p4dbqaa5mpys1ekt9jx"],
            name="Mobile and desktop",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = response.parse()
        assert_matches_type(DeviceSet, preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_device_set(self, client: Courier) -> None:
        with client.previews.with_streaming_response.update_device_set(
            device_set_id="deviceSetId",
            device_ids=["pvd_1w6dgafr3aaycvv9a8bm996pkc", "pvd_34qvmj6p4dbqaa5mpys1ekt9jx"],
            name="Mobile and desktop",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = response.parse()
            assert_matches_type(DeviceSet, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_device_set(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_set_id` but received ''"):
            client.previews.with_raw_response.update_device_set(
                device_set_id="",
                device_ids=["pvd_1w6dgafr3aaycvv9a8bm996pkc", "pvd_34qvmj6p4dbqaa5mpys1ekt9jx"],
                name="Mobile and desktop",
            )


class TestAsyncPreviews:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive_device_set(self, async_client: AsyncCourier) -> None:
        preview = await async_client.previews.archive_device_set(
            "deviceSetId",
        )
        assert_matches_type(DeviceSet, preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_archive_device_set(self, async_client: AsyncCourier) -> None:
        response = await async_client.previews.with_raw_response.archive_device_set(
            "deviceSetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = await response.parse()
        assert_matches_type(DeviceSet, preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_archive_device_set(self, async_client: AsyncCourier) -> None:
        async with async_client.previews.with_streaming_response.archive_device_set(
            "deviceSetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = await response.parse()
            assert_matches_type(DeviceSet, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_archive_device_set(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_set_id` but received ''"):
            await async_client.previews.with_raw_response.archive_device_set(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_device_set(self, async_client: AsyncCourier) -> None:
        preview = await async_client.previews.create_device_set(
            device_ids=["pvd_1w6dgafr3aaycvv9a8bm996pkc"],
            name="Mobile",
        )
        assert_matches_type(DeviceSet, preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_device_set(self, async_client: AsyncCourier) -> None:
        response = await async_client.previews.with_raw_response.create_device_set(
            device_ids=["pvd_1w6dgafr3aaycvv9a8bm996pkc"],
            name="Mobile",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = await response.parse()
        assert_matches_type(DeviceSet, preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_device_set(self, async_client: AsyncCourier) -> None:
        async with async_client.previews.with_streaming_response.create_device_set(
            device_ids=["pvd_1w6dgafr3aaycvv9a8bm996pkc"],
            name="Mobile",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = await response.parse()
            assert_matches_type(DeviceSet, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_device_sets(self, async_client: AsyncCourier) -> None:
        preview = await async_client.previews.list_device_sets()
        assert_matches_type(DeviceSetListResponse, preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_device_sets(self, async_client: AsyncCourier) -> None:
        response = await async_client.previews.with_raw_response.list_device_sets()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = await response.parse()
        assert_matches_type(DeviceSetListResponse, preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_device_sets(self, async_client: AsyncCourier) -> None:
        async with async_client.previews.with_streaming_response.list_device_sets() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = await response.parse()
            assert_matches_type(DeviceSetListResponse, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_devices(self, async_client: AsyncCourier) -> None:
        preview = await async_client.previews.list_devices()
        assert_matches_type(PreviewDeviceListResponse, preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_devices(self, async_client: AsyncCourier) -> None:
        response = await async_client.previews.with_raw_response.list_devices()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = await response.parse()
        assert_matches_type(PreviewDeviceListResponse, preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_devices(self, async_client: AsyncCourier) -> None:
        async with async_client.previews.with_streaming_response.list_devices() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = await response.parse()
            assert_matches_type(PreviewDeviceListResponse, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_device_set(self, async_client: AsyncCourier) -> None:
        preview = await async_client.previews.retrieve_device_set(
            "deviceSetId",
        )
        assert_matches_type(DeviceSet, preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_device_set(self, async_client: AsyncCourier) -> None:
        response = await async_client.previews.with_raw_response.retrieve_device_set(
            "deviceSetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = await response.parse()
        assert_matches_type(DeviceSet, preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_device_set(self, async_client: AsyncCourier) -> None:
        async with async_client.previews.with_streaming_response.retrieve_device_set(
            "deviceSetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = await response.parse()
            assert_matches_type(DeviceSet, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_device_set(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_set_id` but received ''"):
            await async_client.previews.with_raw_response.retrieve_device_set(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_device_set(self, async_client: AsyncCourier) -> None:
        preview = await async_client.previews.update_device_set(
            device_set_id="deviceSetId",
            device_ids=["pvd_1w6dgafr3aaycvv9a8bm996pkc", "pvd_34qvmj6p4dbqaa5mpys1ekt9jx"],
            name="Mobile and desktop",
        )
        assert_matches_type(DeviceSet, preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_device_set(self, async_client: AsyncCourier) -> None:
        response = await async_client.previews.with_raw_response.update_device_set(
            device_set_id="deviceSetId",
            device_ids=["pvd_1w6dgafr3aaycvv9a8bm996pkc", "pvd_34qvmj6p4dbqaa5mpys1ekt9jx"],
            name="Mobile and desktop",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = await response.parse()
        assert_matches_type(DeviceSet, preview, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_device_set(self, async_client: AsyncCourier) -> None:
        async with async_client.previews.with_streaming_response.update_device_set(
            device_set_id="deviceSetId",
            device_ids=["pvd_1w6dgafr3aaycvv9a8bm996pkc", "pvd_34qvmj6p4dbqaa5mpys1ekt9jx"],
            name="Mobile and desktop",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = await response.parse()
            assert_matches_type(DeviceSet, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_device_set(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `device_set_id` but received ''"):
            await async_client.previews.with_raw_response.update_device_set(
                device_set_id="",
                device_ids=["pvd_1w6dgafr3aaycvv9a8bm996pkc", "pvd_34qvmj6p4dbqaa5mpys1ekt9jx"],
                name="Mobile and desktop",
            )
