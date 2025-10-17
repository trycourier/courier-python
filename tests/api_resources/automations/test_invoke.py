# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types import AutomationInvokeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvoke:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_invoke_ad_hoc(self, client: Courier) -> None:
        invoke = client.automations.invoke.invoke_ad_hoc(
            automation={"steps": [{"action": "delay"}, {"action": "send"}]},
        )
        assert_matches_type(AutomationInvokeResponse, invoke, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_invoke_ad_hoc_with_all_params(self, client: Courier) -> None:
        invoke = client.automations.invoke.invoke_ad_hoc(
            automation={
                "steps": [
                    {
                        "action": "delay",
                        "duration": "duration",
                        "until": "20240408T080910.123",
                    },
                    {
                        "action": "send",
                        "brand": "brand",
                        "data": {"foo": "bar"},
                        "profile": {"foo": "bar"},
                        "recipient": "recipient",
                        "template": "64TP5HKPFTM8VTK1Y75SJDQX9JK0",
                    },
                ],
                "cancelation_token": "delay-send--user-yes--abc-123",
            },
            brand="brand",
            data={"name": "bar"},
            profile={"tenant_id": "bar"},
            recipient="user-yes",
            template="template",
        )
        assert_matches_type(AutomationInvokeResponse, invoke, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_invoke_ad_hoc(self, client: Courier) -> None:
        response = client.automations.invoke.with_raw_response.invoke_ad_hoc(
            automation={"steps": [{"action": "delay"}, {"action": "send"}]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoke = response.parse()
        assert_matches_type(AutomationInvokeResponse, invoke, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_invoke_ad_hoc(self, client: Courier) -> None:
        with client.automations.invoke.with_streaming_response.invoke_ad_hoc(
            automation={"steps": [{"action": "delay"}, {"action": "send"}]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoke = response.parse()
            assert_matches_type(AutomationInvokeResponse, invoke, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_invoke_by_template(self, client: Courier) -> None:
        invoke = client.automations.invoke.invoke_by_template(
            template_id="templateId",
            recipient="recipient",
        )
        assert_matches_type(AutomationInvokeResponse, invoke, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_invoke_by_template_with_all_params(self, client: Courier) -> None:
        invoke = client.automations.invoke.invoke_by_template(
            template_id="templateId",
            recipient="recipient",
            brand="brand",
            data={"foo": "bar"},
            profile={"foo": "bar"},
            template="template",
        )
        assert_matches_type(AutomationInvokeResponse, invoke, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_invoke_by_template(self, client: Courier) -> None:
        response = client.automations.invoke.with_raw_response.invoke_by_template(
            template_id="templateId",
            recipient="recipient",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoke = response.parse()
        assert_matches_type(AutomationInvokeResponse, invoke, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_invoke_by_template(self, client: Courier) -> None:
        with client.automations.invoke.with_streaming_response.invoke_by_template(
            template_id="templateId",
            recipient="recipient",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoke = response.parse()
            assert_matches_type(AutomationInvokeResponse, invoke, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_invoke_by_template(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.automations.invoke.with_raw_response.invoke_by_template(
                template_id="",
                recipient="recipient",
            )


class TestAsyncInvoke:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_invoke_ad_hoc(self, async_client: AsyncCourier) -> None:
        invoke = await async_client.automations.invoke.invoke_ad_hoc(
            automation={"steps": [{"action": "delay"}, {"action": "send"}]},
        )
        assert_matches_type(AutomationInvokeResponse, invoke, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_invoke_ad_hoc_with_all_params(self, async_client: AsyncCourier) -> None:
        invoke = await async_client.automations.invoke.invoke_ad_hoc(
            automation={
                "steps": [
                    {
                        "action": "delay",
                        "duration": "duration",
                        "until": "20240408T080910.123",
                    },
                    {
                        "action": "send",
                        "brand": "brand",
                        "data": {"foo": "bar"},
                        "profile": {"foo": "bar"},
                        "recipient": "recipient",
                        "template": "64TP5HKPFTM8VTK1Y75SJDQX9JK0",
                    },
                ],
                "cancelation_token": "delay-send--user-yes--abc-123",
            },
            brand="brand",
            data={"name": "bar"},
            profile={"tenant_id": "bar"},
            recipient="user-yes",
            template="template",
        )
        assert_matches_type(AutomationInvokeResponse, invoke, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_invoke_ad_hoc(self, async_client: AsyncCourier) -> None:
        response = await async_client.automations.invoke.with_raw_response.invoke_ad_hoc(
            automation={"steps": [{"action": "delay"}, {"action": "send"}]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoke = await response.parse()
        assert_matches_type(AutomationInvokeResponse, invoke, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_invoke_ad_hoc(self, async_client: AsyncCourier) -> None:
        async with async_client.automations.invoke.with_streaming_response.invoke_ad_hoc(
            automation={"steps": [{"action": "delay"}, {"action": "send"}]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoke = await response.parse()
            assert_matches_type(AutomationInvokeResponse, invoke, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_invoke_by_template(self, async_client: AsyncCourier) -> None:
        invoke = await async_client.automations.invoke.invoke_by_template(
            template_id="templateId",
            recipient="recipient",
        )
        assert_matches_type(AutomationInvokeResponse, invoke, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_invoke_by_template_with_all_params(self, async_client: AsyncCourier) -> None:
        invoke = await async_client.automations.invoke.invoke_by_template(
            template_id="templateId",
            recipient="recipient",
            brand="brand",
            data={"foo": "bar"},
            profile={"foo": "bar"},
            template="template",
        )
        assert_matches_type(AutomationInvokeResponse, invoke, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_invoke_by_template(self, async_client: AsyncCourier) -> None:
        response = await async_client.automations.invoke.with_raw_response.invoke_by_template(
            template_id="templateId",
            recipient="recipient",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoke = await response.parse()
        assert_matches_type(AutomationInvokeResponse, invoke, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_invoke_by_template(self, async_client: AsyncCourier) -> None:
        async with async_client.automations.invoke.with_streaming_response.invoke_by_template(
            template_id="templateId",
            recipient="recipient",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoke = await response.parse()
            assert_matches_type(AutomationInvokeResponse, invoke, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_invoke_by_template(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.automations.invoke.with_raw_response.invoke_by_template(
                template_id="",
                recipient="recipient",
            )
