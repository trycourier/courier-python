# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types.notifications import CheckListResponse, CheckUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChecks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Courier) -> None:
        check = client.notifications.checks.update(
            submission_id="submissionId",
            id="id",
            checks=[
                {
                    "id": "id",
                    "status": "RESOLVED",
                    "type": "custom",
                }
            ],
        )
        assert_matches_type(CheckUpdateResponse, check, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Courier) -> None:
        response = client.notifications.checks.with_raw_response.update(
            submission_id="submissionId",
            id="id",
            checks=[
                {
                    "id": "id",
                    "status": "RESOLVED",
                    "type": "custom",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check = response.parse()
        assert_matches_type(CheckUpdateResponse, check, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Courier) -> None:
        with client.notifications.checks.with_streaming_response.update(
            submission_id="submissionId",
            id="id",
            checks=[
                {
                    "id": "id",
                    "status": "RESOLVED",
                    "type": "custom",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check = response.parse()
            assert_matches_type(CheckUpdateResponse, check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.notifications.checks.with_raw_response.update(
                submission_id="submissionId",
                id="",
                checks=[
                    {
                        "id": "id",
                        "status": "RESOLVED",
                        "type": "custom",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `submission_id` but received ''"):
            client.notifications.checks.with_raw_response.update(
                submission_id="",
                id="id",
                checks=[
                    {
                        "id": "id",
                        "status": "RESOLVED",
                        "type": "custom",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Courier) -> None:
        check = client.notifications.checks.list(
            submission_id="submissionId",
            id="id",
        )
        assert_matches_type(CheckListResponse, check, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Courier) -> None:
        response = client.notifications.checks.with_raw_response.list(
            submission_id="submissionId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check = response.parse()
        assert_matches_type(CheckListResponse, check, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Courier) -> None:
        with client.notifications.checks.with_streaming_response.list(
            submission_id="submissionId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check = response.parse()
            assert_matches_type(CheckListResponse, check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.notifications.checks.with_raw_response.list(
                submission_id="submissionId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `submission_id` but received ''"):
            client.notifications.checks.with_raw_response.list(
                submission_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Courier) -> None:
        check = client.notifications.checks.delete(
            submission_id="submissionId",
            id="id",
        )
        assert check is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Courier) -> None:
        response = client.notifications.checks.with_raw_response.delete(
            submission_id="submissionId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check = response.parse()
        assert check is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Courier) -> None:
        with client.notifications.checks.with_streaming_response.delete(
            submission_id="submissionId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check = response.parse()
            assert check is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.notifications.checks.with_raw_response.delete(
                submission_id="submissionId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `submission_id` but received ''"):
            client.notifications.checks.with_raw_response.delete(
                submission_id="",
                id="id",
            )


class TestAsyncChecks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCourier) -> None:
        check = await async_client.notifications.checks.update(
            submission_id="submissionId",
            id="id",
            checks=[
                {
                    "id": "id",
                    "status": "RESOLVED",
                    "type": "custom",
                }
            ],
        )
        assert_matches_type(CheckUpdateResponse, check, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCourier) -> None:
        response = await async_client.notifications.checks.with_raw_response.update(
            submission_id="submissionId",
            id="id",
            checks=[
                {
                    "id": "id",
                    "status": "RESOLVED",
                    "type": "custom",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check = await response.parse()
        assert_matches_type(CheckUpdateResponse, check, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCourier) -> None:
        async with async_client.notifications.checks.with_streaming_response.update(
            submission_id="submissionId",
            id="id",
            checks=[
                {
                    "id": "id",
                    "status": "RESOLVED",
                    "type": "custom",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check = await response.parse()
            assert_matches_type(CheckUpdateResponse, check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.notifications.checks.with_raw_response.update(
                submission_id="submissionId",
                id="",
                checks=[
                    {
                        "id": "id",
                        "status": "RESOLVED",
                        "type": "custom",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `submission_id` but received ''"):
            await async_client.notifications.checks.with_raw_response.update(
                submission_id="",
                id="id",
                checks=[
                    {
                        "id": "id",
                        "status": "RESOLVED",
                        "type": "custom",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCourier) -> None:
        check = await async_client.notifications.checks.list(
            submission_id="submissionId",
            id="id",
        )
        assert_matches_type(CheckListResponse, check, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCourier) -> None:
        response = await async_client.notifications.checks.with_raw_response.list(
            submission_id="submissionId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check = await response.parse()
        assert_matches_type(CheckListResponse, check, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCourier) -> None:
        async with async_client.notifications.checks.with_streaming_response.list(
            submission_id="submissionId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check = await response.parse()
            assert_matches_type(CheckListResponse, check, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.notifications.checks.with_raw_response.list(
                submission_id="submissionId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `submission_id` but received ''"):
            await async_client.notifications.checks.with_raw_response.list(
                submission_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCourier) -> None:
        check = await async_client.notifications.checks.delete(
            submission_id="submissionId",
            id="id",
        )
        assert check is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCourier) -> None:
        response = await async_client.notifications.checks.with_raw_response.delete(
            submission_id="submissionId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check = await response.parse()
        assert check is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCourier) -> None:
        async with async_client.notifications.checks.with_streaming_response.delete(
            submission_id="submissionId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check = await response.parse()
            assert check is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.notifications.checks.with_raw_response.delete(
                submission_id="submissionId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `submission_id` but received ''"):
            await async_client.notifications.checks.with_raw_response.delete(
                submission_id="",
                id="id",
            )
