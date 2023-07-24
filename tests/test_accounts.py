import json
import responses
import pytest
from os import environ
from datetime import datetime, timedelta

from trycourier.client import Courier
from trycourier.exceptions import CourierAPIException

@responses.activate
def test_success_get_account():
    responses.add(
        responses.GET,
        'https://api.courier.com/accounts/account-001',
        status=200,
        content_type='application/json',
        body='{"id":"ACME", "name":"ACME Inc", "properties":{}, "default_preferences":{}, "user_profile":{}}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.accounts.get_account("account-001")

    assert r == {
      "id":"ACME",
      "name":"ACME Inc",
      "properties":{},
      "default_preferences":{},
      "user_profile":{}
    }

@responses.activate
def test_success_get_accounts():
    responses.add(
        responses.GET,
        'https://api.courier.com/accounts',
        status=200,
        content_type='application/json',
        body='{"items":[{"id":"ACME", "name":"ACME Inc", "properties":{}, "default_preferences":{}, "user_profile":{}}], "has_more": false}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.accounts.get_accounts()

    assert r == {
      "items": [{
        "id":"ACME",
        "name":"ACME Inc",
        "properties":{},
        "default_preferences":{},
        "user_profile":{}
      }],
      "has_more": False
    }

@responses.activate
def test_success_put_account():
    responses.add(
        responses.PUT,
        'https://api.courier.com/accounts/account-1',
        status=200,
        content_type='application/json',
        body='{"id":"ACME", "name":"ACME Inc", "properties":{}, "default_preferences":{}, "user_profile":{}}'
    )
    c = Courier(auth_token='123456789ABCDF')
    r = c.accounts.put_account(
        'account-1',
        account={
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
def test_success_delete_account():
    responses.add(
        responses.DELETE,
        'https://api.courier.com/accounts/account-1',
        status=204,
        content_type='application/json'
    )

    c = Courier(auth_token='123456789ABCDF')
    c.accounts.delete_account("account-1")

    assert len(responses.calls) == 1
