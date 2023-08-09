import json
import responses
import pytest
from os import environ
from datetime import datetime, timedelta

from trycourier.client import Courier
from trycourier.exceptions import CourierAPIException

@responses.activate
def test_success_get_tenant():
    responses.add(
        responses.GET,
        'https://api.courier.com/tenants/tenant-001',
        status=200,
        content_type='application/json',
        body='{"id":"ACME", "name":"ACME Inc", "properties":{}, "default_preferences":{}, "user_profile":{}}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.tenants.get_tenant("tenant-001")

    assert r == {
      "id":"ACME",
      "name":"ACME Inc",
      "properties":{},
      "default_preferences":{},
      "user_profile":{}
    }

@responses.activate
def test_success_get_tenants():
    responses.add(
        responses.GET,
        'https://api.courier.com/tenants',
        status=200,
        content_type='application/json',
        body='{"items":[{"id":"ACME", "name":"ACME Inc", "properties":{}, "default_preferences":{}, "user_profile":{}}], "has_more": false, "next_url": null, "url": "/tenants"}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.tenants.get_tenants()

    assert r == {
      "items": [{
        "id":"ACME",
        "name":"ACME Inc",
        "properties":{},
        "default_preferences":{},
        "user_profile":{}
      }],
      "has_more": False,
      "next_url": None,
      "url": "/tenants",
    }

@responses.activate
def test_success_put_tenant():
    responses.add(
        responses.PUT,
        'https://api.courier.com/tenants/tenant-1',
        status=200,
        content_type='application/json',
        body='{"id":"ACME", "name":"ACME Inc", "properties":{}, "default_preferences":{}, "user_profile":{}}'
    )
    c = Courier(auth_token='123456789ABCDF')
    r = c.tenants.put_tenant(
        'tenant-1',
        tenant={
          "name":"ACME Inc",
          "properties":{},
          "default_preferences":{},
          "user_profile":{}
        },
    )

    assert r == {
      "id":"ACME",
      "name":"ACME Inc",
      "properties":{},
      "default_preferences":{},
      "user_profile":{}
    }

@responses.activate
def test_success_delete_tenant():
    responses.add(
        responses.DELETE,
        'https://api.courier.com/tenants/tenant-1',
        status=204,
        content_type='application/json'
    )

    c = Courier(auth_token='123456789ABCDF')
    c.tenants.delete_tenant("tenant-1")

    assert len(responses.calls) == 1
