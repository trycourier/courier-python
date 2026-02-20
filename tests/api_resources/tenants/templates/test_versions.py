# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types import BaseTemplateTenantAssociation

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVersions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Courier) -> None:
        version = client.tenants.templates.versions.retrieve(
            version="version",
            tenant_id="tenant_id",
            template_id="template_id",
        )
        assert_matches_type(BaseTemplateTenantAssociation, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Courier) -> None:
        response = client.tenants.templates.versions.with_raw_response.retrieve(
            version="version",
            tenant_id="tenant_id",
            template_id="template_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(BaseTemplateTenantAssociation, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Courier) -> None:
        with client.tenants.templates.versions.with_streaming_response.retrieve(
            version="version",
            tenant_id="tenant_id",
            template_id="template_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(BaseTemplateTenantAssociation, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.tenants.templates.versions.with_raw_response.retrieve(
                version="version",
                tenant_id="",
                template_id="template_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.tenants.templates.versions.with_raw_response.retrieve(
                version="version",
                tenant_id="tenant_id",
                template_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.tenants.templates.versions.with_raw_response.retrieve(
                version="",
                tenant_id="tenant_id",
                template_id="template_id",
            )


class TestAsyncVersions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCourier) -> None:
        version = await async_client.tenants.templates.versions.retrieve(
            version="version",
            tenant_id="tenant_id",
            template_id="template_id",
        )
        assert_matches_type(BaseTemplateTenantAssociation, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCourier) -> None:
        response = await async_client.tenants.templates.versions.with_raw_response.retrieve(
            version="version",
            tenant_id="tenant_id",
            template_id="template_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(BaseTemplateTenantAssociation, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCourier) -> None:
        async with async_client.tenants.templates.versions.with_streaming_response.retrieve(
            version="version",
            tenant_id="tenant_id",
            template_id="template_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(BaseTemplateTenantAssociation, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.tenants.templates.versions.with_raw_response.retrieve(
                version="version",
                tenant_id="",
                template_id="template_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.tenants.templates.versions.with_raw_response.retrieve(
                version="version",
                tenant_id="tenant_id",
                template_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.tenants.templates.versions.with_raw_response.retrieve(
                version="",
                tenant_id="tenant_id",
                template_id="template_id",
            )
