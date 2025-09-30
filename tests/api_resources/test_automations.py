# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types.automations import AutomationInvokeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAutomations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_invoke_ad_hoc(self, client: Courier) -> None:
        automation = client.automations.invoke_ad_hoc(
            automation={
                "steps": [
                    {
                        "action": "add-to-digest",
                        "subscription_topic_id": "RAJE97CMT04KDJJ88ZDS2TP1690S",
                    }
                ]
            },
        )
        assert_matches_type(AutomationInvokeResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_invoke_ad_hoc_with_all_params(self, client: Courier) -> None:
        automation = client.automations.invoke_ad_hoc(
            automation={
                "steps": [
                    {
                        "if": "if",
                        "ref": "ref",
                        "action": "add-to-digest",
                        "subscription_topic_id": "RAJE97CMT04KDJJ88ZDS2TP1690S",
                    }
                ],
                "cancelation_token": "cancelation_token",
            },
            brand="brand",
            data={"foo": "bar"},
            profile={},
            recipient="recipient",
            template="template",
        )
        assert_matches_type(AutomationInvokeResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_invoke_ad_hoc(self, client: Courier) -> None:
        response = client.automations.with_raw_response.invoke_ad_hoc(
            automation={
                "steps": [
                    {
                        "action": "add-to-digest",
                        "subscription_topic_id": "RAJE97CMT04KDJJ88ZDS2TP1690S",
                    }
                ]
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = response.parse()
        assert_matches_type(AutomationInvokeResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_invoke_ad_hoc(self, client: Courier) -> None:
        with client.automations.with_streaming_response.invoke_ad_hoc(
            automation={
                "steps": [
                    {
                        "action": "add-to-digest",
                        "subscription_topic_id": "RAJE97CMT04KDJJ88ZDS2TP1690S",
                    }
                ]
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = response.parse()
            assert_matches_type(AutomationInvokeResponse, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_invoke_by_template(self, client: Courier) -> None:
        automation = client.automations.invoke_by_template(
            template_id="templateId",
        )
        assert_matches_type(AutomationInvokeResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_invoke_by_template_with_all_params(self, client: Courier) -> None:
        automation = client.automations.invoke_by_template(
            template_id="templateId",
            brand="brand",
            data={"foo": "bar"},
            profile={},
            recipient="recipient",
            template="template",
        )
        assert_matches_type(AutomationInvokeResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_invoke_by_template(self, client: Courier) -> None:
        response = client.automations.with_raw_response.invoke_by_template(
            template_id="templateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = response.parse()
        assert_matches_type(AutomationInvokeResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_invoke_by_template(self, client: Courier) -> None:
        with client.automations.with_streaming_response.invoke_by_template(
            template_id="templateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = response.parse()
            assert_matches_type(AutomationInvokeResponse, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_invoke_by_template(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.automations.with_raw_response.invoke_by_template(
                template_id="",
            )


class TestAsyncAutomations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_invoke_ad_hoc(self, async_client: AsyncCourier) -> None:
        automation = await async_client.automations.invoke_ad_hoc(
            automation={
                "steps": [
                    {
                        "action": "add-to-digest",
                        "subscription_topic_id": "RAJE97CMT04KDJJ88ZDS2TP1690S",
                    }
                ]
            },
        )
        assert_matches_type(AutomationInvokeResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_invoke_ad_hoc_with_all_params(self, async_client: AsyncCourier) -> None:
        automation = await async_client.automations.invoke_ad_hoc(
            automation={
                "steps": [
                    {
                        "if": "if",
                        "ref": "ref",
                        "action": "add-to-digest",
                        "subscription_topic_id": "RAJE97CMT04KDJJ88ZDS2TP1690S",
                    }
                ],
                "cancelation_token": "cancelation_token",
            },
            brand="brand",
            data={"foo": "bar"},
            profile={},
            recipient="recipient",
            template="template",
        )
        assert_matches_type(AutomationInvokeResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_invoke_ad_hoc(self, async_client: AsyncCourier) -> None:
        response = await async_client.automations.with_raw_response.invoke_ad_hoc(
            automation={
                "steps": [
                    {
                        "action": "add-to-digest",
                        "subscription_topic_id": "RAJE97CMT04KDJJ88ZDS2TP1690S",
                    }
                ]
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = await response.parse()
        assert_matches_type(AutomationInvokeResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_invoke_ad_hoc(self, async_client: AsyncCourier) -> None:
        async with async_client.automations.with_streaming_response.invoke_ad_hoc(
            automation={
                "steps": [
                    {
                        "action": "add-to-digest",
                        "subscription_topic_id": "RAJE97CMT04KDJJ88ZDS2TP1690S",
                    }
                ]
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = await response.parse()
            assert_matches_type(AutomationInvokeResponse, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_invoke_by_template(self, async_client: AsyncCourier) -> None:
        automation = await async_client.automations.invoke_by_template(
            template_id="templateId",
        )
        assert_matches_type(AutomationInvokeResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_invoke_by_template_with_all_params(self, async_client: AsyncCourier) -> None:
        automation = await async_client.automations.invoke_by_template(
            template_id="templateId",
            brand="brand",
            data={"foo": "bar"},
            profile={},
            recipient="recipient",
            template="template",
        )
        assert_matches_type(AutomationInvokeResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_invoke_by_template(self, async_client: AsyncCourier) -> None:
        response = await async_client.automations.with_raw_response.invoke_by_template(
            template_id="templateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = await response.parse()
        assert_matches_type(AutomationInvokeResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_invoke_by_template(self, async_client: AsyncCourier) -> None:
        async with async_client.automations.with_streaming_response.invoke_by_template(
            template_id="templateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = await response.parse()
            assert_matches_type(AutomationInvokeResponse, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_invoke_by_template(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.automations.with_raw_response.invoke_by_template(
                template_id="",
            )
