import json
import responses
import pytest
from os import environ
from datetime import datetime, timedelta

from trycourier.client import Courier
from trycourier.exceptions import CourierAPIException

@responses.activate
def test_success_get_audit_event():
    responses.add(
        responses.GET,
        'https://api.courier.com/audit-events/audit-event-001',
        status=200,
        content_type='application/json',
        body='{"actor": {"email": "foo@bar.com", "id": "foo-user"}, "auditEventId": "ZX3xXUMNKL4y2NkiKgstl", "source": "courier.studio", "target": {}, "timestamp": "2022-07-22T22:33:59.552Z", "type": "notification:published"}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.audit_events.get_audit_event("audit-event-001")

    assert r == {
      "actor": {
        "email": "foo@bar.com",
        "id": "foo-user"
      },
      "auditEventId": "ZX3xXUMNKL4y2NkiKgstl",
      "source": "courier.studio",
      "target": {},
      "timestamp": "2022-07-22T22:33:59.552Z",
      "type": "notification:published"
    }

@responses.activate
def test_success_list_audit_events():
    responses.add(
        responses.GET,
        'https://api.courier.com/audit-events?cursor=abc',
        status=200,
        content_type='application/json',
        body='{"paging": {"cursor": "def" }, "results": [{"actor": {"email": "foo@bar.com", "id": "foo-user"}, "auditEventId": "ZX3xXUMNKL4y2NkiKgstl", "source": "courier.studio", "target": {}, "timestamp": "2022-07-22T22:33:59.552Z", "type": "notification:published"}]}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.audit_events.list_audit_events(cursor='abc')

    assert r == {
        "results": [
          {
            "actor": {"email": "foo@bar.com", "id": "foo-user"},
            "auditEventId": "ZX3xXUMNKL4y2NkiKgstl",
            "source": "courier.studio",
            "target": {},
            "timestamp": "2022-07-22T22:33:59.552Z",
            "type": "notification:published"
          }
        ],
        "paging": {
            "cursor": "def"
        }
    }
