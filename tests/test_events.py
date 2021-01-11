import responses
import pytest

from trycourier.client import Courier
from trycourier.exceptions import CourierAPIException

@responses.activate
def test_success_events_list():
    responses.add(
        responses.GET,
        'https://api.courier.com/events',
        status=200,
        content_type='application/json',
        body='{"results": []}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.events.list()

    assert r == {"results": []}


@responses.activate
def test_fail_events_list():
    responses.add(
        responses.GET,
        'https://api.courier.com/events',
        status=400,
        content_type='application/json',
        body='{"message": "An error occurred"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.events.list()


@responses.activate
def test_success_events_get():
    responses.add(
        responses.GET,
        'https://api.courier.com/events/my.event.id',
        status=200,
        content_type='application/json',
        body='{"status": "DELIVERED"}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.events.get(
        event_id='my.event.id',
    )

    assert r == {"status": "DELIVERED"}


@responses.activate
def test_fail_events_get():
    responses.add(
        responses.GET,
        'https://api.courier.com/events/my.event.id',
        status=400,
        content_type='application/json',
        body='{"message": "Not Found"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.events.get("my.event.id")


@responses.activate
def test_success_events_replace():
    responses.add(
        responses.PUT,
        'https://api.courier.com/events/my.event.id',
        status=200,
        content_type='application/json',
        body='{"id": "notification-id-1", "type": "notification"}'
    )

    c = Courier(auth_token='123456789ABCDF')
    r = c.events.replace(event_id="my.event.id", notification_id = "my.notification.id")

    assert r == {"id": "notification-id-1", "type": "notification"}

@responses.activate
def test_fail_events_replace():
    responses.add(
        responses.PUT,
        'https://api.courier.com/events/my.event.id',
        status=400,
        content_type='application/json',
        body='{"message": "An error occured"}'
    )

    c = Courier(auth_token='123456789ABCDF')

    with pytest.raises(CourierAPIException):
        c.events.replace(event_id="my.event.id", notification_id="notification-id-1")


